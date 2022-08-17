"""
v1.0

apilookup allows you to get data from an API.

For example, say that an API (named api.a.com/users/123456789) contained this data:

    {
        "id": 123456789,
        "UUID": 12345678987654321,
        "visit_count": [
            1,
            2,
            3,
            4
        ]
        "profile_data": {
            "username": "Bob",
            "email": "example@gmail.com",
            "profile_picture_url": "https://a.com/users/bob/pfp.png",
            "bio": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime mollitia,
                    molestiae quas vel sint commodi repudiandae consequuntur voluptatum laborum
                    numquam blanditiis harum quisquam eius sed odit fugiat iusto fuga praesentium
                    optio, eaque rerum!"
        }
    }

    and we wanted to get their 'id'.

    For this, you would use this code:

    `
        import apilookup

        lookup = apilookup.Lookup(default="https://a.com/users/bob/pfp.png")

        id = lookup.get_data()["id"]
    `


    You can define a default url to be used any time you call the 'get_data()' method.

"""

import json
import requests

class Lookup: # Base class used for API lookups.
    def __init__(self, default="nil"):
        self.default = default

    def get_data(self, url=""): # Returns a dictionary with API data.
        res_url = url
        if res_url == "":
            if not self.default == "nil":
                res_url = self.default
            else:
                raise _exceptions.NoURLException

        response_API = requests.get(res_url)
        data = response_API.text
        parse_json = json.loads(data)

        return parse_json


if __name__ == "__main__":
    # Test script
    lookup = Lookup(default="https://api.scratch.mit.edu/users/codingboy_CW")

    username = lookup.get_data()["username"]
    join = lookup.get_data()["history"]["joined"]

    print(username, join)