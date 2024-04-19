#retrieve_own_youtube_comments.py
# Big shoutout and credits to Benjamin Loison for providing the solution
# https://codeberg.org/Benjamin_Loison/Retrieve_own_YouTube_comments/src/branch/master/retrieve_own_youtube_comments.py


#!/usr/bin/python3

import requests
import config
import re
import json
from datetime import datetime
from xo.redis import xoRedis

url = 'https://myactivity.google.com/page?page=youtube_comments'

# cookies = {
#     'SID': config.SID,
#     'HSID': config.HSID,
#     'SSID': config.SSID,
#     'OSID': config.OSID,
#     '__Secure-1PSIDTS': config.__Secure_1PSIDTS
# }

cookies = config.cookie_dict

# First page is made of 100 comments.

text = requests.get(url, cookies = cookies).text
# print("#############")
# print(text)
# print("#############")
data = json.loads(re.findall(', data:(.*?), sideChannel', text)[-1])


def timestamp_to_datetime(timestamp_str):
    try:
        # Convert the timestamp string to a float (in seconds)
        timestamp = int(timestamp_str) / 1000000.0
        
        # Create a datetime object from the timestamp
        dt = datetime.fromtimestamp(timestamp)
        
        return dt
    except:
        return None

# Example usage:
# timestamp_str = "1355181858000000"


xo = xoRedis("my_comments",port=6379)
temp_comments = {}

def treatData(data):
    items = data[0]
    for item in items:
        timestamp = item[4]
        print("xxxxxx",type(timestamp))
        commentId = item[5]
        comment = item[9][0]
        video = item[23]
        temp_comments[commentId] = {}
        temp_comments[commentId]["comment"] = comment
        # Otherwise may be a community post comment for instance.
        if video != None:
            temp_comments[commentId]["video"] = {}
            videoDuration = video[1]
            videoId = video[3].split('=')[1]
            videoTitle = item[32][0][1]
            temp_comments[commentId]["video"]["videoId"] = videoId
            temp_comments[commentId]["video"]["videoTitle"] = videoTitle
            temp_comments[commentId]["video"]["videoDuration"] = videoDuration
            temp_comments[commentId][timestamp] = timestamp
            datet = timestamp_to_datetime(str(timestamp))
            temp_comments[commentId]["datetime"] = str(datet)
            # print("@@@", str(datet), commentId, comment, videoDuration, videoId, videoTitle)
            print("@@@", str(datet), videoTitle,"(",str(datet),") - ", comment)
            # dt = timestamp_to_datetime(timestamp_str)
            # print(dt)



paginationData = json.loads(re.search('window.WIZ_global_data = (.*?);</script>', text).group(1))

def getNextPageData(paginationToken):
    intermediary0Data = [
        [
            None,
            None,
            [
                'youtube_comments'
            ]
        ],
        paginationToken,
        100
    ]

    intermediary1Data = [
        [
            [
                'y3VFHd',
                json.dumps(intermediary0Data, separators=(',', ':')),
                None,
                'generic'
            ]
        ]
    ]

    nextPageData = f'f.req={json.dumps(intermediary1Data, separators=(",", ":"))}&at={paginationData["SNlM0e"]}'
    return nextPageData

def treatFollowingPage(data):
    url = 'https://myactivity.google.com/_/FootprintsMyactivityUi/data/batchexecute'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    nextPageData = getNextPageData(data[1])
    text = requests.post(url, cookies = cookies, headers = headers, data = nextPageData).text

    data = json.loads(json.loads(re.search('\[\["wrb.fr",(.*)\]\]', text).group())[0][2])

    treatData(data)
    return data

treatData(data)
while len(data) >= 2:
    data = treatFollowingPage(data)

print("#########################")
print("#########################")
print("#########################")
print(f"FOUND {len(temp_comments)} COMMENTS !!!")
added=[]
for key in temp_comments:
    if xo.comments[key].value == None:
        added.append([key,temp_comments[key]])
        xo.comments[key]._setValue(temp_comments[key])
        print("."*len(added)+key+":"+str(xo.comments[key].value),end="\r")
print()
print(f"Added {len(added)} comments to db")
print(temp_comments)
