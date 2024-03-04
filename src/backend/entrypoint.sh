#!/bin/sh

HOST=${HOST:-0.0.0.0}
PORT=${PORT:-80}

python manage.py run -h $HOST -p $PORT