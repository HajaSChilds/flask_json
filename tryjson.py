import json

animal = {'type' : 'cat', 'age' : 12}
as_json = json.dumps(animal)

print(type(animal))
print(type(as_json))

as_object = json.loads(as_json)
print(type(as_object))