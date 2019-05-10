import json

a = '{"a": 1, "b": true}'
print(json.loads(a))

b = {
    'a': 1,
    'b': True
}
print(json.dumps(b))
