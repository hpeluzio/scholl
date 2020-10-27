import requests

# GET AVALIACOES
url_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'
avaliacoes = requests.get(url_avaliacoes)


#Acessando o codigo de status HTTP
#print(avaliacoes)
#print(avaliacoes.status_code)

#Acessando os dados da resposta
print(avaliacoes.json())
# print(type(avaliacoes.json()))