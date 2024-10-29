Add your tokens to a .env file save that file.

import the following into your script.

from dotenv import load_dotenv
import os
import base64
from requests import post,get
import json
from pyeuropeana.apis import search
import requests

This script will search spotify for keyword "Juice" and then type the most popular search down, which turned out to be Juice WRLD. It will print out followers, genre, popularity and such. 

Then it will search Europena for the same word, and print out the results from that. 


All this saved into a JSON file. 