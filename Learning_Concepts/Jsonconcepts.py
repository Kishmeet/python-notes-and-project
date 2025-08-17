#Javascript Object Notation (JSON) is a lightweight data interchange format that is easy for humans to read and write, 
#and easy for machines to parse and generate. It is often used to transmit data between a server and a web application.
# The json module in Python provides methods to work with JSON data.
import json
data='''{"person": [{
    "name": "John",
    "age": 30,
    "city": "New York"},
    {
    "name": "Anna",
    "age": 22,
    "city": "London"
    }]
    }
    '''
a=json.loads(data) # The json.loads() function parses a JSON string and converts it into a Python dictionary.
print(a)
print(type(a))
print(a['person'][0]['name'])
print(a['person'][1]['city'])
for person in a['person']:
    del person['city']  # Removing the 'city' key from each person
str=json.dumps(a, indent=4)
print(str)
# The json.dumps() function converts a Python object into a JSON string.
# The indent parameter in dumps() is used to pretty-print the JSON string with specified indentation.

with open("data.json","r") as f:
    data = json.load(f)  
    print(data)
    for x in data.keys():
        print(x) 
    del data["Address"]['City'] 
with open("data2.json","w") as f:
    json.dump(data, f, indent=4)  