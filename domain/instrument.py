class Instrument:
    def __init__(self, display_name):
        self.display_name = display_name

    def to_dict(self):
        """Convierte el objeto Instrument a un diccionario para retornarlo en las respuestas JSON."""
        return {
            "display_name": self.display_name
        }
