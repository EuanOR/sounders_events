from calendar import c
from datetime import datetime
import psycopg2
import json

def insert_event(event):
    try:
        with open('db/credentials.txt') as cs:
            connection_string = cs.readline().rstrip()
            print(connection_string)
            connection_string = json.loads(connection_string)
        connection = psycopg2.connect(user=connection_string['user'],
                                        password=connection_string['password'],
                                        host=connection_string['host'],
                                        port=connection_string['port'],
                                        database=connection_string['database'])

        print(connection)

        cursor = connection.cursor()

        # Update single record now
        #sql_insert_query = """INSERT INTO events
        #                     VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %f, %f);
        #                     """
        # cursor.execute(sql_insert_query, 
        #                 (
        #                     event['id'], 
        #                     event['name'], 
        #                     datetime.now(), 
        #                     event['venue'],
        #                     event['address'], 
        #                     event['city'], 
        #                     event['state'],
        #                     event['zip'],
        #                     event['country'],
        #                     event['latitude'],
        #                     event['longitude']
        #                 )
        #             )
        # connection.commit() 
        
        # sql_insert_query = """INSERT INTO events (id, name, venue, address, city, state, zip, country, latitude, longitude)
        #                     VALUES({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9});
        #                     """.format(
        #                     event['id'], 
        #                     event['name'], 
        #                     event['venue'],
        #                     event['address'], 
        #                     event['city'], 
        #                     event['state'],
        #                     event['zip'],
        #                     event['country'],
        #                     event['latitude'],
        #                     event['longitude']
        #                 )
        # print(sql_insert_query)
        # cursor.execute(sql_insert_query)
        # connection.commit()
        print(cursor)
        sql_insert_query = """INSERT INTO events (id, name)
                            VALUES({0}, {1});
                            """.format(
                            event['id'], 
                            event['name'], 
                        )
        print(sql_insert_query)
        cursor.execute(sql_insert_query)
        connection.commit()


    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")