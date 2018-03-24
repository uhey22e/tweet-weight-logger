import os
import json
import re
import decimal
from datetime import datetime as dt
import boto3


def tw_parse_date(date_str):
    date = dt.strptime(date_str, '%a %b %d %H:%M:%S %z %Y')
    return int(date.timestamp())


def tweet_to_value(tweet):
    try:
        text = tweet['text']
    except:
        print('parse error')
        return None

    pattern = r'[0-9\.]+kg'
    match = re.search(pattern, text)
    if match is None:
        return None

    return {
        'tweet_id': tweet['id'],
        'tweet_text': tweet['text'],
        'tweeted_at': tw_parse_date(tweet['created_at']),
        'weight': decimal.Decimal(match.group()[:-2]),
    }


def save_to_db(data):
    dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-1')
    table = dynamodb.Table(os.environ['TABLE_NAME_WEIGHT_LOG'])
    now = int(dt.utcnow().timestamp())
    items = list(map(lambda v: {**v, **{'created_at': now}}, data))
    print(items)
    with table.batch_writer() as batch:
        for v in items:
            batch.put_item(Item=v)


def main(event, context):
    try:
        sns_data = event['Records'][0]['Sns']
        data = json.loads(sns_data['Message'])
    except JSONDecodeError:
        print('json decode error')
        return None
    except:
        print('parse data error')
        return None

    print('tweets')
    print(data)
    weight_logs = list(map(tweet_to_value, data))
    print(weight_logs)

    save_to_db(weight_logs)

    return weight_logs

