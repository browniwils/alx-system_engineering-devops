#!/usr/bin/python3
"""Script exports todo list information for an employee to CSV format."""
import csv
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get("{}users/{}".format(url, user_id)).json()
    username = user.get("username")
    todos = requests.get("{}todos".format(url),
                          params={"userId": user_id}).json()
    with open("{}.csv".format(user_id), "w", newline="") as file_:
        writer = csv.writer(file_, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
         ) for t in todos]

