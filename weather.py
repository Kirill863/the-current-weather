## Код с урока для рефакторинга


"""
Это погодное приложение, которое работает на Python библиотеке requests, plyer.

pip install plyer requests pyinstaller

Образец ссылки https://api.openweathermap.org/data/2.5/weather?q=Москва&appid=23496c2a58b99648af590ee8a29c5348&units=metric&lang=ru

{'coord': {'lon': 37.6156, 'lat': 55.7522}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'облачно с прояснениями', 'icon': '04n'}], 'base': 'stations', 'main': {'temp': 0.93, 'feels_like': -3.44, 'temp_min': 0.24, 'temp_max': 0.93, 'pressure': 1022, 'humidity': 61, 'sea_level': 1022, 'grnd_level': 1002}, 'visibility': 10000, 'wind': {'speed': 4.47, 'deg': 214, 'gust': 11.97}, 'clouds': {'all': 64}, 'dt': 1733247335, 'sys': {'type': 2, 'id': 2095214, 'country': 'RU', 'sunrise': 1733204316, 'sunset': 1733230838}, 'timezone': 10800, 'id': 524901, 'name': 'Москва', 'cod': 200}

"""

import requests
from plyer import notification
# Просто сделаем запрос без функций

CITY = "Щёлково"
API_KEY = "23496c2a58b99648af590ee8a29c5348"
UNITS = "metric"
LANG = "ru"


url= fr'https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units={UNITS}&lang={LANG}'

response = requests.get(url) # Сделали запрос и получили объект ответа
print(response.status_code) # Получили статус ответа
print(response.json()) # Получили объект Python из JSON


# Получим описание и температуру, и ощущается как
weather_dict = response.json()

# Temp
temp = weather_dict['main']['temp']
# Ощущается как
feels_like = weather_dict['main']['feels_like']
# Описание погоды
description = weather_dict['weather'][0]['description']

print(f'Температура: {temp}°C\nОщущается как: {feels_like}°C\nОписание: {description}')

# Уведомление
notification.notify(
title= 'Погода в Щёлково',
message= f'Температура: {temp}°C\nОщущается как: {feels_like}°C\nОписание: {description}',
app_name='Weather',
app_icon = "the-current-weather\sunny_sunshine_weather_2778.ico",
timeout = 10,
toast = False,
)
