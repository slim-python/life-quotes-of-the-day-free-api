import requests
import sys
from bs4 import BeautifulSoup
import json

url = "https://www.brainyquote.com/topics/life-quotes"

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

quotes = soup.find_all(class_="clearfix")

authors = soup.find_all('div' , {'style' : 'text-align:left'})

life_quotes = {}

for quote,author in zip(quotes, authors):
    numbering = str(quotes.index(quote))
    scrapped_quote = quote.find('a').contents[0]
    life_quotes[numbering] = scrapped_quote
    


json_object = json.dumps(life_quotes, sort_keys=True) 

json_object = json.loads(json_object) #this is the scrapped quotes in json


# ##########################################################
# #flask stuff
# ##########################################################

import flask
from os import environ
import gunicorn
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True



# A route to return all of the available entries in our catalog.
@app.route('/', methods=['GET'])
def api_all():
         return jsonify(json_object)
app.run(host='0.0.0.0', process.env.PORT || 5000, debug=True)
