"""Scrapes Data from https://www.worldometers.info"""

import csv
import requests
from bs4 import BeautifulSoup


def scrape(country):
    """Scrape Function"""
    country = str(country).replace(" ", "-")

    with open('data.csv', newline='', encoding="utf-8") as f:
        reader = csv.reader(f)
        data = list(reader)
        data = data[0]

    if country.lower() not in data:
        return None

    url = "https://www.worldometers.info/coronavirus/country/"+country

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    html_line = soup.findAll("div", class_="maincounter-number")
    numbers = []
    for i in range(0, 2):
        num = ""
        for c in str(html_line[i]):
            if c.isdigit():
                num = num + c
        numbers.append(num)

    finish = "The total cases in", country.upper(
    ), "is", numbers[0], "and the total number of deaths is", numbers[1]
    finish = str(finish).replace('(', '')
    finish = str(finish).replace(')', '')
    finish = str(finish).replace("'", '')

    return finish


print(scrape("spain"))
