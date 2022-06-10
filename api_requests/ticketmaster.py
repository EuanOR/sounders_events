import requests
import json

def scrape_ticketmaster():
    with open ('credentials/ticketmaster.txt') as t:
        api_key = t.readline().rstrip()

    api_url = 'https://app.ticketmaster.com/discovery/v2/events.json?keyword=sounders&apikey={}'.format(api_key)
    r = requests.get(api_url)
    response_data = json.loads(r.text)

    event_data = dict()
    sounders_events = []

    for event in response_data['_embedded']['events']:
        try:
            # try:
            #     event_data.pop('_id')
            # except:
            #     pass
            
            venue = event['_embedded']['venues'][0]
            
            
            event_data['name'] = event['name']
            event_data['date'] = event['dates']['start']['dateTime']
            event_data['venue'] = venue['name']
            event_data['address'] = venue['address']['line1']
            event_data['city'] = venue['city']['name']
            event_data['state'] = venue['state']['stateCode']
            event_data['zip'] = venue['postalCode']
            event_data['country'] = venue['country']['countryCode']

            event_data['home'] = True
            if 'seattle' not in event_data['city'].lower():
                event_data['home'] = False

            sounders_events.append(event_data)
        except:
            return (False, {}, "Error while parsing Seatgeek API")
    
    return (True, sounders_events, "Successfully pulled data from Ticketmaster")