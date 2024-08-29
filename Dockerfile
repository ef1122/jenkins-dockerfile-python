# Usar una imagen base oficial de Python
FROM python:3.10-slim

LABEL AUTHOR='Apasoft Training'
# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de requisitos (requirements.txt) y el código fuente
COPY requirements.txt requirements.txt
COPY temperature.py temperature.py

# Instalar las dependencias especificadas en requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Definir una variable de entorno para la API Key
ENV API_KEY="63f99e64f995efd1b8fc94bc462b2a51"


