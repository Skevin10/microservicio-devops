from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"}), 200

@app.route('/version', methods=['GET'])
def version():
    app_version = os.getenv('APP_VERSION', '1.0.0')
    return jsonify({"version": app_version}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
