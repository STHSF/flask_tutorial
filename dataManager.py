import json
import time

def datestamp(date):
    result = int(time.mktime(time.strptime(date, '%Y-%m-%d %H:%M:%S')))
    print(result)
    return result
