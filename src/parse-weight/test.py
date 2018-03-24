import parse_weight
import json
import os

tweets = [
  {
    "created_at": "Sun Mar 18 07:29:56 +0000 2018",
    "id": 975273078119849984,
    "id_str": "975273078119849984",
    "text": "今日の体重:82.4kg\n#繋がらなくてもいいからうめかにかまの体重を見てくれ",
    "truncated": False,
    "entities": {
      "hashtags": [
        {
          "text": "繋がらなくてもいいからうめかにかまの体重を見てくれ",
          "indices": [
            13,
            39
          ]
        }
      ],
      "symbols": [],
      "user_mentions": [],
      "urls": []
    },
    "source": "<a href=\"http://twitter.com\" rel=\"nofollow\">Twitter Web Client</a>",
    "in_reply_to_status_id": None,
    "in_reply_to_status_id_str": None,
    "in_reply_to_user_id": None,
    "in_reply_to_user_id_str": None,
    "in_reply_to_screen_name": None,
    "user": {
      "id": 974957378373234688,
      "id_str": "974957378373234688"
    },
    "geo": None,
    "coordinates": None,
    "place": None,
    "contributors": None,
    "is_quote_status": False,
    "retweet_count": 0,
    "favorite_count": 0,
    "favorited": False,
    "retweeted": False,
    "lang": "ja"
  },
  {
    "created_at": "Sat Mar 17 10:37:31 +0000 2018",
    "id": 974957899729461249,
    "id_str": "974957899729461249",
    "text": "今日の体重:79.7kg\n#繋がらなくてもいいからうめかにかまの体重を見てくれ",
    "truncated": False,
    "entities": {
      "hashtags": [
        {
          "text": "繋がらなくてもいいからうめかにかまの体重を見てくれ",
          "indices": [
            13,
            39
          ]
        }
      ],
      "symbols": [],
      "user_mentions": [],
      "urls": []
    },
    "source": "<a href=\"http://twitter.com\" rel=\"nofollow\">Twitter Web Client</a>",
    "in_reply_to_status_id": None,
    "in_reply_to_status_id_str": None,
    "in_reply_to_user_id": None,
    "in_reply_to_user_id_str": None,
    "in_reply_to_screen_name": None,
    "user": {
      "id": 974957378373234688,
      "id_str": "974957378373234688"
    },
    "geo": None,
    "coordinates": None,
    "place": None,
    "contributors": None,
    "is_quote_status": False,
    "retweet_count": 0,
    "favorite_count": 0,
    "favorited": False,
    "retweeted": False,
    "lang": "ja"
  },
  {
    "created_at": "Sat Mar 17 10:36:47 +0000 2018",
    "id": 974957712780832768,
    "id_str": "974957712780832768",
    "text": "今日の体重:80.5kg（入社時+11.8kg）\n#繋がらなくてもいいからうめかにかまの体重を見てくれ",
    "truncated": False,
    "entities": {
      "hashtags": [
        {
          "text": "繋がらなくてもいいからうめかにかまの体重を見てくれ",
          "indices": [
            25,
            51
          ]
        }
      ],
      "symbols": [],
      "user_mentions": [],
      "urls": []
    },
    "source": "<a href=\"http://twitter.com\" rel=\"nofollow\">Twitter Web Client</a>",
    "in_reply_to_status_id": None,
    "in_reply_to_status_id_str": None,
    "in_reply_to_user_id": None,
    "in_reply_to_user_id_str": None,
    "in_reply_to_screen_name": None,
    "user": {
      "id": 974957378373234688,
      "id_str": "974957378373234688"
    },
    "geo": None,
    "coordinates": None,
    "place": None,
    "contributors": None,
    "is_quote_status": False,
    "retweet_count": 0,
    "favorite_count": 0,
    "favorited": False,
    "retweeted": False,
    "lang": "ja"
  }
]

event = {
  "Records": [
    {
      "EventVersion": "1.0",
      "EventSubscriptionArn": "arn:aws:sns:EXAMPLE",
      "EventSource": "aws:sns",
      "Sns": {
        "SignatureVersion": "1",
        "Timestamp": "1970-01-01T00:00:00.000Z",
        "Signature": "EXAMPLE",
        "SigningCertUrl": "EXAMPLE",
        "MessageId": "95df01b4-ee98-5cb9-9903-4c221d41eb5e",
        "Message": json.dumps(tweets),
        "MessageAttributes": {
          "Test": {
            "Type": "String",
            "Value": "TestString"
          },
          "TestBinary": {
            "Type": "Binary",
            "Value": "TestBinary"
          }
        },
        "Type": "Notification",
        "UnsubscribeUrl": "EXAMPLE",
        "TopicArn": "arn:aws:sns:EXAMPLE",
        "Subject": "TestInvoke"
      }
    }
  ]
}

os.environ['TABLE_NAME_WEIGHT_LOG'] = 'tweet-weight-logger-dev-t-weight-log'
parse_weight.main(event, 0)

