# to run this in the django shell type the line below in the command line
# python manage.py shell < db.py


import webbrowser
import requests
import time
from bs4 import BeautifulSoup


# create dictionary and list

accidents = {}
emptykeylist = []



# define which accident webpages to run

x = 794

for j in range(x):

    time.sleep(2)

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



# remove empty keys (for empty accident webpages)

for key in accidents:
    if len(accidents.get(key)) < 3:
        emptykeylist.append(key)

for key in emptykeylist:
    accidents.pop(key)



# get lat and long


from selenium import webdriver
driver = webdriver.Firefox()
print (driver.current_url)

for key in accidents:

    # clean up name text
    name = str(accidents[key][2])

    namesplit = name.split(' ')

    strippedwordlist = []

    # get rid of this
    for word in namesplit:
        strippedwordlist.append(word)

    striplist = ['/', ',', ' ']

    for i in range(len(namesplit)):
        for character in striplist:
            text = strippedwordlist[i]
            strippedwordlist[i] = text.strip(character)

    # remove words that confuse google/maps

    removewordlist = ['Near', 'near', 'OB', 'in', 'bounds', 'off', 'trail', 'but', 'of', 'north', 'east', 'south', 'west', 'Town', 'of', 'outside', 'northern', 'southern', 'eastern', 'western', 'Drainage', 'drainage', 'The', 'Ballroom']

    for word in removewordlist:
        if word in strippedwordlist:
            strippedwordlist.remove(word)
        

    # create string of location description with list of remaining words
    namestring = ''

    for word in strippedwordlist:
        namestring += str(word) + '+'


    ###  Scrape url from each webpage so lat/long can be extracted from url


    # define URL of webpage to scrape
    url =  'http://www.google.com/maps/search/' + str(namestring) + str(accidents[key][1])


    # Getting the webpage, creating a Response object.

    driver.get(url)

    # make sure page is fully loaded (probably a better way to do this)

    webaddresswithlatlong = driver.current_url

    while '@' not in webaddresswithlatlong:
        time.sleep(0.1)
        webaddresswithlatlong = driver.current_url



    urlsplitat = webaddresswithlatlong.split('@')

    urlsplitcomma = urlsplitat[1].split(',')

    lat = urlsplitcomma[0]

    long = urlsplitcomma[1]


    #keylistaddlat = accidents.get(key).append(lat)

    accidents.get(key).append(lat)

    #keylistaddlong = keylistaddlat.append(long)

    accidents.get(key).append(long)


    print(accidents[key])




# add data to django sql database

from django.utils import timezone
from podcast_data.models import Avalanche_Accident

for key in accidents:

    a = Avalanche_Accident(Avalanche_Number = key, Name = accidents[key][2], Date = accidents[key][0], State = accidents[key][1], Lat = accidents[key][3], Long = accidents[key][4], pub_date = timezone.now())

    a.save()

