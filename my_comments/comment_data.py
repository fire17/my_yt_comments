'''
### INSERT COMMENT:
https://developers.google.com/youtube/v3/docs/comments/insert?apix_params=%7B%22part%22%3A%5B%22snippet%22%5D%2C%22resource%22%3A%7B%22kind%22%3A%22youtube%23comment%22%2C%22snippet%22%3A%7B%22parentId%22%3A%22UgwtRJbNj5HHEMLcGux4AaABAg%22%2C%22textOriginal%22%3A%22YO%20YO%20FROM%20API!!!%22%7D%7D%7D
# add to request body:
{
  "kind": "youtube#comment",
  "snippet": {
    "parentId": "UgwtRJbNj5HHEMLcGux4AaABAg",
    "textOriginal": "YO YO FROM API!!!"
  }
}
'''
# -*- coding: utf-8 -*-

# Sample Python code for youtube.comments.insert
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "YOUR_CLIENT_SECRET_FILE.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.comments().insert(
        part="snippet",
        body={
          "kind": "youtube#comment",
          "snippet": {
            "parentId": "UgwtRJbNj5HHEMLcGux4AaABAg",
            "textOriginal": "(@fire17102)[https://www.youtube.com/channel/UCbDhLtzwBmaXJTqxu1sYo3w] YO YO FROM API2!!!"
          }
        }
    )
    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()


'''##################### GET ALL REPLIES ##############################'''

# -*- coding: utf-8 -*-

# Sample Python code for youtube.commentThreads.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os

import googleapiclient.discovery

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "YOUR_API_KEY"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        part="snippet,replies",
        id="UgwtRJbNj5HHEMLcGux4AaABAg,UgwtRJbNj5HHEMLcGux4AaABAg"
    )
    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()


'''###################################################'''
'''###################################################'''
'''###################################################'''
'''###################################################'''



import os
import googleapiclient.discovery

# Set up your API key and YouTube Data API service
api_key = "YOUR_API_KEY"  # Replace with your actual API key
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)

# Define the comment ID for which you want to retrieve replies
comment_id = "UgwtRJbNj5HHEMLcGux4AaABAg"

# Initialize variables for pagination
next_page_token = None
all_replies = []

# Loop to retrieve all replies
while True:
    # Call the comments().list() method with the comment ID and optional page token
    comments_response = youtube.comments().list(
        part="snippet",
        parentId=comment_id,
        maxResults=100,  # Maximum number of replies per page (you can adjust this)
        pageToken=next_page_token,
    ).execute()

    # Extract the replies from the response and add them to the list
    for comment in comments_response.get("items", []):
        all_replies.append(comment["snippet"]["textOriginal"])

    # Check if there are more pages of replies
    next_page_token = comments_response.get("nextPageToken")
    if not next_page_token:
        break  # No more pages of replies

# Print all the retrieved replies
for reply in all_replies:
    print(reply)

# Make sure to replace "YOUR_API_KEY" with your actual YouTube Data API v3 API key. This code will retrieve all the replies for the specified comment ID and print them to the console. You can adjust the maxResults parameter to control the number of replies fetched in each API call.





