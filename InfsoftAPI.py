import requests
import json


"""
Query Data from Infsoft API from a all devices:

https://api.infsoft.com/data/102450/current/SENSOR?operationId=5cc2be8d-a968-4897-b689-5346709dbc9d

"""

get_url = "https://api.infsoft.com/data/102450/current/SENSOR?operationId=5cc2be8d-a968-4897-b689-5346709dbc9d"
get_headers = {
    "content-type": "application/json",
    "Ocp-Apim-Subscription-Key": "XXX"
}

response = requests.get(get_url, headers=get_headers)

if response.status_code == 200:
    
    print(response)
    response_data = response.json()

    print(json.dumps(response_data, indent=4, ensure_ascii=False))

else:
    print("Error:", response.status_code, response.text)