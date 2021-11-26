#data from https://www.worldometers.info
import requests
import urllib.request
from bs4 import BeautifulSoup

print("\nCorona Updates\n")

while True:
  print("If the country name has multiple words, add a '-' between them")
  country=input("Enter the name of the country: ")

  url="https://www.worldometers.info/coronavirus/country/"+country

  response = requests.get(url)
  soup = BeautifulSoup(response.text, "html.parser")
  html_line=str(soup.findAll("title"))

  html_line = html_line.replace(',', '')
  int_list = [int(s) for s in html_line.split() if s.isdigit()]

  finish = "The total cases in",country,"is",int_list[0],"and the total number of deaths is", int_list[1]

  finish = str(finish).replace('(', '')
  finish = str(finish).replace(')', '')
  finish = str(finish).replace("'", '')

  print("\n",finish)