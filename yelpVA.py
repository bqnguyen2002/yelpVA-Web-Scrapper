from bs4 import BeautifulSoup
import requests
from datetime import datetime

urlFairfax = 'https://www.yelp.com/search?cflt=restaurants&find_loc=Fairfax%2C+VA'
pageFairfax = requests.get(urlFairfax)
soup = BeautifulSoup(pageFairfax.text, 'html.parser')
count = 1
textFairfax = 'Fairfax top 10 Restaurants: \n'
for link in soup.find_all('a', class_ = 'css-19v1rkv'):
    if(link.get('name') is not None):
        #print(str(count) + '. ' + link.get('name'))
        textFairfax += str(count) + '. ' + link.get('name') + '\n'
        count += 1

urlCentreville = 'https://www.yelp.com/search?cflt=restaurants&find_loc=Centreville%2C+VA'
pageCentreville = requests.get(urlCentreville)
soup = BeautifulSoup(pageCentreville.text, 'html.parser')
count = 1
textCentreville = 'Centreville top 10 Restaurants: \n'
for link in soup.find_all('a', class_ = 'css-19v1rkv'):
    if(link.get('name') is not None):
        #print(str(count) + '. ' + link.get('name'))
        textCentreville += str(count) + '. ' + link.get('name') + '\n'
        count += 1

urlVienna = 'https://www.yelp.com/search?cflt=restaurants&find_loc=Vienna%2C+VA'
pageVienna = requests.get(urlVienna)
soup = BeautifulSoup(pageVienna.text, 'html.parser')
count = 1
textVienna = 'Vienna top 10 Restaurants: \n'
for link in soup.find_all('a', class_ = 'css-19v1rkv'):
    if(link.get('name') is not None):
        #print(str(count) + '. ' + link.get('name'))
        textVienna += str(count) + '. ' + link.get('name') + '\n'
        count += 1   

urlAlexandria = 'https://www.yelp.com/search?cflt=restaurants&find_loc=Alexandria%2C+VA'
pageAlexandria = requests.get(urlAlexandria)
soup = BeautifulSoup(pageAlexandria.text, 'html.parser')
count = 1
textAlexandria = 'Alexandria top 10 Restaurants: \n'
for link in soup.find_all('a', class_ = 'css-19v1rkv'):
    if(link.get('name') is not None):
        #print(str(count) + '. ' + link.get('name'))
        textAlexandria += str(count) + '. ' + link.get('name') + '\n'
        count += 1 

urlHerndon = 'https://www.yelp.com/search?cflt=restaurants&find_loc=Herndon%2C+VA'
pageHerndon = requests.get(urlHerndon)
soup = BeautifulSoup(pageHerndon.text, 'html.parser')
count = 1
textHerndon = 'Herndon top 10 Restaurants: \n'
for link in soup.find_all('a', class_ = 'css-19v1rkv'):
    if(link.get('name') is not None):
        #print(str(count) + '. ' + link.get('name'))
        textHerndon += str(count) + '. ' + link.get('name') + '\n'
        count += 1 

urlManassas = 'https://www.yelp.com/search?cflt=restaurants&find_loc=Manassas%2C+VA'
pageManassas = requests.get(urlManassas)
soup = BeautifulSoup(pageManassas.text, 'html.parser')
count = 1
textManassas = 'Manassas top 10 Restaurants: \n'
for link in soup.find_all('a', class_ = 'css-19v1rkv'):
    if(link.get('name') is not None):
        #print(str(count) + '. ' + link.get('name'))
        textManassas += str(count) + '. ' + link.get('name') + '\n'
        count += 1

urlFallsChurch = 'https://www.yelp.com/search?cflt=restaurants&find_loc=Falls%20Church%2C+VA'
pageFallsChurch = requests.get(urlFallsChurch)
soup = BeautifulSoup(pageFallsChurch.text, 'html.parser')
count = 1
textFallsChurch = 'Falls Church top 10 Restaurants: \n'
for link in soup.find_all('a', class_ = 'css-19v1rkv'):
    if(link.get('name') is not None):
        #print(str(count) + '. ' + link.get('name'))
        textFallsChurch += str(count) + '. ' + link.get('name') + '\n'
        count += 1

#print('\n' + textFairfax + '\n' +textCentreville + '\n' + textVienna + '\n' + textAlexandria + '\n' + textHerndon + '\n' + textManassas + '\n' + textFallsChurch)

"""
import smtplib

email = "YOUR_EMAIL"
receiver_email = "RECEIVER_EMAIL"
subject = "Top 10 Restaurants in VA for " + datetime.now().strftime("%B")
message = ('\n' + textFairfax + '\n' +textCentreville + '\n' + textVienna + '\n' + textAlexandria + '\n' + textHerndon + '\n' + textManassas + '\n' + textFallsChurch)
text = f"Subject: {subject}\n\n{message}"
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(email, "hjth cxup zreo twgb")
server.sendmail(email, receiver_email, text.encode('utf8'))
print("Email has been sent to " + receiver_email)

"""
