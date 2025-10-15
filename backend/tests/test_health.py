import requests

def test_health_endpoint():
    """Verifica se o endpoint /health está respondendo corretamente."""
    url = "http://127.0.0.1:8000/health"
    response = requests.get(url)
    
    assert response.status_code == 200, "A API não retornou status 200"
    data = response.json()
    
    assert "status" in data, "A resposta não contém o campo 'status'"
    assert data["status"] == "ok", "O status da API não é 'ok'"
    
    print("✅ Teste /health passou com sucesso!")
    
if __name__ == "__main__":
    test_health_endpoint()
