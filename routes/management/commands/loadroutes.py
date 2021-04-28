from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup
import re


class Command(BaseCommand):
    help = "Get opening Hours for Kraftreaktor"

    def handle(self, *args, **options):
        url = "https://kraftreaktor.ch/angebot/routenliste/"
        res = requests.get(url, allow_redirects=True)
        soup = BeautifulSoup(res.text, 'html.parser')

        # routenliste_div = soup.find('div', {'class': 'detail_page page_routenliste slide_in'})
        # divs = routenliste_div.findAll('div')
        # php_array = divs[3].text.replace("&gt;", ">")
        #
        # arr = php_array.replace("\t", "").lstrip().split("\n")
        # p = re.compile('\W')
        #
        # for a in arr:
        #     if p.match(a):
        #         print("matched")

        tables = soup.findAll('table')
        # print(tables[0])

        i = 0
        for table in tables:
            trs = table.findAll('tr')
            trs = trs[1:]
            print(type(trs))

            print(trs[0])
            i = i + 1

        '''
        ps = hours.find_all('p')

        for p in ps:

            day_text = ""
            time_text = ""

            if p.find('strong'):
                day = p.find('strong')
                day_text = day.text
                day.decompose()
                time_text = p.text

        '''
