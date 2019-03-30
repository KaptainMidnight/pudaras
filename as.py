import json

with open('data.json', 'r') as file:
    data = json.load(file)
    data['start'] = 5
    data['end'] = 1000
print(data['start'])