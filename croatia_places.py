# -*- coding: utf-8 -*-
"""Croatia places.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_L0FIUwuWsexbhJx61yl-KGaihoI27Ir
"""

# Needed imports

import pandas
import geopy
from geopy.geocoders import Nominatim
import requests
from bs4 import BeautifulSoup
import numpy as np
from time import sleep

# Croatian alphabet

alphabet = ["A", "B", "C", "Č", "Ć", "D", "DŽ", "Đ", "E", "F", "G", "H", "I", "J", "K", "L", "LJ", "M", "N", "NJ", "O", "P", "R", "S", "Š", "T", "U", "V", "Z", "Ž"]

# Code for getting all names of Croatian settlements

# 6790 is the total number of settlements according to wikipedia
places = np.zeros((6790, 4), dtype=object)
index = 0
for letter in alphabet:
  # For each letter in alphabet sending a request to fetch the content from the page
  # And then parsing the content to get all the names
  # And saving them into places variable. Format Places: ['Settlement_name', 'County_name', 0, 0]
  result = requests.get("https://hr.wikipedia.org/wiki/Dodatak:Abecedni_popis_naselja_u_Republici_Hrvatskoj/{}".format(letter))
  src = result.content
  soup = BeautifulSoup(src, 'lxml')
  table = soup.find_all("a")

  flag = 0
  count = 1
  for i, row in enumerate(table):
    if "Dodatak:Popis gradova" in row.text:
      flag = 1
      continue

    if "↑" in row.text or "uredi VE" in row.text or "http" in row.text:
      flag = 0

    if "[" in row.text:
      continue

    if flag == 1:
      if count == 1 or count == 4:
        places[index, 0] = table[i].text
        places[index, 1] = table[i+1].text
        index += 1
        count = 1

      count += 1

print(places)

print(places.shape)

# Variable for all places that are not going to be found
places_notfound = []

# Fetching longitudes and latitudes using the OpenStreetMap API
# There can only be one request per second so that's why is there "sleep(1.2)" function

nom = Nominatim(user_agent="croatiaplaces2")

# Handling all the cases if request result is "null"
for i in range(places.shape[0]):
  n = nom.geocode(places[i, 0] + ", " + places[i, 1] + ", Croatia")
  if n == None:
    sleep(1.2)
    n = nom.geocode(places[i, 0] + ", Croatia")
    if n == None:
      places_notfound.append([places[i, 0], places[i, 1]])
      sleep(1.2)
      continue
  
  places[i, 2] = n.latitude
  places[i, 3] = n.longitude
  print("Broj: {}, Selo: {}".format(i, places[i, 0]))
  sleep(1.2)

print(places[0:50])

# Mounting on google drive

from google.colab import drive
drive.mount('/content/drive')

# Saving the result on google drive in format: "Settlement_name,Settlement_count,Lat,Lon"

np.savetxt("/content/drive/My Drive/Croatia Places/placesUpdate.txt", places, delimiter=",", fmt="%s")

notFound = np.array(places_notfound)
print(notFound.shape)

np.savetxt("/content/drive/My Drive/Croatia Places/placesNotFoundUpdate.txt", notFound, delimiter=",", fmt="%s")