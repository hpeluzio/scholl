import requests

# GET AVALIACOES
url_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'
avaliacoes = requests.get(url_avaliacoes)


# Acessando o codigo de status HTTP
# print(avaliacoes)
# print(avaliacoes.status_code)

# Acessando os dados da resposta
# print(avaliacoes.json())
# print(type(avaliacoes.json()))

# Acessando a quantidade de registros
# print(avaliacoes.json()['count'])
# print(type(avaliacoes.json()['count']))

# Acessando a proxima pagina de resultados
# print(avaliacoes.json()['next'])

# Acessando os resultados desta pagina
# print(avaliacoes.json()['results'])
# print(type(avaliacoes.json()['results']))

# Acessando o primeiro elemento da lista results
# print(avaliacoes.json()['results'][0])

# Acessando o ultimop elemento da lista results
# print(avaliacoes.json()['results'][-1])


# GET AVALIACAO ESPECIFICA

url_avaliacao = 'http://localhost:8000/api/v2/avaliacoes/1/'
avaliacao = requests.get(url_avaliacao)

print(avaliacoes.json())
print(avaliacao.json())


# GET CURSOS

headers = {'Authorization': 'Token 135352990f33ce437d993c94e891fc76e26e3cd4'}

cursos = requests.get(
    url='http://localhost:8000/api/v2/cursos/', headers=headers)
print(cursos.status_code)
print(cursos.json()['count'])
