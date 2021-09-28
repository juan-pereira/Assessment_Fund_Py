import requests
from bs4 import BeautifulSoup

url = "https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html"

html = requests.get(url).text
soup = BeautifulSoup(html,"lxml")

estado = input("Insira a sigla do estado: ")

if (estado == "GO") | (estado == "MT") | (estado == "MS") | (estado == "DF"):
  for div in soup.html.body.find_all("div", "linha"):
    print(div.text)
else:
  print("Estado não pertecente ao Grupo Selecionado")