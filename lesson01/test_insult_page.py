import requests

class TestInsultPage:
    def test_generate_insult(self):
        responce = requests.get("https://evilinsult.com/")
        assert responce.status_code == 200, "Запрос на получение оскорбления сломан"
        print(responce.text)
