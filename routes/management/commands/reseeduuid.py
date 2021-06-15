import logging
import uuid
from datetime import datetime
from django.db.models import Q

import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand

from routes.models import Route, RouteArchive, GradeScale

logger = logging.getLogger('root')


class Command(BaseCommand):
    help = "update uuid on routearchive"

    def handle(self, *args, **options):
        routes = Route.objects.all()
        routes_archive = RouteArchive.objects.all()

        for route in routes:
            print("updating %s" % route.name)
            route.uuid = uuid.uuid4()
            route.save()

        for route in routes_archive:
            print("updtate route archive %s" % route.name)
            route.uuid = uuid.uuid4()
            route.save()
        '''
        grades = GradeScale.objects.all()
        for grade in grades:
            grade.uuid = uuid.uuid4()
            grade.save()
        '''