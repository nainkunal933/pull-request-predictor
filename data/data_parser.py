import json
import os
from dotenv import load_dotenv, find_dotenv
from datetime import datetime
import requests

load_dotenv(find_dotenv())

owner = "sequelize"
repos = "sequelize"
response = requests.get("https://api.github.com/repos/%s/%s/pulls?state=closed&page=1&per_page=1" % (owner, repos), headers={'Authorization': 'token %s' % (os.getenv("access_token"))})
json_response = response.json()

for pr in json_response:
    status_check = requests.get("https://api.github.com/repos/%s/%s/commits/%s/status" % (owner, repos, pr["head"]["sha"]), headers={'Authorization': 'token %s' % (os.getenv("access_token"))})
    status_check = status_check.json()

    user_contr = requests.get("https://api.github.com/repos/%s/%s/commits?author=%s&per_page=100" % (owner, repos, pr["head"]["user"]["login"]), headers={'Authorization': 'token %s' % (os.getenv("access_token"))})

    comment_count = requests.get("https://api.github.com/repos/%s/%s/issues/%s/comments?per_page=100" % (owner, repos, pr["number"]), headers={'Authorization': 'token %s' % (os.getenv("access_token"))})

    closed_at = pr["closed_at"]
    created_at = pr["created_at"]
    created_at_timeobject = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%SZ")
    closed_at_timeobject = datetime.strptime(closed_at, "%Y-%m-%dT%H:%M:%SZ")
    time = closed_at_timeobject - created_at_timeobject

    print("PR Number = ", pr["number"])
    print("PR Status Check = ", status_check["state"])
    print("PR User Type = ", pr["author_association"])
    print("PR User Contribution History = ", len(user_contr.json()))
    print("PR Conversation History (Comment Count) = ", len(comment_count.json()))
    print("PR Time Duration", time.total_seconds())
    print("PR Is Merged = ", pr["merged_at"], "\n")
