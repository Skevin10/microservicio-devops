from flask import Flask, jsonify
import os

# Inicializa la app Flask
app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    """
    Ruta de comprobacion de estado Healthcheck
    Devuelve un estado 'ok' para indicar que el servidor esta en línea.
    """
    return jsonify({
        "status": "ok",
        "container": "python"
    }), 200

@app.route('/version', methods=['GET'])
def version():
    """
    Ruta para obtener la versioon de la app
    Lee la variable de entorno 'APP_VERSION'.
    """
    # Si no se encuentra la variable de entorno, usa '1.0.0' por defecto
    app_version = os.getenv('APP_VERSION', '1.0.0')
    return jsonify({"versionContainerPython": app_version}), 200

if __name__ == '__main__':
    # Ejecuta el servidor en todas las interfaces (0.0.0.0) a traves del puerto 8080
    app.run(host='0.0.0.0', port=8080, debug=False)
