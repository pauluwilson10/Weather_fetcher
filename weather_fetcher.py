import requests

API_KEY="a7fbe3a5872aa57bdbbfaf1c1ddf652e"
BASE_URL="https://api.openweathermap.org/data/2.5/weather"

city=input("Enter a city name: ")
requests_url=f"{BASE_URL}?appid={API_KEY}&q={city}"
response=requests.get(requests_url)
if response.status_code ==200:
    data=response.json()
    weather=data["weather"][0]["description"]
    temperature=data["main"]["temp"]
    temp=round((temperature-273.15),2)
    print(f"The temperature is: {temp} in(degree celcius)")
    print(f"The Weather is: {weather}")
    
    # temperature=
    
else:
    print("Error")