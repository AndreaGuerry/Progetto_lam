import tweepy

auth = tweepy.OAuth2BearerHandler("AAAAAAAAAAAAAAAAAAAAAJxlegEAAAAAtd6LmEuYP4zp2Y2KmokwwhhXQM0%3Dzkqhu0v9BnBXHLpvQSe7EzotUIIQUPlQI4c8SH3D2C9tXgnIkL")
api = tweepy.API(auth)

result=tweepy.Client.search_all_tweets(query="bitcoin",end_time="2022-07-08T00:00:00.000Z",start_time="2022-07-07T00:00:00.000Z")