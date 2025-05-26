import requests
import json
import random
import time

# Webhook endpoint (same as your original)
url = 'https://tandem.autodesk.com/api/v1/timeseries/models/urn:adsk.dtm:htcEYQmiSFech82BIQBFLg/webhooks/generic'



# Authorization headers – consider using environment variables in production
headers = {
    'Authorization': 'Basic Ok1Dbmp6Zl9HVGI2RFRoVTFDTXpDSnc=',
    'Content-Type': 'application/json'
}

# Component stream ID for cooling/heating air condition in airport waiting room
STREAM_ID = "AQAAADUHyv8GxkOJhbGQb-1asAUAAAAA"

# Generate fake temperature and humidity data
def create_environmental_data():
    return {
        "id": STREAM_ID,
        "temperatur": round(random.uniform(18.0, 26.0), 1),      # typical indoor AC range
        "feuchtigkeit": round(random.uniform(30.0, 60.0), 1),    # relative humidity %
        "timestamp": int(time.time() * 1000)
    }

# Send the data
def send_environmental_data():
    payload = [create_environmental_data()]  # payload must be a list
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.ok:
        print('✅ Data sent successfully!')
    else:
        print(f'❌ Failed to send data. Status Code: {response.status_code}, Response: {response.text}')

if __name__ == "__main__":
    iterations = 6  # Send data every 10 seconds for 1 minute
    for i in range(iterations):
        print(f"🌡️ Sending environmental data... ({i+1}/{iterations})")
        send_environmental_data()
        if i < iterations - 1:
            time.sleep(10)
    print("🎉 Finished sending environmental data!")