import requests
import json
from mongo_calls import insert_events

with open ('credentials/seatgeek.txt') as t:
    api_key = t.readline().rstrip()

api_url = 'https://api.seatgeek.com/2/events?q=sounders&client_id={}'.format(api_key)

r = requests.get(api_url)

response_data = json.loads(r.text)

event_data = dict()

for event in response_data['events']:
    try:
        event_data['name'] = event['title']
        event_data['date'] = event['datetime_local']
        venue = event['venue']
        event_data['venue'] = venue['name_v2']
        event_data['address'] = venue['address']
        event_data['city'] = venue['city']
        event_data['state'] = venue['state']
        event_data['zip'] = venue['postal_code']
        event_data['country'] = venue['country']
        # event_data['latitude'] = float(venue['location']['lat'])
        # event_data['longitude'] = float(venue['location']['lon'])

        insert_events(event)
    except:
        print("Error while parsing data from API")
