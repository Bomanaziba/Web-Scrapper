
import requests
from bs4 import BeautifulSoup

class Scrapper:

    def __PrayerScrap(self, url):

        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find(id = 'x-content-band-1')
        prayer_elems = results.find_all('div',  class_ = 'x-accordion-group')
        for prayer_elem in prayer_elems:
            prayer_title = prayer_elem.find('a', class_= 'x-accordion-toggle collapsed')
            prayer_content = prayer_elem.find('div', class_= 'x-accordion-inner')
            
            if None in (prayer_title, prayer_content):
                print(prayer_title)
                print(prayer_content)
            print()

            result = Scrapper()
            
            print(prayer_title.text.strip())
            end = result.__PrayerSplit(prayer_content.text.strip())
            print(end[0])
            print(end[1] + ":" + end[2])
            print()


    def __PrayerSplit(self, paryString):
        return paryString.split(':',4)

    
    def CovenantHour(self, mainUrl):

        page = requests.get(mainUrl)

        soup = BeautifulSoup(page.content, 'html.parser')

        results = soup.find(id = 'top')

        covenantHourSites = results.find_all('article')

        for covenantHourSite in covenantHourSites:
            title = covenantHourSite.find('h2', class_ = 'entry-title')
            prayerlink = covenantHourSite.find('a')['href']
            if None in (title, prayerlink):
                print(title)
                print(prayerlink)
            
            print("============================================================")
            print(title.text.strip())
            result.__PrayerScrap(prayerlink)

result = Scrapper()

URL = 'https://www.winnerschapelny.org/tag/covenant-hour-of-prayer/'

result.CovenantHour(URL)
  
