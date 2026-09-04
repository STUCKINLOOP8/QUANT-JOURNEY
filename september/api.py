# 1. WHAT IS AN API?

# API stands for:
# Application Programming Interface

# An API allows two programs to communicate.

# Example:

# Your Python Program
#        |
#        v
#      API
#        |
#        v
#     Server


# Your program sends a request.
# The server sends back a response.


# 2. SIMPLE REAL-LIFE EXAMPLES

# APIs are used for:

# Weather
# News
# Stock prices
# Maps
# Payments
# AI
# Sports scores
# Cryptocurrency prices
# Login systems
# Government data


# 3. BASIC API FLOW

# Step 1:
# Your program sends a request.

# Step 2:
# The API receives the request.

# Step 3:
# The server processes it.

# Step 4:
# The API sends a response.

# Step 5:
# Your Python program reads the response.


# 4. IMPORTANT API WORDS

# API
# Allows programs to communicate.


# Endpoint
# The URL where we send a request.


# Request
# Data sent to the API.


# Response
# Data returned by the API.


# JSON
# Common format used to send data.


# Status Code
# Number that tells whether the request worked.


# API Key
# A secret key used to access some APIs.


# 5. requests LIBRARY

# Python commonly uses the requests library
# for working with APIs.

# requests is NOT built into Python.

# Install it using terminal:

# pip install requests


# Or:

# python -m pip install requests


# 6. IMPORT requests

import requests


# 7. SIMPLE GET REQUEST

# GET means:
# Get or receive data.


url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

print(response)


# Output:

# <Response [200]>


# 8. STATUS CODE

print(response.status_code)

# Output:
# 200


# 200 usually means:
# The request was successful.


# 9. COMMON STATUS CODES

# 200
# Request successful.


# 201
# Data created successfully.


# 400
# Bad request.


# 401
# Unauthorized.


# 403
# Access forbidden.


# 404
# Data not found.


# 429
# Too many requests.


# 500
# Server error.


# For beginners,
# remember mainly:

# 200 = Success
# 201 = Created
# 400 = Bad Request
# 401 = Unauthorized
# 403 = Forbidden
# 404 = Not Found
# 500 = Server Error


# 10. RESPONSE TEXT

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

print(response.text)


# response.text returns the response
# as normal text/string.


# 11. RESPONSE JSON

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

data = response.json()

print(data)


# response.json()
# converts JSON into Python data.


# Usually:

# JSON Object
# becomes
# Python Dictionary


# JSON Array
# becomes
# Python List


# 12. CHECK TYPE OF API DATA

data = response.json()

print(type(data))

# Output:
# <class 'dict'>


# 13. ACCESSING API DATA

data = response.json()

print(data["id"])

print(data["title"])

print(data["body"])


# API JSON works like
# normal Python dictionaries.


# 14. SAFER ACCESS USING get()

data = response.json()

title = data.get("title")

print(title)


# get() is safer than [] when
# you are not sure whether a key exists.


# Example:

username = data.get(
    "username",
    "Not Found"
)

print(username)


# 15. CHECKING STATUS BEFORE USING DATA

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print(data)
else:
    print("Request failed")


# 16. response.ok

response = requests.get(url)

if response.ok:
    print("Request successful")
else:
    print("Request failed")


# response.ok is True
# when the request is generally successful.


# 17. BASIC GET REQUEST WITH TIMEOUT

response = requests.get(
    url,
    timeout=10
)

print(response.status_code)


# timeout=10 means:
# Wait maximum about 10 seconds
# for the request.


# It is a good habit to use timeout.


# 18. GET REQUEST WITH QUERY PARAMETERS

# Some APIs need extra information.

# Example:

# https://example.com/search?q=python


# q=python is called a query parameter.


url = "https://jsonplaceholder.typicode.com/comments"

params = {
    "postId": 1
}

response = requests.get(
    url,
    params=params
)

print(response.url)

print(response.json())


# requests automatically creates
# the correct URL.


# 19. MULTIPLE QUERY PARAMETERS

params = {
    "page": 1,
    "limit": 10,
    "search": "python"
}


# Example:

# response = requests.get(
#     url,
#     params=params
# )


# 20. WHAT IS JSON?

# JSON stands for:

# JavaScript Object Notation


# JSON is commonly used by APIs.


# Example JSON:

# {
#     "name": "Alice",
#     "age": 20,
#     "course": "CSE"
# }


# It looks similar to a Python dictionary.


# 21. JSON OBJECT TO PYTHON DICTIONARY

# API response:

# {
#     "name": "Alice",
#     "age": 20
# }


# After:

# data = response.json()


