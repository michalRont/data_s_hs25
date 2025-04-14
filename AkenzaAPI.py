import requests
import json


"""
Akenza API Documentation: https://docs.api.akenza.io/

Query Data from Akenza API from a specific device:

https://api.akenza.io/v3/devices/{AkenzaDeviceID}/query?topic={topic}&limit=1&skip=0

AkenzaDeviceID (required): the Akenza device ID of the device you want to query
limit (optional): default 8000
skip (optional): default 0
topic (optional): default "default", use topic "*" for any topics
timestamp (optional): allows restricting the date range

"""

get_url = "https://api.akenza.io/v3/devices/02e193fe64b3fbe8/query?topic=default&limit=1&skip=0"
get_headers = {
    "content-type": "application/json",
    "x-api-key": "XXX" 
}

response = requests.get(get_url, headers=get_headers)

if response.status_code == 200:
    
    print(response)
    response_data = response.json()

    print(json.dumps(response_data, indent=4, ensure_ascii=False))

else:
    print("Error:", response.status_code, response.text)