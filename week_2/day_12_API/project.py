import requests
api_key=input("enter the api key")
header={
    "x-api-key":api_key
}
city_name=input("enter the name of city to gget weather")
url=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}"
helo=requests.get(url,headers=header)
if helo.status_code==200:

    
    print(f"{city_name}'s temp is {helo.json()["main"]["temp"]-273}℃ with {helo.json()["weather"][0]["description"]}")
else:
    print(f"there is a error{helo.status_code}")