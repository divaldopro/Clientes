FROM python:3

WORKDIR /usr/src/app

COPY requeriments.txt ./
RUN pip install --no-cache-dir -r requeriments.txt

COPY . .

EXPOSE 80

CMD [ "fastapi", "run", "main.py", "--port", "80" ]
