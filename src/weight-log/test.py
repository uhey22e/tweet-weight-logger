import os
from weight_log import get

os.environ['TABLE_NAME_WEIGHT_LOG'] = 'tweet-weight-logger-dev-t-weight-log'

print(get(None,None))

