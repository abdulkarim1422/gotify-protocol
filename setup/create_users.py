import csv
import requests
import os

# Read the CSV file
with open('contacts.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    rows = list(csv_reader)

url = os.getenv('GOTIFY_URL') + '/user'

for row in rows:
    username = row[0]
    password = row[1]

    # Define the URL and payload
    payload = {'username': username, 'password': password}

    # Make the POST request
    response = requests.post(url, data=payload)

    # Print the response
    print(response.text)
