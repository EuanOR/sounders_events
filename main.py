from api_requests import seatgeek
from api_requests import ticketmaster
from sounders_write import push_data_to_api
import time

INTERMISSION = 86400

while 1:
    print("Beginning sounders event refresh....")
    sounders_events = []

    seatgeek_data = seatgeek.scrape_seatgeek()
    if not seatgeek_data:
        print("Error while pulling data from Seatgeek")

    ticketmaster_data = ticketmaster.scrape_ticketmaster()

    if not ticketmaster_data:

        print("Error while pulling data from Ticketmaster")
    try:
        sounders_events = seatgeek_data + ticketmaster_data
    except:
        print("Failed to combine data sources")
    api_push_success = push_data_to_api(sounders_events)

    if api_push_success[0]:
        print(api_push_success[2])
    else:
        print("Failed to push event {}".format(api_push_success[1]))
    
    time.sleep(INTERMISSION)
    