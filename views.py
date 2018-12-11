from django.shortcuts import render
from django.http import HttpResponse
from  nltk.sentiment.util import *
import tweepy
from tweepy.streaming import StreamListener
from tweepy import Stream
from tweepy import OAuthHandler
import pandas as pd
import string
import nltk
from nltk import word_tokenize
from nltk.corpus  import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Create your views here.
def index(request):
    return render(request,'index.html')
def stats(request):
     #lib to analyze polarity
    #Acess details
    acess_token="956033448577241089-6S1DYfuZdl55BtGnArUHw8ofVWS4Cep"
    acess_token_secret="2gwgxEJC9OxsdhSgVRjcprzZY3GxFccb42LvSDSGAJkIK"
    consumer_key="flGGNLwGmqNiav5ooMwgkIklF"
    consumer_key_secret="FzSANGquLnPSlqAZAutGy7hbjEq0S3FrVFwzkrGEDKsp5OLirW"
    #connection establishment
    auth=tweepy.auth.OAuthHandler(consumer_key,consumer_key_secret)
    auth.set_access_token(acess_token,acess_token_secret)
    api=tweepy.API(auth)
    #fetched the tweets
    score=request.GET["tweet"]
    field=request.GET["field"]
    num=int(request.GET["count"])
    chart=request.GET["chart"]
    f_tweets=api.search(q=[score,field],result_type='recent',lang='en',count=num)
    def d_populate(tweets):
	    d_tweet=pd.DataFrame()
	    d_tweet['id']=list(map(lambda tweet:tweet.id,tweets))
	    d_tweet['text']=list(map(lambda tweet:tweet.text,tweets))
	    d_tweet['retweet']=list(map(lambda tweet:tweet.retweeted,tweets))
	    d_tweet['name']=list(map(lambda tweet:tweet.user.screen_name,tweets))
	    d_tweet['location']=list(map(lambda tweet:tweet.user.location,tweets))
	    d_tweet['verified_user']=list(map(lambda tweet:tweet.user.verified,tweets))
	    d_tweet['followers']=list(map(lambda tweet:tweet.user.followers_count,tweets))
	    d_tweet['friends']=list(map(lambda tweet:tweet.user.friends_count,tweets))
	    return d_tweet
    df=d_populate(f_tweets)
    sa=SentimentIntensityAnalyzer()
    df['polarity']=df.text.apply(lambda x:sa.polarity_scores(x)['compound']) #calculating the polarity score of each comment 
    df['negative']=df.text.apply(lambda x:sa.polarity_scores(x)['neg']) #checking neg score 
    df['neutral']=df.text.apply(lambda x:sa.polarity_scores(x)['neu']) #neutral score
    df['positive']=df.text.apply(lambda x:sa.polarity_scores(x)['pos']) #positvity score
    df['sentiment']=""
    #providing sentiments to each comment on basis of polarity_score
    df.loc[df.polarity>0,'sentiment']='POSITIVE' 
    df.loc[df.polarity==0,'sentiment']='NEUTRAL'
    df.loc[df.polarity<0,'sentiment']='NEGATIVE'
    #plotting statistics on bar grapgh
    import matplotlib.pyplot as plt
    if chart=='pie':
        df.sentiment.value_counts().plot(kind='pie',title='Sentiment Analysis')
        resp=plt.show()
    else:
        df.sentiment.value_counts().plot(kind='bar',title='Sentiment Analysis')
        resp=plt.show()
    return HttpResponse(resp)

