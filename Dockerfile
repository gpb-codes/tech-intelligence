# Tech Intelligence — imagen del collector
FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PYTHONPATH=/app

WORKDIR /app

# Git para el versionado automático del Vault
RUN apt-get update \
    && apt-get install -y --no-install-recommends git \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml README.md ./
COPY app ./app
COPY config ./config

# PYTHONPATH=/app + la instalación del paquete garantizan que
# el código se ejecute desde /app (config/settings.yaml resuelto ahí)
RUN pip install --no-cache-dir .

# Directorios de estado (montados como volúmenes)
RUN mkdir -p /app/vault /app/database /app/logs

COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["scheduler"]