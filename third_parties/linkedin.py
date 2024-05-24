import os

import requests

from dotenv import load_dotenv

load_dotenv()


def scrap_linkedin_profile(linkedin_url: str, mock: bool = False):
    print("asd")
    if mock:
        linkedin_url = "https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/fad4d7a87e3e934ad52ba2a968bad9eb45128665/eden-marco.json"
        response = requests.get(
            linkedin_url,
            timeout=10
        )



if __name__ == "__main__":
    scrap_linkedin_profile(linkedin_url="https://www.linkedin.com/in/mario-bojarovski")
