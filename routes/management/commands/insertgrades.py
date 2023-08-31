import logging
from datetime import datetime
from django.db.models import Q

import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand

from routes.models import Route, RouteArchive, GradeScale, Category

logger = logging.getLogger('root')


class Command(BaseCommand):
    help = "Insert Grades"

    def handle(self, *args, **options):
        grades = [
            ("3–4", "1", "M", "1", "I", "I", "1–2", "1–2", "1", "1", "I", "I"),
            ("5", "", "", "1", "", "", "3–4", "3–4", "", "", "I sup", ""),
            ("5.1", "2", "", "2", "II", "II", "5–6", "5–6", "2", "2", "II", "II"),
            ("5.2", "", "D", "2", "", "", "7", "7", "", "", "II sup", ""),
            ("5.3", "3", "", "3", "III", "III", "8–9", "8–9", "3", "3", "", "III"),
            ("5.4", "", "VD", "4a", "IV", "IV", "10", "10", "", "", "III", "IV"),
            ("5.5", "4a", "S", "4b", "IV+/V-", "V", "11–12", "11–12", "4", "4", "III sup", ""),
            ("5.6", "4b", "HS", "4c", "V", "VI", "13", "13", "", "", "IV", "IV+"),
            ("5.7", "4c", "VS", "5a", "V+", "", "14–15", "14–15", "5-", "5-", "", "V-"),
            ("5.7", "", "", "5a+", "", "", "", "", "", "", "", ""),
            ("5.8", "", "HVS", "5b", "VI-", "VIIa", "16", "16", "5", "5", "IV sup", "V"),
            ("5.8", "", "", "5b+", "", "", "", "", "", "", "", ""),
            ("5.9", "5a", "", "5c", "VI", "VIIb", "17", "17–18", "5+", "5+", "V", "V+"),
            ("5.9", "", "", "5c+", "", "", "", "", "", "", "", ""),
            ("5.10a", "", "E1", "6a", "VI+", "VIIc", "18", "19", "", "6-", "VI", "VI"),
            ("5.10b", "5b", "", "6a+", "VII-", "", "19", "20", "6-", "", "", "VI+"),
            ("5.10c", "", "E2", "6b", "VII", "VIIIa", "20", "21", "6", "6", "VI sup", "VI.1"),
            ("5.10d", "5c", "", "6b+", "VII+", "VIIIb", "", "22", "", "6+", "", "VI.1+"),
            ("5.11a", "", "E3", "6c", "", "VIIIc", "21", "", "6+", "7-", "7a", "VI.2"),
            ("5.11b", "", "", "6c+", "VIII-", "", "22", "23", "7-", "7", "7b", ""),
            ("5.11c", "6a", "E4", "6c+", "", "IXa", "23", "24", "7", "", "7c", "VI.2+"),
            ("5.11d", "", "", "7a", "VIII", "IXb", "", "25", "", "7+", "", "VI.3"),
            ("5.12a", "", "E5", "7a+", "VIII+", "IXc", "24", "26", "7+", "7+/8-", "8a", "VI.3+"),
            ("5.12b", "", "", "7b", "", "", "25", "27", "8-", "8-", "8b", "VI.4"),
            ("5.12c", "6b", "E6", "7b+", "IX-", "Xa", "26", "28", "8", "8", "8c", ""),
            ("5.12d", "", "", "7c", "IX", "Xb", "27", "29", "8+", "8/8+", "9a", "VI.4+"),
            ("5.13a", "", "E7", "7c+", "IX+", "Xc", "28", "30", "9-", "8+", "9b", "VI.5"),
            ("5.13b", "6c", "", "8a", "", "", "29", "31", "9", "9-", "9c", "VI.5+"),
            ("5.13c", "", "E8", "8a+", "X-", "XIa", "30", "32", "9+", "9-/9", "10a", ""),
            ("5.13d", "", "E9", "8b", "X", "XIb", "31", "33", "10-", "9", "10b", "VI.6"),
            ("5.14a", "7a", "E10", "8b+", "X+", "XIc", "32", "34", "10", "9/9+", "10c", "VI.6+"),
            ("5.14b", "", "", "8c", "", "", "33", "35", "10+", "9+", "11a", "VI.7"),
            ("5.14c", "7b", "E11", "8c+", "XI-", "XIIa", "34", "36", "11-", "9+/10-", "11b", "VI.7+"),
            ("5.14d", "", "", "9a", "XI", "XIIb", "35", "37", "11", "", "11c", "VI.8"),
            ("5.15a", "", "", "9a+", "XI+", "", "36", "38", "", "", "12a", ""),
            ("5.15b", "", "", "9b", "", "", "37", "39", "", "", "12b", ""),
            ("5.15c", "", "", "9b+", "XII-", "", "38", "40", "", "", "12c", ""),
            ("5.15d", "", "", "9c", "XII", "", "39", "", "", "", "13a", ""),
            ("5.15d", "", "", "9c+", "", "", "", "", "", "", "", ""),
        ]

        GradeScale.objects.all().delete()

        for grade in grades:
            print("Add new Grade {french}".format(french=grade[3]))

            new_grade = GradeScale()
            new_grade.yds = grade[0]
            new_grade.british_tech = grade[1]
            new_grade.british_adj = grade[2]
            new_grade.french = grade[3]
            new_grade.uiaa = grade[4]
            new_grade.saxon = grade[5]
            new_grade.australia = grade[6]
            new_grade.scandinavia = grade[8]
            new_grade.brasil = grade[9]

            new_grade.save()
