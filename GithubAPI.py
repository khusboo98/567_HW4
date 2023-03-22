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

import unittest
from unittest.mock import patch, MagicMock

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
            result = ""
            for i in data:
                name = i["name"]
                commits = requests.get("https://api.github.com/repos/" + userInput + "/" + name + "/commits")
                commits_data = len(commits.json())
                result += "Repo:" + name + " Number of commits: " + str(commits_data) + "\n"
            return result
        except:
            return "================================================================\n     YOU HAVE EXCEEDED YOUR API RATE LIMIT. SEE BELOW\n================================================================\n" + os.system("curl -i https://api.github.com/users/" + userInput)

class TestGitHubFunction(unittest.TestCase):
    @patch('requests.get')
    def test_gitHubFunction(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = [{"name": "repo1"}, {"name": "repo2"}]
        mock_get.return_value = mock_response

        result = gitHubFunction("mock_username")
        expected_result = "Repo:repo1 Number of commits: 5\nRepo:repo2 Number of commits: 10\n"
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()


