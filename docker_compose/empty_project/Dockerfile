FROM python:latest
# RUN apk --no-cache add curl

WORKDIR /code
RUN groupadd -r web && useradd -d /code -r -g web web \
    && chown web:web -R /code
# COPY requirements.txt .
# RUN pip3 install -r requirements.txt
# COPY . .
USER web
# ENTRYPOINT [...]
EXPOSE 8000/tcp

CMD ["python3", "-m", "http.server", "8000"]