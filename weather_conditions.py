import requests
from twilio.rest import Client

ACOUNT_SID = 'COLOQUE SEU ID DE CONTA AQUI'  
MY_API_KEY = 'COLOQUE SUA CHAVE DE API AQUI' 
AUTH_TOKEN = 'COLOQUE SEU TOKEN DE AUTENTICAÇÃO AQUI'
API_ENDPOINT = 'https://api.openweathermap.org/data/2.5/forecast'
weather_params = {
    'lat': 0,
    'lon': 0,
    'appid': MY_API_KEY, 
    
    'cnt': 4
}


request = requests.get(API_ENDPOINT, params=weather_params)
request.raise_for_status()

weather_data = request.json()

weather_condition = ""

for hour_data in weather_data['list']:
    condition = hour_data['weather'][0]['id']
    if int(condition) > 700:
        weather_condition = "Chuvinha"
    elif int(condition) < 300:
        weather_condition = "Tempestade"
    elif int(condition) < 600:
        weather_condition = "Chuva"
    elif int(condition) < 700:
        weather_condition = "Neve"
    elif int(condition) < 800:
        weather_condition = "Atmosfera"
    elif int(condition) == 800:
        weather_condition = "Céu Claro"
    else:
        weather_condition = "Nuvens"

TWILLIO_WHATSAPP = ''  
client = Client(ACOUNT_SID, AUTH_TOKEN)
message = client.messages.create(
    from_="whatsapp:'número twilio'",
    body=f"A condição do tempo é: {weather_condition}",
    to="whatsapp:'seu número'"
)
print('Mensagem enviada com sucesso')
print(message.status)
print(weather_condition)
