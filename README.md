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
