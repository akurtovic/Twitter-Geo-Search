'''
Twitter Geo Search

Runs a Twitter search on a list of search terms and saves new geotagged tweets
to a CSV logfile

@amirkurtovic
'''

from TwitterAPI import TwitterAPI
import codecs

# Create app on https://apps.twitter.com/ to get API keys
consumer_key = ""
consumer_secret = ""
access_token_key = ""
access_token_secret = ""

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

# word_list contains all of the words to be searched
word_list = [
	]


def search(words):
	
	for word in words:
		print "Now searching for", word
		r = api.request('search/tweets', {'q': word})
		entry = []

		for item in r.get_iterator():
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
				entry.append(id_str + ',' + cords + ',' + text + ',' + screen_name + ',' + created_at + '\n')
	return entry
	
def checkDup(searchresult):
	# Loop through the search results and check each one
	# for each line in the logfile
	for line in searchresult:
		isDuplicate = False #initiate isDuplicate flag at false
		logfile = codecs.open("log.csv", mode="r", encoding='utf-8')
		tweetID = line[0:18]
	
		# Check each entry in the logfile and set isDuplicate flag
		# to true if the Tweet ID is found
		for entry in logfile: 
			if (tweetID==entry[0:18]):
				isDuplicate = True
				break
			else:
				pass
		# If, after checking each line in the log, the isDuplicate flag
		# is still false, then call addentry() and pass the current line
		# from the search results
		if (isDuplicate==False):
			logfile.close()
			addEntry(unicode(line))
		logfile.close()

def addEntry(entry):
	logfile = codecs.open("log.csv", mode="a", encoding='utf-8')
	logfile.write(entry)
	print "Added Tweet ID#" + entry[0:18] + " to log.csv"
	logfile.close()
	

searchresult = search(word_list)
checkDup(searchresult)