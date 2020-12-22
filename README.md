<p align="center">
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/johnvict0r/sistema-vacinas.svg">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/johnvict0r/sistema-vacinas.svg">
  
  <a href="https://github.com/johnvict0r/sistema-vacinas./commits/master">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/johnvict0r/sistema-vacinas.svg">
  </a>

  <a href="https://github.com/johnvict0r/sistema-vacinas./issues">
    <img alt="Repository issues" src="https://img.shields.io/github/issues/johnvict0r/sistema-vacinas.svg">
  </a>

  <img alt="License" src="https://img.shields.io/badge/license-MIT-brightgreen">
</p>

<p align="center">
  <a href="#rocket-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-projeto">Projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-layout">Layout</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-como-contribuir">Como contribuir</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#memo-licença">Licença</a>
</p>

<br>

<p align="center">
  <img alt="Frontend" src=".github/sistema-vacinas-web.png" width="100%">
</p>

## :rocket: Tecnologias

Esse projeto foi desenvolvido com as seguintes tecnologias:

- [Django](https://www.djangoproject.com)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [React](https://reactjs.org)

## 💻 Projeto

Elaborar uma aplicação que consiste em uma carteira digital de vacinação integrada com as redes de atenção à saúde, onde o usuário do Sistema Único de Saúde (SUS) poderá realizar o autocadastro e ser vacinado em qualquer estabelecimento de
saúde que tenha disponibilidade de vacinas.

## Configuração

Clone o projeto e execute os seguintes comandos:

```shell
$ git clone [(https://github.com/JohnVict0r/sistema-vacinas.git)](https://github.com/JohnVict0r/sistema-vacinas.git)
$ cd sistema-vacinas
$ pip install -r requirements.txt
$ cp .env.example .env
$ python manage.py migrate
$ python manage.py importar_municipios_ibge
$ python manage.py runserver
```

Altere o arquivo .env com suas configurações locais, como por exemplo, as informações do banco de dados (DB_HOST, DB_NAME, DB_USERNAME, DB_PASSWORD, etc)

Inicie o servidor e acesse o sistema 🤞🙏⏱👍

## 🤔 Como testar

- [Cartão de vacina digital - Frontend](https://cartao-de-vacinas-digital.netlify.app/)
- Usuário(Gestor do SUS): Administrador do Django
- Usuário(Profissional de saúde): profissional e senha: pteste123
- Usuário(Paciente): teste e senha: 12345678

## 🤔 Como contribuir

- Faça um fork desse repositório;
- Cria uma branch com a sua feature: `git checkout -b minha-feature`;
- Faça commit das suas alterações: `git commit -m 'feat: Minha nova feature'`;
- Faça push para a sua branch: `git push origin minha-feature`.

Depois que o merge da sua pull request for feito, você pode deletar a sua branch.

## :memo: Licença

Esse projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE.md) para mais detalhes.

---

Feito com ♥ by John Victor ☕ Code and coffee
