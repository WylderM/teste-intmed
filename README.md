# teste-intmed

# Preparação de Ambiente

## 1. Usando Docker

### Clonado o repositório
``` bash
git clone https://github.com/WylderM/teste-intmed.git
```

### Iniciando o banco de dados e a aplicação com docker
```
Após clonar o projeto, navegue até a raiz da pasta "BACKEND" lá terá os arquivos docker para inicialização da aplicação. 
Com bash/cmd, use o comando abaixo para inicializar a aplicação:   

docker-compose up --build


Obs: Esse comando irá baixar todas as dependências necessárias para rodar o projeto, e irá construir um banco de dados local pra aplicação. 
```

Acesse a aplicação em [http://localhost:8000](http://localhost:8000).

### Migre o banco de dados

``` 
Navegue até a raiz da pasta "BACKEND" e digite os seguintes comandos abaixo: 

docker-compose exec web /code/eureca_core/manage.py createcachetable
docker-compose exec web /code/eureca_core/manage.py migrate
```
#ou

```
docker exec -it <container_id> /bin/sh
cd intmed
python manage.py createcachetable
python manage.py migrate
```

### Crie um user super admin
```
docker-compose exec web /code/intmed/manage.py createsuperuser

Username: admin

Email address: admin@intmed.com

Password: admin@2023

acesse: http://localhost:8000/admin
```
