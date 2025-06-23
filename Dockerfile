FROM python:3.13

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.s

CMD ["python","main.py"]