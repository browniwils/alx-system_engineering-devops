#!/usr/bin/python3
"""Script exports todo list information of all employees to JSON format."""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get("{}users".format(url)).json()
    with open("todo_all_employees.json", "w") as file_:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in requests.get("{}0todos".format(url),
                                    params={"userId": u.get("id")}).json()]
            for u in users}, file_)
