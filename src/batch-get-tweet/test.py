import batch_get_tweet
import os
import yaml

abs_path = os.path.dirname(os.path.abspath(__file__))
rel_path = os.path.normpath(os.path.join(abs_path, '../../twitter_key.yml'))

with open(rel_path, 'r') as fp:
    keys = yaml.load(fp)

print(keys)

try:
    os.environ['TWITTER_CONSUMER_KEY'] = keys['consumerKey']
    os.environ['TWITTER_CONSUMER_KEY_SECRET'] = keys['consumerKeySecret']
    os.environ['TWITTER_ACCESS_TOKEN'] = keys['accessToken']
    os.environ['TWITTER_ACCESS_TOKEN_SECRET'] = keys['accessTokenSecret']
except:
    print('error')

batch_get_tweet.main(0, 0)

