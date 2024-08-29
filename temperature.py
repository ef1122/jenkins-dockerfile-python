import requests

def get_weather(api_key, city):
    # URL de la API de OpenWeatherMap
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    # Hacer la petición GET a la API
    response = requests.get(url)
    
    # Verificar si la respuesta fue exitosa
    if response.status_code == 200:
        data = response.json()
        temp_celsius = data['main']['temp']
        return temp_celsius
    else:
        print(f"Error obteniendo datos para {city}. Código de estado: {response.status_code}")
        return None

def main():
    # Tu API key de OpenWeatherMap
    api_key = "221ef973315076a01c33d0215ebbfe02"

    # Ciudades a consultar
    cities = ["New York", "Madrid", "Paris"]

    # Obtener y mostrar la temperatura en Celsius de cada ciudad
    for city in cities:
        temp = get_weather(api_key, city)
        if temp is not None:
            print(f"La temperatura en {city} es {temp}°C")

if __name__ == "__main__":
    main()
