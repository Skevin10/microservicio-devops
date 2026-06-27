# Imagen base liviana
FROM python:3.11-slim

# Directorio de trabajo
WORKDIR /app

# Copiar requirements
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código
COPY src/ ./src/

# Puerto
EXPOSE 8080

# Variable de entorno por defecto
ENV APP_VERSION=1.0.0

# Comando de inicio
CMD ["python", "src/app.py"]
