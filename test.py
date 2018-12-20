import utils
import json

print([json.loads(utils.getJsonFromFile(x)) for x in utils.AVAILABE_SHOWS])

show = json.dump(utils.getJsonFromFile('7'))
print(show)
print(show['id'])
print(show['rating']['average'])
print(show['name'])
