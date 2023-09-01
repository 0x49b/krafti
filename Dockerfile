FROM python:3.11

LABEL Maintainer="Florian Thiévent"
LABEL traefik.enable="true"
LABEL traefik.http.middlewares.krafti-https-redirect.redirectscheme.scheme="https"
LABEL traefik.http.routers.krafti-secure.entrypoints="https"
LABEL traefik.http.routers.krafti-secure.rule="Host(`kr.thievent.org`)"
LABEL traefik.http.routers.krafti-secure.service="krafti"
LABEL traefik.http.routers.krafti-secure.tls="true"
LABEL traefik.http.routers.krafti-secure.tls.certresolver="http"
LABEL traefik.http.routers.krafti.entrypoints="http"
LABEL traefik.http.routers.krafti.middlewares="krafti-https-redirect"
LABEL traefik.http.routers.krafti.rule="Host(`kr.thievent.org`)"
LABEL traefik.http.routers.krafti.service="krafti"
LABEL traefik.http.routers.krafti.tls.certresolver="leresolver"
LABEL traefik.http.services.krafti.loadbalancer.server.port="8000"

# Set variables for project name, and where to place files in container.
ENV PROJECT=krafti
ENV CONTAINER_HOME=/opt
ENV CONTAINER_PROJECT=$CONTAINER_HOME/$PROJECT
ENV PERMANENT_CLOSED="22.01.2021 23:59:59"

# Image updates
# RUN apt-get update && apt-get upgrade

# Create application subdirectories
RUN mkdir $CONTAINER_PROJECT
WORKDIR $CONTAINER_PROJECT
RUN mkdir $CONTAINER_PROJECT/logs
RUN echo "" > $CONTAINER_PROJECT/logs/gunicorn.log
# Copy application source code to $CONTAINER_PROJECT
COPY . $CONTAINER_PROJECT

# Install Python dependencies
RUN pip install -r $CONTAINER_PROJECT/requirements.txt

# Copy and set entrypoint
WORKDIR $CONTAINER_PROJECT

RUN ["python", "manage.py", "migrate"]

COPY ./start.sh /
RUN ["chmod", "+x", "/opt/krafti/start.sh"]

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
