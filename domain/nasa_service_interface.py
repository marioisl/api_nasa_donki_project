from abc import ABC, abstractmethod
from typing import List, Dict

class NASAServiceInterface(ABC):
    
    @abstractmethod
    def fetch_data(self, route: str) -> List[Dict]:
        """Consulta la API de NASA para obtener datos de la ruta especificada."""
        pass
