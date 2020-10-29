import requests

headers = {'Authorization': 'Token 11beaa3b865e223f79d1de5c7764194fd12c1e83'}
url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'


curso_atualizado = {
    "titulo": "curso_atuzalizado_Teste",
    "url": "http://www.googasasaasle.com.br"
}


# buscando o curso com id 4
curso = requests.get(url=f'{url_base_cursos}4/', headers=headers)
print(curso.json())
#
resultado = requests.put(
    url=f'{url_base_cursos}4/', headers=headers, data=curso_atualizado)
# print(resultado.status_code)
assert resultado.status_code == 200
# print(resultado.json())
