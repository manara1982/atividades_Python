import requests
from bs4 import BeautifulSoup

# URL da página da Wikipedia que queremos extrair informações
url = 'https://pt.wikipedia.org/wiki/Python_(linguagem_de_programa%C3%A7%C3%A3o)'

# Enviar requisição HTTP
response = requests.get(url)

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    # Extrair o conteúdo HTML da página
    html_content = response.text

    # Criar um objeto BeautifulSoup para analisar o HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Encontrar o título da página
    title = soup.find('h1', class_='firstHeading').text.strip()

    # Encontrar o primeiro parágrafo da página
    first_paragraph = soup.find('div', class_='mw-parser-output').p.text.strip()

    # Imprimir o título e o primeiro parágrafo
    print('Título: ', title)
    print('Primeiro parágrafo: ', first_paragraph)
else:
    print('Não foi possível acessar a página.')
