import requests

status='available'

res = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}\
",headers = {'accept': 'application/json'})
print(res.status_code)
print(res.text)
print(res.json())

res2 = requests.post(f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}\
",headers = {'accept': 'application/json'},data = {'key1': 'value1', 'key2': 'value2'})

print(res2.status_code)
print(res2.text)
print(res2.json())

res3 = requests.delete(f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}\
",headers = {'accept': 'application/json'},data = {'key1': 'value1', 'key2': 'value2'} )

print(res3.status_code)
print(res3.text)
print(res3.json())

res4 = requests.put(f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}\
",headers = {'accept': 'application/json'},data = {'key1': 'value1', 'key2': 'value2'})

print(res4.status_code)
print(res4.text)
print(res4.json())

