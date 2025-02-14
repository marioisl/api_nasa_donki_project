from flask import Flask
from api.instrument_controller import instrument_bp
from api.activity_controller import activity_bp  # Asegúrate de tener activity_controller si lo necesitas

app = Flask(__name__)

# Registrar blueprints
app.register_blueprint(instrument_bp, url_prefix='/api')
app.register_blueprint(activity_bp, url_prefix='/api')  # Si tienes activity_controller.py

# Ruta para la raíz del servicio
@app.route('/')
def index():
    return "Bienvenido a la API de NASA DONKI. Accede a /api/instruments o /api/activity_ids."

if __name__ == "__main__":
    app.run(debug=True)
