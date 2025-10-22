import requests

api_key = '30d4741c779ba94c470ca1f63045390a'
print("Ｗｅｌｃｏｍｅ ｔｏ ｗｅａｔｈｅｒ ａｐｐ\n")
print("Ｄｅｖｅｌｏｐｅｄ ｉｎ ｐｙｔｈｏｎ ｂｙ Ｍｒｉｄｕｌ\n")
print("Ｅｎｔｅｒ ｙｏｕｒ ｄｅｓｉｒｅｄ ｌｏｃａｔｉｏｎ ｂｅｌｏｗ！\n")
user_input = input("Ｅｎｔｅｒ ｃｉｔｙ：")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    InCelsius = round((temp-32)*(5/9))
    print(f"The visual weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {temp}ºF or {InCelsius}°C")
