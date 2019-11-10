import json
import os
from github import Github
from dotenv import load_dotenv, find_dotenv
from datetime import datetime
import requests

load_dotenv(find_dotenv())

# json_file = open("./raw_data.json", "r")
# raw_data = json.load(json_file)
# print(json.dumps(raw_data, indent=4, sort_keys=True))



g = Github(os.getenv("access_token"), per_page=30)

repo = g.get_repo("Sequelize/Sequelize")
print(repo)
pulls = repo.get_pulls(state='closed').get_page(0)
for pr in pulls:
    print(pr.user)
    print("PR Number = ", pr.number)
    # response = requests.get(pr.html_url)
    # print(response)
    # data = response.json()
    # print(data)
    # print("PR User Type = ", data.author_association)
    print("PR User Contribution History = ", repo.get_commits(author=pr.user).totalCount)
    print("PR Conservation History (Comment Count) = ", pr.get_issue_comments().totalCount)
    print("PR Time Duration = ", pr.closed_at - pr.created_at)
    print("PR Is Merged = ", pr.is_merged(), "\n")
