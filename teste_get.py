import requests

headers = {'Authorization': 'Token 135352990f33ce437d993c94e891fc76e26e3cd4'}
url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'


resultado = requests.get(url=url_base_cursos, headers=headers)

# print(resultado.json())


# Testando se o endpoint está correto
assert resultado.status_code == 200

# Testando a quantidade de registros
assert resultado.json()['count'] == 3

# Testar tipo estados BR-
