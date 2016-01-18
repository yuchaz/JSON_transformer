import json

filename = []

with open('./filename.txt') as inputData:
	filename = inputData.read().split("\n")
	# filename.remove("")
	# print(filename)


	
for idx in range(1,4):
	with open('./load.json') as jsonObj:
		objJSON = json.load(jsonObj)
		for name in filename:
			nwname = "http://psyop.hopto.org/yuchazImg/"+str(idx)+"/"+name
			print(nwname)
			objJSON['data'].append({"src": nwname, "details": "nothing to tell"})
		objJSON['current_page'] = idx
		with open('./output/'+str(idx)+'.json', 'w+') as outputFile:
			json.dump(objJSON, outputFile)