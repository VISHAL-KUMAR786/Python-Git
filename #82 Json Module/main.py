'''
JavaScript Object Notation 

Basic Rules of JSON

Keys are unique strings that cannot be null.

Values can be anything from a String, Number, Tuple, Boolean, list, or null.

A JSON is represented by a string which is enclosed within curly braces { } with key-value pairs which are separated by a colon ( : ), and pairs separated by a comma(, ).

-----------x-----------------x---------------x-------------x-----------------

load(): This method is used to load data from a JSON file into a python dictionary.

Loads( ): This method is used to load data from a JSON variable into a python dictionary.

dump(): This method is used to load data from the python dictionary to the JSON file.

dumps(): This method is used to load data from the python dictionary to the JSON variable.

JSON	            PYTHON
true     	        True
false   	        False
string     	        string
number	            number
array    	        list, tuple
object 	            dict
null      	        none

'''
import json
data = '{"name":"vishal","age":45,"hobby":"thinking"}'
parse_data = json.loads(data)

print(parse_data)
print(type(parse_data))


f = open(r'D:\IMP DOCUMENT\vishal\CWH python\#82 Json Module\my.json')
new_data = json.load(f)
print(new_data,type(new_data))


# ------x--------x-------------x-----------x--------------x------------

data  = {
    "name": "vishal kumar",
    "cars": ['bmw', 'audi a8', 'ferrari'],
    "fridge": ('roti', 540),
    "isbad": False,
    "sigma male" : None
}
new_data = json.dumps(data)
print(new_data) # string


dict1 ={
    "emp1": {
        "name": "Lisa",
        "designation": "programmer",
        "age": "34",
        "salary": "54000"
    },
    "emp2": {
        "name": "Elis",
        "designation": "Trainee",
        "age": "24",
        "salary": "40000"
    },
}
f = open(r'D:\IMP DOCUMENT\vishal\CWH python\#82 Json Module\my.json',"a")
json.dump(dict1,f)
f.close()