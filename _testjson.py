#convert python -> JSON
import json
data = {"name": "Indhu", "age": 23, "city": "chennai"}

json_string = json.dumps(data) #python dic to json string
print(json_string)

#convert Json-> python
import json
json_data = '{"name": "indhu", "age": 23, "city": "chennai"}'

python_data = json.loads(json_data) #dict to string
print(python_data['name'])