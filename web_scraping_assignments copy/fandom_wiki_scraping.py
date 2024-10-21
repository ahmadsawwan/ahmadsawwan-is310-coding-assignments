import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import os

# Ensure the directory exists
os.makedirs('web_scraping_assignments', exist_ok=True)

# Load the HTML file
soup = BeautifulSoup(open("/Users/ahmadsawwan/Downloads/The 52 Best TV Shows on Hulu Right Now (October 2024) - TV Guide.html"), features="html.parser")

# Print the prettified HTML
print(soup.prettify())

# Find the element with id="h2"
top = soup.find(id="h2")
if top:
    top = top.find_next("em")
    if top:
        print(top.get_text())
    else:
        print("No <em> tag found after the element with id='h2'")
else:
    print("No element with id='h2' found")

# Find all <strong> tags and collect their text, excluding "Trailer"
titles = soup.find_all('strong')
title_list = []
for title in titles:
    text = title.get_text()
    if "Trailer" not in text:
        title_list.append(text)
# Save to JSON
with open('web_scraping_assignments/tv_shows.json', 'w', encoding='utf-8') as json_file:
    json.dump(title_list, json_file, ensure_ascii=False, indent=4)