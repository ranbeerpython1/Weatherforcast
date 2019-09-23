import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=44.64196&lon=-124.04110#.XX57BygzbIU')
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)
week = soup.find(id='seven-day-forecast-body')
#print(week)
items = week.find_all(class_='tombstone-container')
#print(items[0])
#print(items[0].find(class_='period-name').get_text())
#print(items[0].find(class_='short-desc').get_text())
#print(items[0].find(class_='temp').get_text())
period_names = [item.find(class_='period-name').get_text() for item in items]
short_description = [item.find(class_='short-desc').get_text() for item in items]
tempretures = [item.find(class_='temp').get_text() for item in items]

#print(period_names)
#print(short_description)
#print(tempretures)
weather_stuff = pd.DataFrame(
    {'period': period_names,
     'short_description':short_description,
     'tempretures': tempretures
 })
print(weather_stuff)
weather_stuff.to_csv('weather.csv')