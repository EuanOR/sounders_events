import requests
import json

def scrape_seatgeek():
    with open ('credentials/seatgeek.txt') as t:
        api_key = t.readline().rstrip()

    api_url = 'https://api.seatgeek.com/2/events?q=sounders&client_id={}'.format(api_key)
    r = requests.get(api_url)
    response_data = json.loads(r.text)

    event_data = dict()
    sounders_events = []

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
            
            event_data['home'] = True
            if 'seattle' not in event_data['city'].lower():
                event_data['home'] = False

            sounders_events.append(event_data)
        except:
            return (False, {}, "Error while parsing Seatgeek API")
    
    return (True, sounders_events, "Successfully pulled data from Seatgeek")
