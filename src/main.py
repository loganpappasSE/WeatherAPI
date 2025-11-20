import weather
class main:
    api =  "1de7d0cedac5f28572181f9c89788818"
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={42}&lon={-93}&appid={api}"
    city = input("what city luh bro\n").lower()
    weather.load(api,city,url)
    weather.get_weather(city,api,url)