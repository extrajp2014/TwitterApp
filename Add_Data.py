from twitoff.twitter import *
twitter_user = TWITTER.get_user('austen')
tweets = twitter_user.timeline(count=200, exclude_replies=True, include_rts=False, tweet_mode='extended')
db_user = User(id=twitter_user.id, name=twitter_user.screen_name, newest_tweet_id=tweets[0].id)
DB.session.add(db_user)

for tweet in tweets:
    embedding = BASILICA.embed_sentence(tweet.full_text, model='twitter')
    db_tweet = Tweet(id=tweet.id, text=tweet.full_text[:300], embedding=embedding)
    db_user.tweets.append(db_tweet)
    DB.session.add(db_tweet)

# DB.session.commit()
failed=False
try:
   DB.session.commit()
except Exception as e:
   #log your exception in the way you want -> log to file, log as error with default logging, send by email. It's upon you
   DB.session.rollback()
   DB.session.flush() # for resetting non-commited .add()
   failed=True
#some use of failed var, specific for your case if you need it
quit()

################################ 
# Add multiple users
################################ 
# from mytwit.models import *
# from mytwit.twitter import *
# userz = ['user1', 'user2', 'user3', 'user4', 'user5']
# for user in userz:
#     print(user)
#     twitter_user = TWITTER.get_user(user)
#     tweets = twitter_user.timeline(count=200, exclude_replies=True, tweet_mode='extended')
#     db_user = User(id=twitter_user.id, name=twitter_user.screen_name, newest_tweet_id=tweets[0].id)
#     DB.session.add(db_user)
#     for tweet in tweets:
#         embedding = BASILICA.embed_sentence(tweet.full_text, model='twitter')
#         db_tweet = Tweet(id=tweet.id, text=tweet.full_text[:300], embedding=embedding)
#         db_user.tweets.append(db_tweet)
#         DB.session.add(db_tweet)

# DB.session.commit()