# Python gives:

data = {
    "name": "Alice",
    "age": 20
}


print(data["name"])


# 22. JSON ARRAY TO PYTHON LIST

# API could return:

# [
#     {
#         "name": "Alice"
#     },
#     {
#         "name": "Bob"
#     }
# ]


# Python receives a list.


users = [
    {
        "name": "Alice"
    },
    {
        "name": "Bob"
    }
]


print(users[0])

print(users[0]["name"])


# 23. LOOPING THROUGH API DATA

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

posts = response.json()


for post in posts[:5]:
    print(post["title"])


# posts is a list.

# Every post is a dictionary.


# 24. NESTED JSON

user = {
    "name": "Alice",
    "address": {
        "city": "Delhi",
        "pin": 110001
    }
}


print(user["address"]["city"])

# Output:
# Delhi


# API responses often contain
# nested dictionaries.


# 25. LIST INSIDE JSON

student = {
    "name": "Alice",
    "subjects": [
        "Python",
        "Maths",
        "Physics"
    ]
}


print(student["subjects"][0])

# Output:
# Python


# 26. HTTP METHODS

# Main methods:

# GET
# Receive data.


# POST
# Send or create data.


# PUT
# Replace existing data.


# PATCH
# Update some data.


# DELETE
# Delete data.


# As a beginner,
# focus mainly on:

# GET
# POST


# 27. GET REQUEST

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

print(response.json())


# GET means:
# Give me some data.


# 28. POST REQUEST

# POST is usually used to create data.


url = "https://jsonplaceholder.typicode.com/posts"


data = {
    "title": "Learning APIs",
    "body": "My first API request",
    "userId": 1
}


response = requests.post(
    url,
    json=data
)


print(response.status_code)

print(response.json())


# json=data means:
# Send this Python dictionary
# as JSON.


# 29. POST RESPONSE

response_data = response.json()

print(response_data)


# The server may return
# the data that was created.


# 30. GET VS POST

# GET
# Used to receive data.


# POST
# Used to send/create data.


# Example:

# GET
# Give me student information.


# POST
# Create a new student.


# 31. BASIC PUT REQUEST

# PUT usually replaces existing data.


url = "https://jsonplaceholder.typicode.com/posts/1"


data = {
    "id": 1,
    "title": "Updated Title",
    "body": "Updated Body",
    "userId": 1
}


response = requests.put(
    url,
    json=data
)


print(response.json())


# 32. BASIC PATCH REQUEST

# PATCH updates only selected data.


url = "https://jsonplaceholder.typicode.com/posts/1"


data = {
    "title": "New Title"
}


response = requests.patch(
    url,
    json=data
)


print(response.json())


# 33. BASIC DELETE REQUEST

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.delete(url)

print(response.status_code)


# DELETE asks the server
# to delete something.


# 34. CRUD

# CRUD means:

# Create
# Read
# Update
# Delete


# Usually:

# Create
# POST


# Read
# GET


# Update
# PUT / PATCH


# Delete
# DELETE


# 35. HEADERS

# Headers send extra information
# with a request.


headers = {
    "Accept": "application/json"
}


response = requests.get(
    "https://jsonplaceholder.typicode.com/posts/1",
    headers=headers
)


print(response.json())


# 36. COMMON HEADERS

# Accept
# Tells API what response format we want.


# Content-Type
# Tells API what type of data we are sending.


# Authorization
# Used for authentication.


# Example:

headers = {
    "Accept": "application/json"
}


# 37. RESPONSE HEADERS

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts/1"
)


print(response.headers)


# Get one header:

print(
    response.headers.get(
        "Content-Type"
    )
)


# 38. API KEY

# Some APIs require an API key.


# Example:

api_key = "YOUR_API_KEY"


# The API key may be sent in:

# URL parameters

# or

# headers


# 39. API KEY IN PARAMETERS

api_key = "YOUR_API_KEY"


params = {
    "api_key": api_key
}


# Example:

# response = requests.get(
#     "https://api.example.com/data",
#     params=params
# )


# 40. API KEY IN HEADER

api_key = "YOUR_API_KEY"


headers = {
    "X-API-Key": api_key
}


# Example:

# response = requests.get(
#     "https://api.example.com/data",
#     headers=headers
# )


# 41. BEARER TOKEN

# Some APIs use tokens.


token = "YOUR_TOKEN"


headers = {
    "Authorization": f"Bearer {token}"
}


# Example:

# response = requests.get(
#     "https://api.example.com/profile",
#     headers=headers
# )


# 42. IMPORTANT API KEY RULE

# NEVER upload your real API key
# to GitHub.


