import utils
import json

#print([json.loads(utils.getJsonFromFile(x)) for x in utils.AVAILABE_SHOWS])


show = json.loads(utils.getJsonFromFile('7'))

#print(show)
#print(show['id'])
print(show['name'])
print(show['_embedded']['episodes'])