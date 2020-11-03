from os import chdir
import json

stringjson = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'

jsonToPython = json.loads(stringjson)
print(jsonToPython)

print(json.dumps(jsonToPython))