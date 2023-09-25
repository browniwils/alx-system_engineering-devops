#!/usr/bin/python3
"""Module prints todo list information for an employee."""
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get("{}users/{}".format(url, sys.argv[1])).json()
    todos = requests.get("{}todos".format(url),
                          params={"userId": sys.argv[1]}).json()
    complete = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(user.get("name"),
                                                          len(complete),
                                                          len(todos)))
    [print("\t {}".format(com)) for com in complete]

