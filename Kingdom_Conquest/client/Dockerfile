# Usar una imagen oficial de Python como base
FROM python:3.9-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar el archivo de requerimientos
COPY ./requirements.txt /app/requirements.txt

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente del cliente
COPY ./src /app/src

# Establecer la variable de entorno para Python
ENV PYTHONPATH=/app/src  
ENV DOCKER_ENV2="True"

# Comando para iniciar la interfaz de consola
CMD ["python", "src/console_ui.py"]
