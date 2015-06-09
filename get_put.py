import requests

MAX_LENGTH = 140  # max length of tweet defined by Twitter API
MAX_NUMBER_OF_TWEETS = 200  # max tweets to download defined by Twitter API


def put_tweet(session, tweet):
    if len(tweet) > MAX_LENGTH:
        tweet = tweet[:MAX_LENGTH]

    r = session.post('statuses/update.json', {'status': tweet})

    if r.status_code == requests.codes.ok:
        return 'Your tweet was successfully uploaded.'
    else:
        return 'Unable to post.'


def get_tweets(session, number_of_tweets):
    if number_of_tweets > MAX_NUMBER_OF_TWEETS:
        number_of_tweets = MAX_NUMBER_OF_TWEETS

    r = session.get('statuses/home_timeline.json',
                    params={'count': number_of_tweets})
    tweets = []

    if r.status_code == requests.codes.ok:
        for tweet in r.json():
            username = tweet['user']['screen_name']
            text = tweet['text']
            tweets.append('@{0}: {1}'.format(username, text))
    else:
        tweets.append('Unable to get tweets')

    return tweets
