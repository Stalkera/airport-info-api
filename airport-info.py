import requests
import json
import sqlite3

airport = input('შეიყვანეთ აეროპორტის "IATA" კოდი(მაგ:AAA, AAB, AAC და ა.შ.): ')

url = "https://airport-info.p.rapidapi.com/airport"
headers = {
    'x-rapidapi-key': "29b390b287mshc1b4a86da43d4d3p194956jsn21c029a1ce38",
    'x-rapidapi-host': "airport-info.p.rapidapi.com"
}

y = {"iata": airport}

r = requests.request("GET", url, headers=headers, params=y)

res = r.json()

with open('airport-info.json', 'w') as f:
    json.dump(res, f, indent=4)

print(f'აეროპორტის ID: {res["id"]}')
print(f'"ICAO" კოდი: {res["icao"]}')
print(f'სახელი: {res["name"]}')
print(f'ლოკაცია: {res["location"]}')
print(f'ქვეყანა: {res["country"]}')
print(f'ტელეფონის ნომერი: {res["phone"]}')
print(f'განედი: {res["latitude"]}')
print(f'გრძედი: {res["longitude"]}')
print(f'ვებსაიტი: {res["website"]}')

for each in res:
    list = []
    id = res["id"]
    ICAO = res["icao"]
    name = res["name"]
    street = res["location"]
    country = res["country"]
    phone = res["phone"]
    latitude = res["latitude"]
    longitude = res["longitude"]
    website = res["website"]
    row = (id, ICAO, name, street, country, phone, latitude, longitude, website)
    list.append(row)

conn = sqlite3.connect('airport-info.sqlite')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS airport
                    (id number(50),
                    icao VARCHAR(50),
                    name varchar(50),
                    street varchar(50),
                    country varchar(50),
                    phone varchar(50),
                    latitude float(50),
                    longitude float(50),
                    website varchar(50))''')
cursor.executemany("INSERT INTO airport(id, icao, name, street, country, phone, latitude, longitude, website) VALUES "
                   "(?, ?, ?, ?, ?, ?, ?, ?, ?)", list)
conn.commit()