import requests

headers = {'Authorization': 'Token 11beaa3b865e223f79d1de5c7764194fd12c1e83'}
url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'


novo_curso = {
  "titulo": "testesss",
  "url": "http://www.googasasle.com.br"
}

resultado = requests.post(url=url_base_cursos, headers=headers, data=novo_curso)
print(resultado.json())

# Testando o codigo de status HTTP 201
assert resultado.status_code == 201

# Testando se o titulo do curso retornado eh o mesmo do informado
assert resultado.json()['titulo'] == novo_curso['titulo']