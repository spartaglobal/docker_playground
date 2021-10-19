FROM python:alpine3.9

WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "app:app"]