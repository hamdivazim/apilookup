## apilookup v1.0

> This is a simple, but helpful library I made! You can now easily make API requests with this library.
<br/>

### Prerequisites
> You only need the requests and json module for this to work.

### Installation Instructions
> You can copy the files to your project.<br/>

> You can run this command in your terminal:<br/>
` $ pip install apilookup `


### How To Use (it is easier to read in \_\_init\_\_.py)
apilookup allows you to get data from an API.
For example, say that an API (named api.a.com/users/123456789) contained this data:<br/>
    {
        "id": 123456789,<br/>
         "UUID": 12345678987654321,<br/>
        "visit_count": [<br/>
            1,<br/>
            2,<br/>
            3,<br/>
            4<br/>
        ]<br/>
        "profile_data": {<br/>
            "username": "Bob",<br/>
            "email": "example@gmail.com",<br/>
            "profile_picture_url": "https://a.com/users/bob/pfp.png",<br/>
            "bio": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Maxime mollitia,<br/>
                    molestiae quas vel sint commodi repudiandae consequuntur voluptatum laborum<br/>
                    numquam blanditiis harum quisquam eius sed odit fugiat iusto fuga praesentium<br/>
                    optio, eaque rerum!"<br/>
        }<br/>
    }<br/>
    and we wanted to get their 'id'.
    For this, you would use this code:
    `
        import apilookup
        lookup = apilookup.Lookup(default="api.a.com/users/123456789")
        id = lookup.get_data()["id"]
    `
    You can define a default url to be used any time you call the 'get_data()' method.