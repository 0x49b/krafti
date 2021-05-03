from datetime import datetime

import pytz
import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand

from counter.models import Visits


class Command(BaseCommand):
    help = "Get journal Entries for Kraftreaktor Website"

    def handle(self, *args, **options):
        url = "https://www.boulderado.de/boulderadoweb/gym-clientcounter/index.php?mode=get&token=eyJhbGciOiJIUzI1NiIsICJ0eXAiOiJKV1QifQ.eyJjdXN0b21lciI6IktyYWZ0cmVha3RvckNIMjkifQ._ITvV6AXPN4jkEUJssq-ejUSs7yGdLY0HpTUQRJLHoE&ampel=0"
        res = requests.get(url, allow_redirects=True)
        soup = BeautifulSoup(res.text, 'html.parser')

        act_counter_elem = soup.find('div', {'class': 'actcounter'})
        free_counter_elem = soup.find('div', {'class': 'freecounter'})
        Visits(
            current_loggedin=act_counter_elem['data-value'],
            current_free=free_counter_elem['data-value'],
            added=datetime.utcnow().replace(tzinfo=pytz.timezone("Europe/Zurich"))
        ).save()
