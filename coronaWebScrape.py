#data from https://www.worldometers.info
import requests
from bs4 import BeautifulSoup
import csv


def scrape(country):
  country=str(country).replace(" ","-")

  with open('data.csv', newline='') as f:
      reader = csv.reader(f)
      data = list(reader)
      data = data[0]

  if country.lower() not in data:
    return None
  
  else:
    url="https://www.worldometers.info/coronavirus/country/"+country

    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, "html.parser")
    html_line=str(soup.findAll("title"))

    html_line = html_line.replace(',', '')
    int_list = [int(s) for s in html_line.split() if s.isdigit()]

    finish = "The total cases in",country.upper(),"is",int_list[0],"and the total number of deaths is", int_list[1]

    finish = str(finish).replace('(', '')
    finish = str(finish).replace(')', '')
    finish = str(finish).replace("'", '')

    return finish