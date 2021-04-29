from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup
from routes.models import Route
from datetime import datetime
import logging

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
                categorie = i

                loaded_routes.append(name)

                route, created = Route.objects.update_or_create(
                    grade=grade,
                    color=color,
                    name=name,
                    setter=setter,
                    date=date,
                    length=length,
                    route_num=route_num,
                    categorie=categorie,
                )

                if created:
                    logger.info("Added new Route %s" % route)
                else:
                    logger.info("Got Route %s " % route)

            i = i + 1

        # Check the db routes if they are currently active
        db_routes = Route.objects.all()
        for db_route in db_routes:
            if db_route.name not in loaded_routes:
                db_route.active = False
                db_route.save()

        logger.info("finished loading routes")
