# Usa una imagen base con Python
FROM python:3.9-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos de requirements
COPY requirements.txt .

# Instala las dependencias necesarias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código en el contenedor
COPY . .

# Expone el puerto donde correrá el servidor FastAPI
EXPOSE 8000

# Comando de inicio (definido en docker-compose)
