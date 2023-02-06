# teste-intmed

# Preparação de Ambiente

## 1. Usando Docker

### Clonado o repositório
``` bash
git clone https://github.com/WylderM/teste-intmed.git
```

### Iniciando o banco de dados e a aplicação
``` bash/cmd
docker-compose up --build
```

Acesse a aplicação em [http://localhost:8000](http://localhost:8000).

### Migre o banco de dados
``` 
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

docker-compose exec web /code/intmed/manage.py createsuperuser

Username: admin

Email address: admin@intmed.com

Password: admin@2023

acesse: http://localhost:8000/admin
