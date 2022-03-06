import requests, json

api_key = "589d6c0f8dde4e32241884fd5b5de354"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name =input("Enter city name : ") 
units = "metric"
lang = "zh_tw"

send_url = base_url
send_url += "appid=" + api_key
send_url += "&q=" + city_name
send_url += "&units=" + units
send_url += "&lang=" + lang

print("%s\n" % send_url)