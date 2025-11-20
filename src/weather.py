import os
import difflib
import json
import requests

    
    

    
def load(api,city,url):
    params = {"q":city.lower(), "appid":api,"units":"imperial"}
    response = requests.get(url, params=params)
    return response.json()
    
def get_weather(which,api,url):
            try: print()
            except: print()
   
            
