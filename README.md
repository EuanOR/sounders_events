## Prerequisites

node 16.x.x
npm 8.x.x
python 3.x.x
pip3 21.x.x
mongo 5.x.x

## Overview

This project is intended as a demo API to serve data on upcoming Seattle sounders games in the MLS. Data on these games have been pulled from seatgeek and ticketmasters Public APIs.

Data from these API's is scraped and parsed using Python. Data is pulled via http requests to the API's and then made uniform so the can be inserted into the underlying Mongo DB via the Sounders Games API.

Sounders Game API data is served via fastify running on NodeJS. Swagger is running on top of this to provide and UI to interact with the API in your browser.

## Authentication

You will need auth tokens to interact with the seatgeek and ticketmaster API's. These should be placed in a directory called credentials in the root sounders_games folder in files called seatgeek.txt and ticketmaster.txt respectively.  

## To run

1. Start the DB
```
$ mongod

```
2. Install required Python modules (this project uses 3 modules, 2 of them are in-built so we're only installing one module here).
From the root sounders_games directory.
```
$ pip3 install -r requirements.txt
```
3. From the root sounders_games directory. Navigate to the the src folder, install required npm modules and initialize the server
```
$ cd api/src

$ npm i

$ npm start

```
If successful you should see a message in the terminal saying..

```
MongoDB connected…
```

4. Run the python script that populates and updates the db. I have it set to update the db daily. The first time you run this it should populate the DB that the API interfaces with. From the main sounders_games directory

```
python3 main.py
```

5. Navigate to http://localhost:3000/swagger on your browser to view the API on your browser.
![Swagger UI](/screenshots/api_screenshot.png "Swagger UI") 