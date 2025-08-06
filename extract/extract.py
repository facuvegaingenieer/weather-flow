from contracts.extract import extractor

import requests
import os


class ExtractorWeather(extractor):
    @classmethod
    def extract(cls):  # corregí nombre y convención 'cls' en vez de 'Self'
        try:
            API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")
            ciudad = os.getenv("CITY_DATA")
            url = "https://api.openweathermap.org/data/2.5/weather"
            params = {
                "q": ciudad,
                "appid": API_KEY,
                "units": "metric",  # grados Celsius
                "lang": "es",  # idioma español
            }
            response = requests.get(url, params=params)

            response.raise_for_status()  # esto lanza excepción si hay error HTTP

            data = response.json()
            return data

        except Exception as e:
            print(f"Error al obtener datos del clima: {e}")
            return None
