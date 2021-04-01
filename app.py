import os
import sys
import json
import subprocess
import requests


def getJoke():
    url = 'https://icanhazdadjoke.com/'
    headers = {
        'Accept': 'text/plain',
    }
    try:
        response = requests.get(url=url, headers=headers)
        return response.text
    except Exception as e:
        print(e)
        sys.exit(1)

def speakLoud(joke):
    speech = subprocess.Popen(["say", joke])

def main():
    joke = getJoke()
    print(joke)

    speakLoud(joke)
    

if __name__ == "__main__" : 
    main()
