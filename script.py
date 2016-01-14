import json

filename = []

with open('./filename.txt') as inputData:
	filename = inputData.read().split("\n")
	# filename.remove("")
	# print(filename)

with open('./load.json') as jsonObj:
	objJSON = json.load(jsonObj)
	for name in filename:
		objJSON['data'].append({"src": name, "details": "nothing to tell"})
	with open('./output/load.json', 'w+') as outputFile:
		json.dump(objJSON, outputFile)