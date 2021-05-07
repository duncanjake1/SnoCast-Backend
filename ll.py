# to run this in the django shell type th eline below in the command line
# python manage.py shell < db.py

import webbrowser
import requests
from bs4 import BeautifulSoup


# create dictionary and list

accidents = {}
emptykeylist = []



# define which accident webpages to run

x = 8

for j in range(x):

    # define URL of webpage to scrape
    URL =  'https://avalanche.state.co.us/caic/acc/acc_report.php?acc_id=' + str(j+1) + '&accfm=inv'

    # create soup object with webpage
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    # use element select() method of soup object to get header text
    elems = soup.select('h1')

    # turn soup element to text string
    text = elems[0].getText()

    # split text by dash
    ts = text.split('-')

    # create list with date, state, and location strings
    tss = []

    for i in range(len(ts)):
        tss.append(ts[i].strip(' '))

    # create dictionary and add webpage data for x iteration

    accidents[j+1] = tss



# create list of keys 

for key in accidents:
    if len(accidents.get(key)) < 3:
        emptykeylist.append(key)

for key in emptykeylist:
    accidents.pop(key)



# get lat and long
 
www.google.com/maps/dir/Lime+Creek+south+of+Edwards+Colorado




# add data to django sql database

from django.utils import timezone
from podcast_data.models import Avalanche_Accident

for key in accidents:

    a = Avalanche_Accident(Avalanche_Number = key, Name = accidents[key][2], Date = accidents[key][0], State = accidents[key][1], pub_date = timezone.now())

    a.save()

