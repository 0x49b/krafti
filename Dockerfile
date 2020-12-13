FROM python:3

MAINTAINER Maintaner Florian Thiévent

# Set variables for project name, and where to place files in container.
ENV PROJECT=krafti
ENV CONTAINER_HOME=/opt
ENV CONTAINER_PROJECT=$CONTAINER_HOME/$PROJECT

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
COPY ./start.sh /

EXPOSE 8000
ENTRYPOINT ["/start.sh"]