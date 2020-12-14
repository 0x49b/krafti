from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup
from counter.models import Visits
from datetime import datetime
import pytz


class Command(BaseCommand):
    help = "Get opening Hours for Kraftreaktor"

    def handle(self, *args, **options):
        url = "https://kraftreaktor.ch/ueber/oeffnungszeiten/"
        res = requests.get(url, allow_redirects=True)
        soup = BeautifulSoup(res.text, 'html.parser')

        hours = soup.find('div', {'class': 'introduction_text'})

        ps = hours.find_all('p')

        for p in ps:

            day_text = ""
            time_text = ""

            if p.find('strong'):
                day = p.find('strong')
                day_text = day.text
                day.decompose()
                time_text = p.text

            print(day_text)
            print(time_text)
