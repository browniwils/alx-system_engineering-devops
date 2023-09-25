#!/usr/bin/python3
"""Script exports todo list information for an employee to JSON format."""
import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get("{}users/{}".format(url, user_id)).json()
    username = user.get("username")
    todos = requests.get("{}todos".format(url),
                          params={"userId": user_id}).json()
    with open("{}.json".format(user_id), "w") as file_:
        json.dump({user_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todos]}, jsonfile_)

