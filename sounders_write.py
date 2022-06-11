import requests
import json

api_url = "http://localhost:3000/soundersEvents"
headers = {"Content-Type":"application/json"}

def get_event_names():
    event_names = []
    try:
        r = requests.get(url=api_url, headers=headers)
        events = json.loads(r.text)
    except:
        return (-1, [], "Failed to pull data from API")
    if events:
        for event in events:
            event_names.append(event['name'])
        return (0, event_names, "Successfully pulled event names")
    else:
        return (1, [], "Empty DB: Proceed")

def push_data_to_api(events_data):
    event_names_result = get_event_names()
    if event_names_result[0] != -1:
        event_names = event_names_result[1]
        for event in events_data:
            if event['name'] not in event_names:                
                r = requests.post(url=api_url, headers=headers, json=event)
                if r.status_code != 200:
                    return (False, event, "Failed to write data to API")
                event_names.append(event['name'])
    
        return (True, {}, "Success")
    else:
        return (False, {}, "Failed to pull data from API")