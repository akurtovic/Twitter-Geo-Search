'''
Twitter Geo Stream

Monitors Twitter stream for a search term saves new geotagged tweets
to a CSV logfile

@amirkurtovic
'''

from TwitterAPI import TwitterAPI
import codecs

# Create app on https://apps.twitter.com/ to get API keys
consumer_key = 
consumer_secret = 
access_token_key = 
access_token_secret = 

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

# What to search for
searchTerm = ""
r = api.request('statuses/filter', {'track':searchTerm})


try:
    logfile = codecs.open("log.csv", mode="a", encoding='utf-8')
except:
    f = open('log.csv','w+')
    f.close()
    logfile = codecs.open("log.csv", mode="a", encoding='utf-8')

for item in r:
	if (item['coordinates'] == None):
		pass
	else:
		cords = '' #string containing coordinates
		
		#loop through coordinates list and join cords into string
		for i in item['coordinates']['coordinates']:
			cords = unicode(cords + str(i) + ',')

		id_str = unicode(item['id_str'])
		text = unicode(item['text'])
		screen_name = unicode(item['user']['screen_name'])
		created_at = unicode(item['created_at'])
		entry = id_str + ',' + cords + text + ',' + screen_name + ',' + created_at + '\n'
		logfile.write(entry)