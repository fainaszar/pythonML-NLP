import tweepy

consumer_key ="CmLpgKRs7U0W3shqe17Dj9psC"
consumer_secret = "uRwmNXqnIkG9QBOeeo54pkA5Vg55OoDE06ZfEoFyRx31xRQbNf"
access_token = "958236456408907777-7gHyRTItt8EHNVf8rtrm1KvWCE5PH2f"
access_token_secret="7cfPLpCOl8V6ZeeszVyABglMNyv9Ia27YRTBR2ygt1ZIM"


auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

#api.update_status("An update from the app!")

# for tweet in tweepy.Cursor(api.search,q="#Kashmir").items(5):
# 	print("-"*10)
# 	print ("@" + tweet.user.screen_name + " via " + tweet.source + "\n" + tweet.text)
# 	print("Location: {}".format(tweet.author.location))
# 	print("-"*10)

import twitter
api = twitter.Api(
	consumer_key = consumer_key,
	consumer_secret = consumer_secret,
	access_token_key=access_token,
	access_token_secret=access_token_secret
	)

def getFriends(user):
	try:
		friends = api.GetFriends(screen_name=user)
		for friend in friends:
			print(friend.name)

	except Exception:
		print("Exception! Either you specified a wrong username or you are not authorized to access Friends of {}".format(user))


def getStatuses(user,count=30):
	statuses = api.GetUserTimeline(
		screen_name=user,
		count=count,
		include_rts=False
	)
	for status in statuses:
		print("-"*80)
		print (status.text)
		print("-"*80)


def getRecentStatus(user):
	status = api.GetUserTimeline(
		screen_name=user,
		count=1,
		include_rts=False
	)
	
	print(status[0].text)



user = "@" + input("Enter a Twitter Username : @")




#getFriends(user)
getStatuses(user,10)
#getRecentStatus(user)

