class Activity:
    def __init__(self, activity_id):
        self.activity_id = activity_id

    def to_dict(self):
        """Convierte el objeto Activity a un diccionario para retornarlo en las respuestas JSON."""
        return {
            "activity_id": self.activity_id
        }
