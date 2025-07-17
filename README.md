# 🐳 docker-python-lab

Projeto-laboratório que demonstra o uso do **FastAPI** com **PostgreSQL** e **Docker**, incluindo todas as operações REST (GET, POST, PUT, DELETE), com persistência real em banco de dados e integração via `docker-compose`.

---

## 📦 Tecnologias Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Uvicorn](https://www.uvicorn.org/)
- [psycopg2](https://pypi.org/project/psycopg2/)

---

## 🚀 Como Executar o Projeto

### Pré-requisitos

- Docker e Docker Compose instalados
- Git Bash ou terminal compatível com shell script (`wait_for_postgres.sh`)

### 1. Clone o repositório

```bash
git clone https://github.com/lucasarneiro5/docker-python-lab.git
cd docker-python-lab
```

### 2. Suba os containers

```bash
docker-compose up --build
```

O script `wait_for_postgres.sh` irá aguardar o PostgreSQL iniciar antes de iniciar a aplicação FastAPI.

### 3. Acesse a API

- Acesse a raiz: http://localhost:8000
- Documentação automática Swagger: http://localhost:8000/docs
- Alternativa ReDoc: http://localhost:8000/redoc

---

## 📂 Estrutura do Projeto

```
docker-python-lab/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── database.py
│   ├── crud.py
│   ├── schemas.py
│   ├── routes.py
│   └── __init__.py
├── init.sql
├── wait_for_postgres.sh
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
└── README.md
```

---

## 🔌 Exemplos de uso

### Criar um registro (POST)

```bash
curl -X POST http://localhost:8000/itens      -H "Content-Type: application/json"      -d '{"nome": "Sensor", "descricao": "Dispositivo IoT", "preco": 199.99}'
```

### Listar todos os itens (GET)

```bash
curl http://localhost:8000/itens
```

### Atualizar um item (PUT)

```bash
curl -X PUT http://localhost:8000/itens/1      -H "Content-Type: application/json"      -d '{"nome": "Sensor atualizado", "descricao": "Versão 2.0", "preco": 249.90}'
```

### Deletar um item (DELETE)

```bash
curl -X DELETE http://localhost:8000/itens/1
```

---

## 🧪 Testes

Você pode adicionar testes utilizando `pytest`. Um exemplo básico está na pasta `tests/`.

```bash
pip install pytest
pytest tests/
```

---

## 🛠️ Comandos Docker úteis

| Comando | Descrição |
|--------|-----------|
| `docker-compose up --build` | Builda e sobe os containers |
| `docker-compose down` | Derruba os serviços |
| `docker ps` | Lista containers ativos |
| `docker exec -it fastapi-container bash` | Acessa o terminal do container da API |
| `docker exec -it postgres-container psql -U user -d mydatabase` | Abre o terminal PostgreSQL dentro do container |

---

## 📌 Observações

- O script `init.sql` é executado automaticamente no primeiro build para criar a estrutura do banco.
- O `wait_for_postgres.sh` evita que a API tente conectar ao banco antes dele estar pronto.

---

## 👨‍💻 Autor

**Lucas Arneiro Vieira**  
🔗 [linkedin.com/in/lucasarneiro](https://www.linkedin.com/in/lucasarneiro/)  
📬 lucasarneiro5@gmail.com  

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.