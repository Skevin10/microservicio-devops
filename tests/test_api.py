import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from app import app
import json

def test_health():
    """Test endpoint /health"""
    client = app.test_client()
    response = client.get('/health')
    
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['status'] == 'ok'
    assert data['container'] == 'python'

def test_version():
    """Test endpoint /version"""
    client = app.test_client()
    response = client.get('/version')
    
    assert response.status_code == 200
    data = json.loads(response.data)
    # Cambiar de 'version' a 'versionContainerPython'
    assert 'versionContainerPython' in data

if __name__ == '__main__':
    test_health()
    test_version()
    print("✓ All tests passed")