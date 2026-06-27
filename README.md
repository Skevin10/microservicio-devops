# Microservicio DevOps

API HTTP mínima con dos endpoints para demostración.

## Requisitos
- Python 3.9+
- pip

## Instalación local

1. Crear entorno virtual:
   \`\`\`bash
   python3 -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   \`\`\`

2. Instalar dependencias:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

3. Ejecutar la app:
   \`\`\`bash
   python src/app.py
   \`\`\`

4. Probar:
   \`\`\`bash
   curl http://localhost:8080/health
   curl http://localhost:8080/version
   \`\`\`

## Variables de entorno
- `APP_VERSION`: Versión de la aplicación (default: "1.0.0")

# Build sin version
docker build -t microservicio:latest .

# Build con version específica
docker build -t microservicio:1.0.0 .

##########Correr Contenedor#######
#Basico
docker run -p 8080:8080 -e APP_VERSION=1.0.0 microservicio:latest

#Con nombre
docker run --name mi-app -p 8080:8080 -e APP_VERSION=2.5.1 microservicio:latest

Probar 
curl http://localhost:8080/health
# {"status":"ok"}

curl http://localhost:8080/version
# {"version":"2.5.1"}
