import requests

class TestCursos: #IMPORTANTE COMECAR CLASSE COM 'Test'

  headers = {'Authorization': 'Token 11beaa3b865e223f79d1de5c7764194fd12c1e83'}
  url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
  
  curso_id_criado = 11

  novo = {
    "titulo": "curso12345",
    "url": "https://www.curso12345.aa.com"
  }

  atualizado = {
    "titulo": "curso12345",
    "url": "http://www.curso12345.com.br"
  }


  #
  def test_get_cursos(self): #IMPORTANTE COMECAR METODOS COM 'test'
    print('HUEHUEHUEHUEHEHU')
    print('HUEHUEHUEHUEHEHU')
    print('HUEHUEHUEHUEHEHU')
    print('HUEHUEHUEHUEHEHU')
    cursos = requests.get(url=self.url_base_cursos, headers=self.headers)

    print('curso criado: ', self.curso_id_criado)

    assert cursos.status_code == 200
    self.curso_id_criado =2

  #
  def test_get_curso(self):
    curso = requests.get(url=f'{self.url_base_cursos}1/', headers=self.headers)

    print('curso criado: ', self.curso_id_criado)

    assert curso.status_code == 200



  #
  def test_post_curso(self):

    resposta = requests.post(url=self.url_base_cursos, headers=self.headers, data=self.novo)

    assert resposta.status_code == 201
    assert resposta.json()['titulo'] == self.novo['titulo']
    
    if resposta.status_code == 201:
      self.curso_id_criado = resposta.json()['id']


  #
  def test_put_curso(self):

    # print(f'{self.url_base_cursos}{self.curso_id_criado}/')
    resposta = requests.put(url=f'{self.url_base_cursos}{self.curso_id_criado}/', headers=self.headers, data=self.atualizado)

    assert resposta.status_code == 200
    assert resposta.json()['titulo'] == atualizado['titulo']



  #
  def test_delete_curso(self):
    resposta = requests.delete(url=f'{self.url_base_cursos}{self.curso_id_criado}/', headers=self.headers)

    assert resposta.status_code == 204 and len(resposta.text) == 0
