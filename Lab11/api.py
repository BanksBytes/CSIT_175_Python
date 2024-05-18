#!/usr/bin/env python3

# Jordan Banks
#Palomar College CSIT 175
# Lab 11 ex.1 Reading Data from an API


# The requests module is a third-party library for making HTTP requests in Python.
# It will need to be installed before this code will run. Try running these (2) lines
# from the command line (terminal) first
#  python3 -m pip % pip install --upgrade urllib3
#  python3 -m pip % pip install --upgrade requests

import requests


# try this URL in a browser. Refresh the pafe a couple times. What happened?
URL = "https://api.quotable.io/random"
SUCCESS_STATUS = 200


# returns a tuple with a quote and an author
def get_random_quote():
    response = requests.get(URL)
    # Every request/response returns a status code
    # You can see a list of status codes here : https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
    if response.status_code == SUCCESS_STATUS:
        # JSON text format is similiar to Python dictionaries
        data = response.json()
        content = data["content"]
        author = data["author"]
        return content, author
    else:
        print("Something wnt wrong:", response.status_code)
        return None,None
    

def read_from_api_demo():
    try:
        content, author = get_random_quote()
        if content and author:
            # '\n' newline, '\t' tab, '\"' quotation mark
            print(f"\n\t\"{content}\"\n\t\t - {author}\n\n")
    except Exception as e:
        print("An error occurred when calling the url {URL}:", e)

if __name__ == "__main__":
    read_from_api_demo()         