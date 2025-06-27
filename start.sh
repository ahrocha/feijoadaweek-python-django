#!/bin/bash

# Coleta os arquivos estáticos
echo ">> Coletando arquivos estáticos..."
python manage.py collectstatic --noinput

# Inicia o servidor com Gunicorn
echo ">> Iniciando aplicação com Gunicorn..."
gunicorn feijoadaweek.wsgi:application --workers 4 --bind 0.0.0.0:8080 --limit-request-field_size 16384
