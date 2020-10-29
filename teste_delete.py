import requests

headers = {'Authorization': 'Token 11beaa3b865e223f79d1de5c7764194fd12c1e83'}
url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'



resultado = requests.delete(url=f'{url_base_cursos}4/', headers=headers)

# Testando codigo HTTP
assert resultado.status_code == 204

# Testando se o tamanho do conteudo retorno é 0
assert len(resultado.text) == 0