# Exemplo de um projeto simples de uma API Rest em Python utilizando Flask, 
com persistência de dados em um banco de dados relacional MySql, 
realizando requisições através da biblioteca Requests e 
criação de dados para testes com a biblioteca Faker.

* Banco de Dados MySql para persistência dos dados, criação de um CRUD em python 
  para manipular os dados;

* API com os métodos GET, POST, PUT e DELETE implementados;

* Automatização das requisições na API usando a biblioteca Requests;

* Criação de um dataset de users para testes utilizando a biblioteca Faker.


## Sobre a aplicação

* Utilizando o script *generate_users.py* é possível gerar uma lista com múltiplos usuários
  através da biblioteca Faker;
  
* O arquivo *api_requests.py* contém uma séria de funções para realizar requisições na api
  utilizando a biblioteca Requests;  
  
* No arquivo *user_dao* estão as funções necessárias para criação e manipulação do banco de
  dados relacional MySql.


Alguns end-points da aplicação:

### Obter JSON contendo todos os users

'''
$ curl -v http://127.0.0.1:5000/users
'''

### Adcionar novo user

'''
$ curl -i -H "Content-Type: application/json" 
    -X POST -d '{"username":"test", "email":"test@email.com", "password":"test123"}' 
    http://127.0.0.1:5000/users
'''




