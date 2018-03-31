import json
import os
import re
from requests_oauthlib import OAuth1Session

import boto3


def filter_weight_tweet(tweet):
    target = '繋がらなくてもいいからうめかにかまの体重を見てくれ'
    tags = [v['text'] for v in tweet['entities']['hashtags']]
    if target in tags:
        return True
    else:
        return False


def main(event, context):
    url = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
    twitter = OAuth1Session(
            os.environ['TWITTER_CONSUMER_KEY'],
            os.environ['TWITTER_CONSUMER_KEY_SECRET'],
            os.environ['TWITTER_ACCESS_TOKEN'],
            os.environ['TWITTER_ACCESS_TOKEN_SECRET'])
    params = {
        'user_id': os.environ['TWITTER_TARGET_USERID'],
        'count': 50,
        'exclude_replies': True,
        'trim_user': True,
    }

    try:
        res = twitter.get(url, params=params)
        tweets = json.loads(res.text)
    except:
        print('get tweet error')
        return {}

    weight_tweets = list(filter(filter_weight_tweet, tweets))

    if len(weight_tweets) == 0:
        print('no data')
        return {}
    else:
        print(f'{len(weight_tweets)} logging tweets found.')

    client = boto3.client('sns', region_name='ap-northeast-1')
    request = {
        'TopicArn': os.environ['WEIGHT_SNS_ARN'],
        'Message': json.dumps(weight_tweets, ensure_ascii=False),
    }

    response = client.publish(**request)

    return {}

