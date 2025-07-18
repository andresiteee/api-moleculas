# Usa una imagen oficial de Python como imagen base
FROM python:3.9-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Instala las dependencias del sistema requeridas por RDKit para dibujar
RUN apt-get update && apt-get install -y libxrender1 && rm -rf /var/lib/apt/lists/*

# Copia el archivo de dependencias al directorio de trabajo
COPY requirements.txt .

# Instala los paquetes necesarios especificados en requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia el contenido del directorio local al directorio de trabajo
COPY . .

# Comando para ejecutar la aplicación
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