# Bad:

# API_KEY = "my_real_secret_key"


# Better:
# Store it in an environment variable.


# 43. ENVIRONMENT VARIABLE

import os


api_key = os.getenv("API_KEY")


print(api_key)


# os.getenv()
# reads a value stored
# in your computer environment.


# 44. CHECK API KEY

api_key = os.getenv("API_KEY")


if api_key is None:
    print("API key not found")
else:
    print("API key loaded")


# Do not print the actual API key
# in real projects.


# 45. BASIC ERROR HANDLING

try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1",
        timeout=10
    )

    print(response.json())

except requests.RequestException:
    print("Something went wrong")


# 46. BETTER ERROR HANDLING

try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1",
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    print(data)

except requests.RequestException as error:
    print("Request failed:", error)


# 47. raise_for_status()

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts/1"
)


response.raise_for_status()


# If the server returns a bad HTTP status,
# Python raises an error.


# 48. TIMEOUT ERROR

try:
    response = requests.get(
        "https://example.com",
        timeout=5
    )

except requests.Timeout:
    print("Request timed out")


# 49. CONNECTION ERROR

try:
    response = requests.get(
        "https://example.invalid",
        timeout=5
    )

except requests.ConnectionError:
    print("Could not connect")


# 50. SIMPLE ERROR HANDLING YOU SHOULD USE

try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1",
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    print(data)

except requests.RequestException as error:
    print("API Error:", error)


# This is enough for most beginner projects.


# 51. API ENDPOINT

# Endpoint means:
# The URL used to access something.


# Example:

# Base URL:

# https://api.example.com


# Endpoints:

# https://api.example.com/users

# https://api.example.com/products

# https://api.example.com/weather


# 52. USING BASE URL

base_url = "https://jsonplaceholder.typicode.com"


response = requests.get(
    base_url + "/posts/1"
)


print(response.json())


# 53. USING f-string IN URL

base_url = "https://jsonplaceholder.typicode.com"

post_id = 1


url = f"{base_url}/posts/{post_id}"


response = requests.get(url)


print(response.json())


# 54. RESPONSE ATTRIBUTES

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts/1"
)


# Status code:

print(response.status_code)


# Text:

print(response.text)


# Headers:

print(response.headers)


# URL:

print(response.url)


# JSON:

data = response.json()

print(data)


# 55. response.text VS response.json()

# response.text

# Gives response as a string.


# response.json()

# Converts JSON response
# into Python data.


# Example:

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts/1"
)


print(type(response.text))

# str


print(type(response.json()))

# dict


# 56. CHECK FOR 404

url = "https://jsonplaceholder.typicode.com/posts/999999"


response = requests.get(url)


if response.status_code == 404:
    print("Data not found")

elif response.status_code == 200:
    print(response.json())

else:
    print("Something went wrong")


# 57. SAFELY ACCESS RESPONSE DATA

data = {
    "name": "Alice"
}


# Risky:

# print(data["age"])


# Better:

age = data.get(
    "age",
    "Not available"
)


print(age)


# 58. BASIC FUNCTION FOR API CALL

def get_post(post_id):
    url = (
        "https://jsonplaceholder.typicode.com/"
        f"posts/{post_id}"
    )

    response = requests.get(
        url,
        timeout=10
    )

    if response.status_code == 200:
        return response.json()

    return None


post = get_post(1)


if post is not None:
    print(post["title"])
else:
    print("Post not found")


# 59. BETTER FUNCTION WITH ERROR HANDLING

def get_post(post_id):
    url = (
        "https://jsonplaceholder.typicode.com/"
        f"posts/{post_id}"
    )

    try:
        response = requests.get(
            url,
            timeout=10
        )

        response.raise_for_status()

        return response.json()

    except requests.RequestException as error:
        print("Error:", error)

        return None


post = get_post(1)


if post is not None:
    print("Title:", post.get("title"))


# 60. FUNCTION WITH QUERY PARAMETERS

def get_comments(post_id):
    url = (
        "https://jsonplaceholder.typicode.com/"
        "comments"
    )

    params = {
        "postId": post_id
    }

    response = requests.get(
        url,
        params=params,
        timeout=10
    )

    return response.json()


comments = get_comments(1)


print(len(comments))


# 61. FUNCTION FOR POST REQUEST

def create_post(title, body):
    url = (
        "https://jsonplaceholder.typicode.com/"
        "posts"
    )

    data = {
        "title": title,
        "body": body,
        "userId": 1
    }

    response = requests.post(
        url,
        json=data,
        timeout=10
    )

    return response.json()


