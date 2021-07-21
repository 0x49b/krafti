import logging
from datetime import datetime
from django.db.models import Q

import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand

from routes.models import Route, RouteArchive, GradeScale, Category

logger = logging.getLogger('root')


class Command(BaseCommand):
    help = "Get opening Hours for Kraftreaktor"

    def handle(self, *args, **options):
        url = "https://kraftreaktor.ch/angebot/routenliste/"
        res = requests.get(url, allow_redirects=True)
        soup = BeautifulSoup(res.text, 'html.parser')
        tables = soup.findAll('table')
        loaded_routes = []
        i = 0
        for table in tables:
            tbody = table.find('tbody')

            trs = tbody.findAll('tr')
            for tr in trs:
                tds = tr.findAll('td')

                grade = tds[0].find('span').text.lstrip().rstrip()
                # print(grade)

                c = tds[0]['style']
                color_raw = c.split(":")
                color = color_raw[1].split(';')[0]

                name = tds[1].text.lstrip().rstrip()
                setter = tds[2].text.lstrip().rstrip()
                d = tds[3].text.lstrip().rstrip()
                date = datetime.strptime(d, "%d.%m.%Y")
                length = tds[4].text.lstrip().rstrip()
                route_num = tds[5].text.lstrip().rstrip()
                categorie = i + 1

                try:
                    grd = GradeScale.objects.filter(Q(french__iexact=grade)).first()
                except Exception as e:
                    print(e)
                    grd = None

                try:
                    cat = Category.objects.get(id=categorie)
                except Exception as e:
                    cat = None

                selfsecurity = ["30", "30.1", "30.2", "30.3", "30.4", "30.5", "30.6", "30.7", "30.8", "30.9",
                                "31", "31.1", "31.2", "31.3", "31.4", "31.5", "31.6", "31.7", "31.8", "31.9",
                                "32", "32.1", "32.2", "32.3", "32.4", "32.5", "32.6", "32.7", "32.8", "32.9",
                                "33", "33.1", "33.2", "33.3", "33.4", "33.5", "33.6", "33.7", "33.8", "33.9",
                                "34", "34.1", "34.2", "34.3", "34.4", "34.5", "34.6", "34.7", "34.8", "34.9"]

                if route_num in selfsecurity:
                    cat = Category.objects.get(slug__exact="sicherungsautomaten")

                if name == "":
                    name = "#%s" % grd.french

                loaded_routes.append(name)

                route, created = Route.objects.update_or_create(
                    grade=grd,
                    color=color,
                    name=name,
                    setter=setter,
                    date=date,
                    length=length,
                    route_num=route_num,
                    category=cat,
                )

                if created:
                    logger.info("Added new Route %s with Grade %s" % (route, route.grade.french))
                else:
                    logger.info("Got Route %s with Grade %s" % (route, route.grade.french))

            i = i + 1

        # Check the db routes if they are currently active
        logger.info("Checking active routes")
        db_routes = Route.objects.all()
        for db_route in db_routes:
            if db_route.name not in loaded_routes:
                db_route.archived = True
                db_route.save()

                if not RouteArchive.objects.filter(uuid=db_route.uuid).exists():
                    RouteArchive.objects.create(
                        uuid=db_route.uuid,
                        grd=db_route.grade,
                        color=db_route.color,
                        name=db_route.name,
                        setter=db_route.setter,
                        date=db_route.date,
                        length=db_route.length,
                        route_num=db_route.route_num,
                        category=db_route.category
                    )

        logger.info("finished loading routes")
