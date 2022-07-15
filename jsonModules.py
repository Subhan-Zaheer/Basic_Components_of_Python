"""
If you want to access dictionary with key value pair then you can do it with
json parsing.
In given example if we do data['f_name'] so it will give me an error message.
JSON.LOADS()
    Json.loads converts the string into python dictionary.
JSON.LOAD():
    It will give us file object. In short it will help us to read data from file.
JSON.DUMPS():
    json.dumps will give us Javascript compatible object. In short it will
    convert python code into javascript compatible code.

    (i). SORT KEYS is a parameter in json.dumps() its default value is FALSE
    but if it is TRUE, then it will sort the items in dict according to
    keys.
"""

import json

data = '{"f_name" : "Subhan", "l_name" : "Zaheer"}'
print(data)
print(type(data))

parsed = json.loads(data)
print(parsed)
print(parsed['f_name'])
print(type(parsed))

Subhan = {
    "Computer" : "Dell Work Station T5500 Xeon Processor",
    "isBad": False,
    "Languages" : ['C', 'C++', 'Python']
}
jscomp = json.dumps(Subhan, sort_keys=True)
print("\n", type(jscomp))
print("\n", jscomp)