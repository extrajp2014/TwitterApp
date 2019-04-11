"""Retrieve Tweets, embeddings, and persist in the database."""

from os import getenv
from dotenv import load_dotenv
import basilica
import tweepy
from .models import DB, Tweet, User

load_dotenv()
TWITTER_AUTH = tweepy.OAuthHandler(getenv('TWITTER_CONSUMER_KEY'),
                                   getenv('TWITTER_CONSUMER_SECRET'))
TWITTER_AUTH.set_access_token(getenv('TWITTER_ACCESS_TOKEN'),
                              getenv('TWITTER_ACCESS_TOKEN_SECRET'))
TWITTER = tweepy.API(TWITTER_AUTH)
BASILICA = basilica.Connection(getenv('BASILICA_KEY'))