from domain.nasa_service_interface import NASAServiceInterface
import requests
from typing import List, Dict

class NASAService(NASAServiceInterface):
    API_KEY = "HXscjhRXSdtlBsg71cZJBooDxGhpLFeGgzUYIw6b"
    BASE_URL = "https://api.nasa.gov/DONKI"
    
    def fetch_data(self, route: str) -> List[Dict]:
        """Consulta la API de NASA DONKI para la ruta dada."""
        url = f"{self.BASE_URL}/{route}?api_key={self.API_KEY}"
        response = requests.get(url)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error al obtener datos de {route}. Código de estado: {response.status_code}")
            return []  # Devuelve una lista vacía si hay error en la consulta
