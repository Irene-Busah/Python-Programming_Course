import json

inputs = '''
[
    {
    "id": "001",
    "name": "Irene",
    "contact": "+233 549185709"
    },
    {
    "id": "002",
    "name": "Harriet",
    "contact": "+250 784857890"
    }
]

'''
files = ["Glenn", "Sally", "Jen"]
json_parse = json.dumps(files)
print(json_parse)


# file = json.loads(inputs)
# print("count: {}".format(len(inputs)))
# for item in file:
#     print("contact: {}".format(item['contact']))

