import json

input_file = open ('degree.json')
json_array = json.load(input_file)

for item in json_array:
    print(item["name"])
    print(item["NER"])