new_post = create_post(
    "Python API",
    "Learning how APIs work"
)


print(new_post)


# 62. API WITH USER INPUT

# Uncomment to test.


# post_id = int(
#     input(
#         "Enter post ID: "
#     )
# )


# url = (
#     "https://jsonplaceholder.typicode.com/"
#     f"posts/{post_id}"
# )


# response = requests.get(
#     url,
#     timeout=10
# )


# if response.status_code == 200:
#     data = response.json()

#     print("Title:", data["title"])

# else:
#     print("Post not found")


# 63. GOOD BEGINNER API PROGRAM

import requests


def get_user(user_id):
    url = (
        "https://jsonplaceholder.typicode.com/"
        f"users/{user_id}"
    )

    try:
        response = requests.get(
            url,
            timeout=10
        )

        if response.status_code == 404:
            return None

        response.raise_for_status()

        return response.json()

    except requests.RequestException as error:
        print("API Error:", error)

        return None


user = get_user(1)


if user is not None:
    print("User Details")

    print("Name:", user.get("name"))

    print("Username:", user.get("username"))

    print("Email:", user.get("email"))

    address = user.get(
        "address",
        {}
    )

    print(
        "City:",
        address.get(
            "city",
            "Unknown"
        )
    )

else:
    print("User not found")


# 64. SIMPLE WEATHER API STRUCTURE

# Real weather APIs usually work like this:


# import requests
# import os


# api_key = os.getenv("WEATHER_API_KEY")


# city = "Delhi"


# url = "https://api.example.com/weather"


# params = {
#     "city": city,
#     "api_key": api_key
# }


# response = requests.get(
#     url,
#     params=params,
#     timeout=10
# )


# if response.status_code == 200:
#     data = response.json()

#     print(data)

# else:
#     print("Weather request failed")


# Exact URL and parameter names
# depend on the API documentation.


# 65. HOW TO READ API DOCUMENTATION

# When using a new API,
# look for these things:


# Base URL

# Example:

# https://api.example.com


# Endpoint

# Example:

# /weather


# HTTP method

# GET
# POST


# Parameters

# Example:

# city
# country


# Authentication

# Example:

# API key


# Response

# Look at what JSON
# the API returns.


# 66. EXAMPLE API DOCUMENTATION

# Imagine documentation says:


# Endpoint:

# GET /weather


# Parameters:

# city
# api_key


# Then Python might look like:


# params = {
#     "city": "Delhi",
#     "api_key": api_key
# }


# response = requests.get(
#     "https://api.example.com/weather",
#     params=params
# )


# 67. COMMON BEGINNER ERROR:
# requests NOT INSTALLED

# Error:

# ModuleNotFoundError:
# No module named 'requests'


# Fix:

# python -m pip install requests


# 68. COMMON BEGINNER ERROR:
# WRONG PYTHON ENVIRONMENT

# Sometimes requests is installed,
# but VS Code uses another Python interpreter.


# Check:

import sys


print(sys.executable)


# This tells you which Python
# is running your program.


# Install requests using that Python.


# 69. COMMON BEGINNER ERROR:
# FORGETTING ()

# Wrong:

# data = response.json


# Correct:

data = response.json()


# response.json is the method.

# response.json()
# actually calls it.


# 70. COMMON BEGINNER ERROR:
# NO INTERNET

# API calls require internet access.

# If internet is unavailable,
# the request may fail.


# 71. COMMON BEGINNER ERROR:
# WRONG URL

# Example:

# https://api.example.com/user


# may be different from:

# https://api.example.com/users


# Always check API documentation.


# 72. COMMON BEGINNER ERROR:
# WRONG KEY NAME

data = {
    "name": "Alice"
}


# Wrong:

# print(data["username"])


# This gives KeyError.


# Better:

print(
    data.get(
        "username",
        "Not Found"
    )
)


# 73. COMMON BEGINNER ERROR:
# WRONG HTTP METHOD

# Example:

# API documentation says:

# POST /users


# But you send:

# requests.get(...)


# The request may fail.


# Always check which method
# the endpoint requires.


# 74. COMMON BEGINNER ERROR:
# API KEY IN GITHUB

# Never write:

# api_key = "real_secret_key"


# inside a public GitHub repo.


# Use:

api_key = os.getenv("API_KEY")


# 75. COMMON BEGINNER ERROR:
# IGNORING STATUS CODE

# Avoid:

# response = requests.get(url)
# data = response.json()


# Better:

response = requests.get(
    "https://jsonplaceholder.typicode.com/posts/1"
)


if response.status_code == 200:
    data = response.json()

    print(data)
else:
    print("Request failed")


