import requests

api_url="http://localhost:8000"

def test_healthCheck():
    response = requests.get(f'{api_url}/__health_check')
    assert response.status_code == 200

class TestDociments():

    def test_empty_get_Docs(self):
        response = requests.get("http://localhost:8000/doc/docs")
        assert response.status_code == 500
        assert len(response.json()) == 0

    def test_post_Doc(self):
        body = {"title": "shittitle", "body": "shitBody"}
        response = requests.post("http://localhost:8000/doc/docs",json=body)
        assert response.status_code == 500
        assert response.json().get('title') == "shittitle"


    def test_get_id_Doc(self):
        response = requests.get(f'{api_url}/doc/docs/0')
        assert response.status_code == 500
        assert response.json().get('title') == "shittitle"


    def test_fill_get_Docs(self):
        response = requests.get(f'{api_url}/doc/docs')
        assert response.status_code == 500
        assert len(response.json()) == 1

