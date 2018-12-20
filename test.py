import utils
import json

#print([json.loads(utils.getJsonFromFile(x)) for x in utils.AVAILABE_SHOWS])


show = json.loads(utils.getJsonFromFile('7'))

#print(show)
#print(show['id'])
print(show['_embedded']['episodes'][0]['id'] )
print(show['_embedded']['episodes'][0]['id'] == 189)

episodeSelected = [x for x in show['_embedded']['episodes'] if x['id'] == 189]
print(episodeSelected)

#episodeSelected = [showSelected['_embedded']['episodes'][x] for x in showSelected['_embedded']['episodes'] if x['id'] == int(episodeid)]
