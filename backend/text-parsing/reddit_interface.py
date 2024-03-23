import requests
from requests.auth import HTTPBasicAuth
from typing import Dict
from dotenv import load_dotenv
import os
import re

load_dotenv()
access_token = os.getenv("REDDIT_TOKEN")


def request_data(url: str) -> Dict:
    headers = {'Authorization': f'bearer {access_token}', 'User-Agent': 'ChangeMeClient/0.1 by benled123'}
    base_url = f"https://oauth.reddit.com/api/info/?id=t3_"
    pattern = r'/comments/(\w+)/'

    match = re.search(pattern, url)
    if match:
        post_id = match.group(1)
        print("Post ID:", post_id)
    else:
        print("Post ID could not be extracted.")

    request_url = f"{base_url}{post_id}"
    response = requests.get(request_url, headers=headers)
    return response.json()['data']['children'][0]["data"]


def get_post_title(reddit_data: Dict) -> str:
    return reddit_data["title"]

def get_post_body(reddit_data: Dict) -> str:
    return reddit_data["selftext"]



