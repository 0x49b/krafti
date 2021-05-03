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

                grade = tds[0].find('span').text
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

                loaded_routes.append(name)
                try:
                    grd = GradeScale.objects.get(Q(french__iexact=grade))
                except Exception as e:
                    grd = None

                try:
                    cat = Category.objects.get(id=categorie)
                except Exception as e:
                    cat = None

                route, created = Route.objects.update_or_create(
                    grade=grade,
                    grd=grd,
                    color=color,
                    name=name,
                    setter=setter,
                    date=date,
                    length=length,
                    route_num=route_num,
                    category=cat,
                )

                if created:
                    logger.info("Added new Route %s" % route)
                else:
                    logger.info("Got Route %s " % route)

            i = i + 1

        # Check the db routes if they are currently active
        logger.info("Checking routes active")
        db_routes = Route.objects.all()
        for db_route in db_routes:
            if db_route.name not in loaded_routes:
                RouteArchive.objects.create(
                    grade=db_route.grade,
                    grd=db_route.grd,
                    color=db_route.color,
                    name=db_route.name,
                    setter=db_route.setter,
                    date=db_route.date,
                    length=db_route.length,
                    route_num=db_route.route_num,
                    category=db_route.category
                )

                db_route.delete()

        logger.info("finished loading routes")
