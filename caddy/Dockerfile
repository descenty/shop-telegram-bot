FROM caddy:latest
FROM python:3.11

RUN pip install python-dotenv

COPY build_caddyfile.py .

RUN python build_caddyfile.py

COPY Caddyfile /etc/caddy/Caddyfile