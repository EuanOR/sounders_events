import requests
import json
from mongo_calls import insert_events

with open ('tokens/ticketmaster.txt') as t:
    api_key = t.readline().rstrip()

api_url = 'https://app.ticketmaster.com/discovery/v2/events.json?keyword=sounders&apikey={}'.format(api_key)

r = requests.get(api_url)

response_data = json.loads(r.text)

event_data = dict()
for event in response_data['_embedded']['events']:
    try:

        try:
            event_data.pop('_id')
        except:
            pass
        
        venue = event['_embedded']['venues'][0]
        
        # uid = (event['name'], venue['name'], event['dates']['start']['dateTime'])
        # event['event_uid'] = hash(uid)
        
        event_data['name'] = event['name']
        event_data['date'] = event['dates']['start']['dateTime']
        event_data['venue'] = venue['name']
        event_data['address'] = venue['address']['line1']
        event_data['city'] = venue['city']['name']
        event_data['state'] = venue['state']['stateCode']
        event_data['zip'] = venue['postalCode']
        event_data['country'] = venue['country']['countryCode']
        # event_data['latitude'] = float(venue['location']['latitude'])
        # event_data['longitude'] = float(venue['location']['longitude'])
        insert_events(event_data)
    except:
        print("Error while parsing data from API")
