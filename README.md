# Proyecto NASA DONKI API

Este proyecto utiliza la API abierta de NASA DONKI para obtener información sobre eventos solares y los instrumentos que los miden. A través de rutas API REST, puedes acceder a la información sobre los instrumentos utilizados en las mediciones, así como al porcentaje de uso de cada uno de ellos en diferentes actividades. El sistema está construido utilizando Flask para el backend y Python como lenguaje de programación.

Descripción

La API de NASA DONKI proporciona datos sobre eventos solares como eyecciones de masa coronal (CME), tormentas solares (HSS) y simulaciones de modelos solares (WSAEnlil). Este proyecto tiene como objetivo proporcionar una forma sencilla de consultar, analizar y obtener estadísticas sobre los instrumentos utilizados para medir estos eventos y las actividades asociadas a ellos.

Funcionalidades
Obtener todos los instrumentos utilizados en las mediciones.
Obtener todas las IDs de actividades sin mostrar las fechas.
Obtener el porcentaje de uso de cada instrumento en relación al total.
Obtener el porcentaje de uso de un instrumento específico en las actividades en las que ha sido utilizado.

## Requisitos
- Python 3.x
- Flask
- Requests
- Otros paquetes especificados en `requirements.txt`


Instalación --> Clonar el repositorio
Clona el repositorio en tu máquina local:

git clone https://github.com/tu-usuario/nasa-donki-api.git
cd nasa-donki-api

1. Crea un entorno virtual :

python3 -m venv venv

2. Activa el entorno virtual:

En Windows:

venv\Scripts\activate

En macOS/Linux:

source venv/bin/activate

Instalar dependencias
Instala las dependencias desde el archivo requirements.txt:

pip install -r requirements.txt

Ejecución

Iniciar la aplicación --> Para iniciar la aplicación, usa el siguiente comando:

python app.py

Esto arrancará el servidor de Flask en http://localhost:5000.

Acceder a las rutas de la API

Una vez que la aplicación esté en funcionamiento, puedes acceder a las siguientes rutas:

Obtener todos los instrumentos utilizados en las mediciones:
Método: GET
Ruta: /api/instrument/instruments
Descripción: Devuelve todos los instrumentos utilizados en las mediciones de las rutas disponibles.
Ejemplo de respuesta:

[
  { "display_name": "MODEL: SWMF" },
  { "display_name": "LASCO" }
]

Obtener el porcentaje de uso de cada instrumento:

Método: GET
Ruta: /api/instrument/instrument_usage
Descripción: Devuelve el porcentaje de uso de cada instrumento en las actividades.
Ejemplo de respuesta:

{
  "MODEL: SWMF": 0.3,
  "LASCO": 0.7
}

3. Obtener todas las IDs de actividades sin mostrar las fechas:

Método: GET
Ruta: /api/activity/activity_ids
Descripción: Devuelve todas las IDs de las actividades sin las fechas asociadas.
Ejemplo de respuesta:

[
  { "activity_id": "IPS-001" },
  { "activity_id": "HSS-001" },
  { "activity_id": "GST-001" }
]

4. Obtener el porcentaje de uso de un instrumento específico:

Método: GET
Ruta: /api/instrument/instrument_usage/{instrument_name}
Descripción: Devuelve el porcentaje de uso de un instrumento específico, proporcionando el nombre del instrumento como parámetro.
Ejemplo de respuesta:

{
  "instrument": "MODEL: SWMF",
  "usage_percentage": 0.3
}

Estructura del Proyecto
La estructura de archivos del proyecto es la siguiente:

/api_nasa_donki_project
│
├── app.py               
├── README.md            
├── requirements.txt    
├── .gitignore           
│
├── /api
│   ├── __init__.py
│   ├── instrument_controller.py
│   └── activity_controller.py
│
├── /services
│   ├── __init__.py
│   └── nasa_service.py
│
└── /domain
    ├── __init__.py
    ├── instrument.py
    └── activity.py

## Endpoints
- `/api/instruments`: Obtiene una lista de todos los instrumentos.
- `/api/activity_ids`: Obtiene los IDs de actividades.
- `/api/instrument_usage`: Obtiene el uso total de instrumentos.
- `/api/instrument_usage_by_activity`: Obtiene el porcentaje de uso de un instrumento en actividades específicas.

El proyecto utiliza las siguientes dependencias de Python, que puedes instalar con el archivo requirements.txt:

Flask: Framework para crear aplicaciones web en Python.
Requests: Librería para hacer solicitudes HTTP.

Agregar nuevas dependencias
Si necesitas agregar nuevas dependencias, asegúrate de añadirlas al archivo requirements.txt ejecutando:
pip freeze > requirements.txt

Tests
Se recomienda realizar pruebas en cada ruta API para asegurarte de que las respuestas sean correctas. Puedes utilizar herramientas como Postman o cURL para hacer pruebas manuales de las rutas. También puedes implementar pruebas unitarias en el futuro para mayor robustez.

Ejemplo de pruebas con cURL

Obtener todos los instrumentos:
http://localhost:5000/api/instrument/instruments

Obtener el porcentaje de uso de un instrumento específico:
http://localhost:5000/api/instrument/instrument_usage/MODEL%3A%20SWMF

## Despliegue
Este proyecto puede ser desplegado en [Vercel](https://vercel.com/)

## Postman Collection
Revisar el Json de Postman


## Licencia
Este proyecto es de código abierto.
