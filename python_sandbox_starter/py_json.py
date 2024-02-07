# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary
import _json
import json

# sample json
userJSON = '{"name1":"ocen", "age": 30}'

# parse to dict
user = json.loads(userJSON)

print(user)
print(user['age'])