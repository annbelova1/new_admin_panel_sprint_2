FROM python:3.10

WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt'


COPY . .

EXPOSE 8000

ENTRYPOINT ["uwsgi", "--strict", "--ini", "uwsgi.ini"]
