# Microservicio DevOps

API HTTP mínima con dos endpoints para demostración y aprendizaje de DevOps.

## Requisitos

- Python 3.9+
- Docker (para contenerización)
- Git (para control de versiones)

## Instalación y ejecución local

### Opción 1: Ejecutar directamente con Python

```bash
# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
python src/app.py
```

La app estará disponible en `http://localhost:8080`

### Opción 2: Con Docker

```bash
# Construir imagen
docker build -t microservicio:latest .

# Ejecutar contenedor
docker run -p 8080:8080 -e APP_VERSION=1.0.0 microservicio:latest
```

## Endpoints disponibles

### GET /health
Verifica que el servicio está corriendo.

```bash
curl http://localhost:8080/health
# Respuesta: {"status":"ok"}
```

### GET /version
Devuelve la versión actual del servicio.

```bash
curl http://localhost:8080/version
# Respuesta: {"version":"1.0.0"}
```

## Variables de entorno

- `APP_VERSION`: Versión de la aplicación (default: `1.0.0`)

## Health Check Automatizado

Se incluye un script para monitorear la salud del servicio en tiempo real.

### Uso básico

```bash
./healthcheck.sh
```

El script generará un archivo `healthcheck.log` con los resultados.

### Personalizar host y puerto

```bash
HC_HOST=192.168.1.100 HC_PORT=9090 ./healthcheck.sh
```

### Programar chequeos periódicos con cron

Para ejecutar cada 5 minutos:

```bash
*/5 * * * * /path/to/healthcheck.sh
```

### Variables soportadas

| Variable | Default | Descripción |
|----------|---------|-------------|
| `HC_HOST` | localhost | Host del servicio |
| `HC_PORT` | 8080 | Puerto del servicio |
| `HC_LOG` | healthcheck.log | Archivo de log |

## Pipeline CI/CD

El repositorio cuenta con un pipeline automático en GitHub Actions que ejecuta:

- Validación de código (flake8)
- Tests unitarios (pytest)
- Construcción de imagen Docker
- Pruebas del contenedor

Puedes ver el estado en la pestaña **Actions** del repositorio.

## Seguridad y Secretos

### En GitHub Actions

Los secretos nunca se hardcodean. Se definen en `Settings → Secrets and variables → Actions`:

```yaml
- name: API Call
  run: |
    curl -H "Authorization: Bearer ${{ secrets.API_KEY }}" https://api.example.com
```

**Ventajas:**
- No aparecen en logs ni historial de Git
- Encriptados en GitHub
- Se inyectan solo al ejecutar el pipeline

### En desarrollo local

Crear archivo `.env.local` (está en `.gitignore`):

```bash
# .env.local
API_KEY=sk-test-1234567890
DATABASE_URL=localhost:5432
```

Cargar las variables:

```bash
export $(cat .env.local | xargs)
python src/app.py
```

### Buenas prácticas

- Usar secretos en CI/CD
-  Usar variables de entorno en desarrollo local
-  Rotar secretos regularmente
-  Nunca commitear `.env` o `.env.local`
-  Nunca hardcodear credenciales
