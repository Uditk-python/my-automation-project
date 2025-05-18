


# QUERY PARAMETER
url="https://api.agify.io"
data={"name":"priya"}
hello=requests.get("https://api.agify.io",params=data)
print("estimated age of priya:",hello.json()["age"])




# PATH PARAMETER
name = "rahul"
url = f"https://api.nationalize.io?name={name}"
response = requests.get(url)
data = response.json()
print("Name:", data["name"])
print("Top nationality:", data["country"][0]["country_id"])



# API KEY
url = "https://httpbin.org/headers"
headers = {
    "x-api-key": "3455356CCBBHH"
}
res = requests.get(url, headers=headers)
print(res.json())



# POST-REQUESTS
import  requests
url = "https://httpbin.org/post"
data = {
    "name": "Rohit",
    "email": "rohit@example.com"
}
res = requests.post(url, data=data)
print(res.json())




# NEW POST-REQUESTS
import requests
import json

url = "https://httpbin.org/post"
data = {
    "name": "Rohit",
    "email": "rohit@example.com"
}
# Sending JSON data instead of form data
res = requests.post(url, json=data)
print(res.json())




# authentication 
import requests
from requests.auth import HTTPBasicAuth
url = "https://httpbin.org/basic-auth/user/passwd"
response = requests.get(url, auth=HTTPBasicAuth('user', 'passwd'))
print(response.json())


# TOKEN AUTHENTICATION
import requests
url = "https://api.example.com/data"
headers = {
    "Authorization": "Bearer YOUR_TOKEN"
}
response = requests.get(url, headers=headers)
print(response.json())



# POST Request with Payload
import requests
url = "https://reqres.in/api/users/2"
data = {
    "name": "Udit",
    "job": "developer"
}
response = requests.get(url)
# response = requests.post(url,data=data)
print(response.status_code)
print(response.json())



# GETTING THE DATA
import requests
url="https://reqres.in/api/users?page=1"
hello=requests.get(url)
for users in hello["data"]:
    print("name:",users["first_name"],users["last_name"])