# 76. COMMON BEGINNER ERROR:
# NO TIMEOUT

# Avoid:

# requests.get(url)


# Better:

# requests.get(
#     url,
#     timeout=10
# )


# 77. COMMON BEGINNER ERROR:
# CONFUSING JSON WITH DICTIONARY

# JSON is a data format.


# Python dictionary:

student = {
    "name": "Alice"
}


# JSON text:

json_text = """
{
    "name": "Alice"
}
"""


# response.json()
# converts JSON into Python data.


# 78. BASIC API CHEAT SHEET


# Import:

import requests


# GET:

# response = requests.get(
#     url
# )


# GET with timeout:

# response = requests.get(
#     url,
#     timeout=10
# )


# GET with parameters:

# response = requests.get(
#     url,
#     params={
#         "city": "Delhi"
#     }
# )


# POST:

# response = requests.post(
#     url,
#     json={
#         "name": "Alice"
#     }
# )


# Status:

# response.status_code


# JSON:

# response.json()


# Text:

# response.text


# Headers:

# response.headers


# Check error:

# response.raise_for_status()


# 79. MOST IMPORTANT requests FUNCTIONS


# requests.get()

# Receive data.


# requests.post()

# Send/create data.


# requests.put()

# Replace data.


# requests.patch()

# Update part of data.


# requests.delete()

# Delete data.


# 80. MOST IMPORTANT response THINGS


# response.status_code

# HTTP status.


# response.json()

# Convert JSON to Python.


# response.text

# Response as text.


# response.headers

# Response headers.


# response.url

# Final URL.


# response.ok

# Whether request was generally successful.


# response.raise_for_status()

# Raise an error for bad HTTP status.


# 81. MOST IMPORTANT ARGUMENTS


# params=

# Query parameters.


# Example:

params = {
    "postId": 1
}


# headers=

# Request headers.


headers = {
    "Accept": "application/json"
}


# json=

# JSON data being sent.


data = {
    "name": "Alice"
}


# timeout=

# Maximum time to wait.


# 82. WHAT TO LEARN FIRST

# As a beginner,
# focus on these:


# What an API is.

# Request.

# Response.

# Endpoint.

# GET.

# POST.

# JSON.

# Status codes.

# requests.get()

# requests.post()

# response.status_code

# response.json()

# params=

# headers=

# API keys.

# timeout.

# basic try-except.


# Do not worry about advanced API concepts yet.


# 83. COMPLETE BEGINNER API EXAMPLE

import requests


def fetch_post(post_id):
    url = (
        "https://jsonplaceholder.typicode.com/"
        f"posts/{post_id}"
    )

    try:
        response = requests.get(
            url,
            timeout=10
        )

        if response.status_code == 404:
            print("Post not found")

            return None

        response.raise_for_status()

        return response.json()

    except requests.RequestException as error:
        print("Request failed:", error)

        return None


post = fetch_post(1)


if post is not None:
    print("Post Details")

    print("ID:", post.get("id"))

    print("Title:", post.get("title"))

    print("Body:", post.get("body"))


# 84. COMPLETE BEGINNER POST EXAMPLE

import requests


def create_post():
    url = (
        "https://jsonplaceholder.typicode.com/"
        "posts"
    )

    new_post = {
        "title": "Learning Python APIs",
        "body": "This is my first POST request.",
        "userId": 1
    }

    try:
        response = requests.post(
            url,
            json=new_post,
            timeout=10
        )

        response.raise_for_status()

        return response.json()

    except requests.RequestException as error:
        print("Request failed:", error)

        return None


created_post = create_post()


if created_post is not None:
    print("Post Created")

    print(created_post)


# 85. FINAL THINGS TO REMEMBER

# API =
# Application Programming Interface


# API allows programs to communicate.


# requests is a Python library
# used to work with APIs.


# Install:

# python -m pip install requests


# Import:

# import requests


# GET:
# Receive data.


# POST:
# Create/send data.


# PUT:
# Replace data.


# PATCH:
# Update some data.


# DELETE:
# Delete data.


# JSON is the most common
# API data format.


# response.status_code
# tells whether request worked.


# response.json()
# converts JSON into Python data.


# response.text
# returns response as text.


# params=
# sends query parameters.


# headers=
# sends extra request information.


# json=
# sends JSON data.


# timeout=
# prevents waiting forever.


# 200 means success.

# 201 means created.

# 400 means bad request.

# 401 means unauthorized.

# 403 means forbidden.

# 404 means not found.

# 500 means server error.


# Never put real API keys
# inside public GitHub code.


# Always read the API documentation.


# END OF PYTHON API BASICS