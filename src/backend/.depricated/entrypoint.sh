#!/bin/sh

HOST=${HOST:-0.0.0.0}
PORT=${PORT:-80}

python3 main.py run -h $HOST -p $PORT