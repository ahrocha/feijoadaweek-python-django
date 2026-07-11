FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        default-libmysqlclient-dev \
        pkg-config \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip \
    && pip install -r /app/requirements.txt

#ARG ENV_FILE=.env.production
#COPY ${ENV_FILE} /app/.env
# Declara os argumentos que serão recebidos durante o build
ARG DB_HOST
ARG DB_PASSWORD

# Define as variáveis de ambiente que a aplicação Django/PHP lerá em runtime
ENV DB_HOST=${DB_HOST}
ENV DB_PASSWORD=${DB_PASSWORD}

COPY . /app

RUN chmod +x /app/start.sh

EXPOSE 8080

CMD ["/app/start.sh"]