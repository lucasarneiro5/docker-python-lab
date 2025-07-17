#!/bin/sh

# Valores padrão caso variáveis não definidas
DB_HOST=${DB_HOST:-db}
DB_PORT=${DB_PORT:-5432}
TIMEOUT=${TIMEOUT:-30}  # segundos

echo "⏳ Aguardando PostgreSQL iniciar em $DB_HOST:$DB_PORT..."

start_time=$(date +%s)

while ! nc -z $DB_HOST $DB_PORT; do
  sleep 1
  now=$(date +%s)
  elapsed=$(( now - start_time ))
  if [ $elapsed -ge $TIMEOUT ]; then
    echo "❌ Timeout após $TIMEOUT segundos esperando o PostgreSQL"
    exit 1
  fi
done

echo "✅ PostgreSQL está pronto. Iniciando aplicação..."

exec "$@"
