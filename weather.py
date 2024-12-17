import requests  # type: ignore
from plyer import notification  # type: ignore

CITY = "Щёлково"
API_KEY = "23496c2a58b99648af590ee8a29c5348"
UNITS = "metric"
LANG = "ru"

def get_weather_data(city: str, api_key: str, units: str, lang: str):
    """Получаем данные о погоде по заданному городу."""
    url = fr'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={units}&lang={lang}'
    response = requests.get(url)  # Сделали запрос и получили объект ответа
    if response.status_code == 200:
        return response.json()  # Получили объект Python из JSON
    else:
        print(f"Ошибка: {response.status_code}")
        return None

def extract_weather_info(weather_dict):
    """Извлекаем информацию о погоде из словаря."""
    if weather_dict:
        temp = weather_dict['main']['temp']
        feels_like = weather_dict['main']['feels_like']
        description = weather_dict['weather'][0]['description']
        return temp, feels_like, description
    return None, None, None

def notify_weather(temp, feels_like, description):
    """Отправляем уведомление о погоде."""
    notification.notify(
        title='Погода в Щёлково',
        message=f'Температура: {temp}°C\nОщущается как: {feels_like}°C\nОписание: {description}',
        app_name='Weather',
        app_icon=r"C:\Users\User-X\Desktop\Python\the-current-weather\sunny_sunshine_weather_2778.ico",
        timeout=10,
        toast=False,
    )

# Основной код
def main_display_weather_info(city, api_key, units, lang):
    weather_data = get_weather_data(city, api_key, units, lang)
    temp, feels_like, description = extract_weather_info(weather_data)

    if temp is not None:
        print(f'Температура: {temp}°C\nОщущается как: {feels_like}°C\nОписание: {description}')
        notify_weather(temp, feels_like, description)

# Вызов функции
main_display_weather_info(CITY, API_KEY, UNITS, LANG)
