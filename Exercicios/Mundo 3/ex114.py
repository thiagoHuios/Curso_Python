import requests

url = "https://www.pudim.com.br"

response = requests.get(url)

if response.status_code == 200:
    print("O site está acessivel!")
else:
    print("O site está fora do ar!")
    print(f"Falha ao acessar o site. Status Code: {response.status_code}")


