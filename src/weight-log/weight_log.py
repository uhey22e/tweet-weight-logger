import os
import sys
import traceback

import simplejson as json
import boto3

def get(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-1')
    table = dynamodb.Table(os.environ['TABLE_NAME_WEIGHT_LOG'])

    try:
        res = table.scan()
        body = json.dumps(res['Items'], ensure_ascii=False, encoding='utf-8', use_decimal=True)
    except:
        print('Table scan error.')
        t, v, tb = sys.exc_info()
        traceback.print_exception(t, v, tb)
        return {'statusCode': '500'}

    return {
        'statusCode': '200',
        'body': body,
        'headers': {
            'Content-Type': 'application/json',
        },
    }

