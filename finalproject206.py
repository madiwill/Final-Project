# Name: Madison Willihnganz
# uniqname: madiwill
# Section Day/Time: Thursday/3-4pm

import json
import random
import requests
from facebook import Facebook

 def __init__(self):
        # Facebooks Debugger URL
        self.fb_url = 'https://developers.facebook.com/tools/debug/og/object'

def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

class Post():
    def __init__(self, post_dict={}):
    	if 'message' in post_dict:
    		self.message = post_dict['message']
    	else:
    		self.message = ""
    	if 'comments' in post_dict:
    		self.comments = post_dict['comments']['data']
    	else:
    		self.comments = []
    	if 'likes' in post_dict:
    		self.likes = post_dict['likes']['data']
    	else:
    		self.likes = []

access_token = "EAACB3qWFbHMBAJYZBHCv8LaEcF66pT78Ycw1AnsIkBUdu5xoxQ2f2QZCinC3RMqiVpL7WIZAOCWc6disZCYxToWIGmI6U01ZCTdjKxZBnJUJZBDqKkTZAsxzOlkWJ42rrx7poA6sFkvKTLoZC6mj9U7DkpKpCMcGvbJWvNQcrYdL4jFnAsZAWb4nxZA42Hchs2FAXAZD"
if access_token == None:
    access_token = raw_input("\nCopy and paste token from https://developers.facebook.com/tools/explorer\n>  ")

baseurl = "https://graph.facebook.com/v2.3/me/feed"
url_params = {}
url_params["access_token"] = access_token
# Write code to fill in other url_parameters dictionary here.
url_params['limit'] = 100
url_params['fields'] = 'message,comments,likes'
url_params['include_hidden'] = True

feed = requests.get(baseurl,params=url_params)
d = json.loads(feed.text)
for post in d['data']:
	if 'message' in post:
		print (post['message'])
