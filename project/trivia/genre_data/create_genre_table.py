#!/usr/bin/python3
#
# Small script to show PostgreSQL and Pyscopg together
#

import psycopg2

try:
        conn = psycopg2.connect("dbname='trivia_db' user='bgilroy26' host='localhost' password='trivia'")
except:
        print("I am unable to connect to the database")

cur =  conn.cursor()

cursor.execute("CREATE TABLE genres (id serial PRIMARY KEY, name varchar);")
db.commit()
    
genres = []

with open('genres.txt','r') as f:
    for line in f:
        genres.append(strip(line))
        

cursor.execute

