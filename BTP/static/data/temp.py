import json

input_file = open ('degree.json')
json_array = json.load(input_file)

print(json_array)