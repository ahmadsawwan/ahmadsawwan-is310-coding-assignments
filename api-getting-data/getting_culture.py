from dotenv import load_dotenv
import os
import base64
from requests import post,get
import json
from pyeuropeana.apis import search
import requests




load_dotenv()
europeana_api_key = os.getenv("EUROPEANA_API_KEY")
client_id=os.getenv("CLIENT_ID")
client_secret=os.getenv("CLIENT_SECRET")


def get_token():
    auth_string=client_id+ ":" + client_secret
    auth_bytes=auth_string.encode("utf-8")
    auth_base64=str(base64.b64encode(auth_bytes),"utf-8")

    url="https://accounts.spotify.com/api/token"
    headers={
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data={"grant_type": "client_credentials"}
    result=post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token=json_result["access_token"]
    return token
def get_auth_header(token):
    return{"Authorization":"Bearer " + token}

def search_artist(token,artist_name):
    url="https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"
    query_url=url+query
    result=get(query_url,headers=headers)
    json_result=json.loads(result.content)["artists"]["items"]
    if len (json_result)==0:
        print("artist does not exist")
        return None
    return json_result[0]

def search_europeana(keyword):
    url = "https://www.europeana.eu/api/v2/search.json"
    params = {
        "query": keyword,
        "wskey": europeana_api_key,
        "rows": 1  # Limit to 1 result for simplicity
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

token = get_token()
artist_result = search_artist(token, "Juice")
if artist_result:
    print(f"Artist Name: {artist_result['name']}")

europeana_result = search_europeana("Juice")
if europeana_result:
    print(json.dumps(europeana_result, indent=4))



data_to_store = {
    "spotify_artist": artist_result,
    "europeana_item": europeana_result
}



filename = os.path.join("api-getting-data", "data_spotify_europeana.json")
with open(filename, 'w', encoding='utf-8') as json_file:
    json.dump(data_to_store, json_file, ensure_ascii=False, indent=4)
    
