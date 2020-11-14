# Programa em Python que utiliza Web Scraping para rastrear encomendas dos Correios
# ao inserir um código de rastreamento.

import requests
from bs4 import BeautifulSoup

print('#######################################')
print('###########CORREIOS TRACKING###########')
print('#######################################')
print('Descrição: Este programa rastreia encomendas dos Correios utilizando Web Scraping')
print()

#Bloco de preparação da URL para o Beautiful Soup
codigo = str(input('Digite corretamente o código de rastreamento: '))
url = 'https://www.linkcorreios.com.br/?id=' + codigo
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

#Bloco de busca e exibição dos elementos HTML contendo a informação relevante da página.
print()
print('Histórico do Objeto:')
elementos = soup.find('div', class_ = 'singlepost').find_all('ul', class_ = 'linha_status')
for ul in elementos:
    print(ul.text)
    print('-'*60)

#Loop utilizado para escolher se deve salvar o resultado ou não
while True:
    salvar = input('Deseja salvar o resultado? (s/n) ')
    if salvar == 's':
        f = open('results.txt','w')
        for ul in elementos:
            f.write(ul.text)
            f.write('\n')
            f.write('-'*40)
        f.close()
        break
    elif salvar == 'n':
        break
    else:
        print('Resposta inválida. Responda apenas s ou n.')