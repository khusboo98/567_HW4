#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 21:41:07 2023

@author: khusboopatel
"""

import json
import pprint
import os
import requests

# userInput = input("Username: ")
userInput = "khusboo98"

def gitHubFunction(userInput):
    if (userInput == "" or userInput == []):
        return "You must provide a username"
    elif (isinstance(userInput, str) != True):
        return "The input username is not valid"
    elif((requests.get("https://api.github.com/users/" + userInput + "/repos")).json() == []):
        return "This account does not have any repositories"
    else:
        repoName = requests.get("https://api.github.com/users/" + userInput + "/repos")
        data = repoName.json()
        try:
            for i in data:
                name = i["name"]
                commits = requests.get("https://api.github.com/repos/" + userInput + "/" + name + "/commits")
                commits_data = len(commits.json())
                # commits_data = commits.json()
                print("Repo:" + name + " Number of commits: " + str(commits_data))
        except:
            print("================================================================")
            print("     YOU HAVE EXCEEDED YOUR API RATE LIMIT. SEE BELOW")
            print("================================================================")
            print(os.system("curl -i https://api.github.com/users/" + userInput))

