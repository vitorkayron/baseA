## Instruções para rodar a aplicação

### Pré Requisitos

- É necessário ter instalado o Docker na sua máquina

### Passo a passo para rodar a aplicação

1 - Clone o repositório

#### Na raiz do projeto, execute o seguinte comando para construir as imagens Docker:

2 - docker-compose up -d --build 

#### Execute as migrações do Django para criar as tabelas do banco de dados:

3 - docker-compose exec web python manage.py migrate 

#### Crie um superusuário para acessar a aplicação:

4 - docker-compose exec web python manage.py createsuperuser

5 - Após criar o superuser, vá para http://127.0.0.1:8000/api/token/

6- Coloque seu usuario e senha para obter o token

7- Depois de obter o seu token, você pode fazer o login

Será necessário fazer o login em http://127.0.0.1:8000/admin

E depois poderá acessar os endpoints

#### Documentação da api com endpoints podem ser acessadas em:

- /Swagger/ - Documentação da API usando o Swagger UI;
- /Redoc/  - Documentação da API usando o ReDoc.
