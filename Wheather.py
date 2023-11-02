import requests, json


# ingresamos la API KEY
api_key = "API_Key"

# direccion web desde donde solicitaremos la informacion
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# ciudad (se lo mas especifico posible en el nombre)
city_name = "Costa Rica"

# esta es la URL completa con la informacion concatenada para realizar la petición correcta
complete_url = base_url + "appid=" + api_key + "&q=" + city_name