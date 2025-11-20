import os
import difflib
import json
import requests

    
    

    
def load(api,city,url):
    params = {"q":city.lower(), "appid":api,"units":"imperial"}
    response = requests.get(url, params=params)
    return response.json()
    
def get_weather(which,api,url):
            data = load(api,which,url)
            try:
                   print(f" For {which} the temp is {data['main']['temp']}")
            except:
                    print("thats not a city lil bro")
                    get_weather(which,api,url)
                    

   
            
