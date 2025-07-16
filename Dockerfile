# Usar una imagen base oficial de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de requisitos e instalar las librerías
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el código de nuestra aplicación (app.py)
COPY . .

# Exponer el puerto 8080 para que Cloud Run pueda comunicarse con nuestro servidor
EXPOSE 8080

# El comando para iniciar la aplicación usando Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
