''' Twitter Scrapper for Grubhub '''

import csv
import tweepy
# import tokens
import secret_stuff

consumer_key = secret_stuff.c_key
consumer_secret = secret_stuff.Consumer_Secret
access_token = secret_stuff.access_token
access_token_secret = secret_stuff.access_token_secret


def search_for_hashtags(consumer_key, consumer_secret, access_token, access_token_secret, hashtag_phrase):
    
    #create authentication for accessing Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    #initialize Tweepy API
    api = tweepy.API(auth)  

    #open the spreadsheet we will write to
   
    with open('#Grubhub.csv','w') as file:
        

        w = csv.writer(file)

        #write header row to spreadsheet
        w.writerow(['timestamp', 'tweet_text', 'username', 'all_hashtags', 'followers_count'])

        #for each tweet matching either the hashtag or the keyword, print information in row
        # .items(#) indiciates the number of tweets we would like to grab
        
        for tweet in tweepy.Cursor(api.search, q=hashtag_phrase+' -filter:retweets', lang="en", tweet_mode='extended').items(10):
            
            w.writerow([tweet.created_at, tweet.full_text.replace('\n',' ').encode('utf-8'), tweet.user.screen_name.encode('utf-8'), [e['text'] for e in tweet._json['entities']['hashtags']], tweet.user.followers_count])
            
hashtag_phrase = input('Enter a Hashtag Phrase or Keyword to search (#): ' )

if __name__ == '__main__':
    search_for_hashtags(consumer_key, consumer_secret, access_token, access_token_secret, hashtag_phrase)
