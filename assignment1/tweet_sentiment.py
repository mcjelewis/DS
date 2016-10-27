import sys
import json
import re

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    afinn_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    getScore(afinn_file,tweet_file)
    lines(afinn_file)
    lines(tweet_file)

def getScore(afinn_file, tweet_txt):
	countTW = 0
	tweet_data = {}
	scores = {}
	afinn_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	tweets = tweet_file.read()
	for line in afinn_file:
		term, score = line.split("\t")
		scores[term] = int(score)
	#print scores.items()
    	for tweet in tweets.splitlines():
		try:
			json.loads(tweet)
		except ValueError:
			continue
		j = json.loads(tweet)
		if 'text' in j:
			tweet_text = unicode(j['text']).encode('utf-8')
			#print j['text']
			#print json.loads(tweet)
			countTW +=1
			twScore = 0
			
			for term in scores:
				regex = "r(\s+%s\s+)" % (term)
				pattern = re.compile(regex)
				matchObj = re.match(pattern, tweet_text)
				#print matchObj
				if matchObj:
					print term, score
					twScore += int(scores[term])
			#print tweet_text				
			print countTW, twScore
			tweetID = j['id_str']
			tweet_data.update({'tweetID': tweetID, 'tweetNum': countTW})
			tweet_data[tweetID] = {}
			tweet_data.update({'text': tweet_text, 'score': twScore, 'screen_name': j['user']['screen_name'], 'coordinates': j['coordinates'], 'hashtags': j['entities']['hashtags'], 'lang': j['lang'], 'id_str': j['id_str']})
			if 'place' in j:
				if j['place'] is not None:
					tweet_data.update({'country_code': j['place']['country_code'], 'cityState': j['place']['full_name'], 'city_name': j['place']['name'], 'place_type': j['place']['place_type']})
				else:
					tweet_data.update({'country_code': '', 'cityState': '', 'city_name': '', 'place_type': ''})




		#afinnfile = open(sys.argv[1])
		#scores = {}
		#for line in afinnfile:
		#	term, score = line.split("\t")
		#	scores[term] = int(score)
		#print scores.items()
		


if __name__ == '__main__':
    main()
