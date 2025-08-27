#!/bin/bash

set -euo pipefail

python manage.py check --database default >/dev/null 2>&1 || true

if [[ "${AUTO_MIGRATE:-1}" = "1" ]]; then
  echo ">> Aplicando migrações..."
  python manage.py migrate --noinput
else
  echo ">> AUTO_MIGRATE=0 -> pulando migrações."
fi

# Coleta os arquivos estáticos
echo ">> Coletando arquivos estáticos..."
python manage.py collectstatic --noinput

# Inicia o servidor com Gunicorn
echo ">> Iniciando aplicação com Gunicorn..."
gunicorn feijoadaweek.wsgi:application --workers 4 --bind 0.0.0.0:8080 --limit-request-field_size 16384
