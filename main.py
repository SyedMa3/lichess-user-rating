import requests
import csv
from collections import namedtuple 

file = 'players.csv'
players = dict()

with open('players.csv', mode='r') as infile:
    for r in infile:
        r = r.strip()
        row = r.split(',')
        if 'Name' in row[0]:
            continue
        players[row[0]] = row[1]


modes = ['bullet', 'blitz', 'rapid', 'classical']


with open('players_out.csv', mode='w') as csvfile:
    csvwriter = csv.writer(csvfile)
    fields = ['Name of the PLayer', 'Username', 'Bullet Rating', 'Blitz Rating','Rapid Rating', 'Classical Rating']
    csvwriter.writerow(fields)
    for name, username in players.items():
        response = requests.get(f'https://lichess.org/api/user/{username}')
        json_response = response.json()
        
        row_output = [name,username]

        for mode in modes:
            row_output.append(json_response['perfs'][mode]['rating'])

        csvwriter.writerow(row_output)
        


