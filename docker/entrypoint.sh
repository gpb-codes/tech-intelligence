#!/bin/sh
# Entrypoint del contenedor collector.
# Comando por defecto: scheduler. También permite: sync, collect, health, etc.
set -e

if [ "$1" = "scheduler" ]; then
    shift
    exec tech-intelligence scheduler "$@"
fi

exec tech-intelligence "$@"