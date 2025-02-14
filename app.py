from flask import Flask
from api.instrument_controller import instrument_bp
from api.activity_controller import activity_bp  

app = Flask(__name__)

# Registrar blueprints
app.register_blueprint(instrument_bp, url_prefix='/api')
app.register_blueprint(activity_bp, url_prefix='/api')  #

if __name__ == "__main__":
    app.run(debug=True)
