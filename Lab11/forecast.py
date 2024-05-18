#!/usr/bin/env python3

# Jordan Banks
#Palomar College CSIT 175
# Lab 11 ex.3 
# Reading Data from an API, 
# be careful with capitalization here.


from flask import Flask, render_template
import requests
import datetime

app = Flask(__name__)

def get_location(zip_code):
    url = f'http://api.zippopotam.us/us/{zip_code}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        city = data['places'][0]['place name']
        state = data['places'][0]['state']
        lat = data['places'][0]['latitude']
        lon = data['places'][0]['longitude']
        return city, state, lat, lon
    else:
        return None, None, None, None
