# Usando uma imagem oficial do Python como base
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos de dependências e instala
RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante da aplicação
COPY app/ .

# Copia variáveis de ambiente (se necessário)
COPY .env .

# Copia o script de espera e dá permissão
COPY app/wait_for_postgres.sh .
RUN chmod +x wait_for_postgres.sh

# Expõe a porta 8000
EXPOSE 8000

# Comando padrão (vai ser sobrescrito no docker-compose)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
