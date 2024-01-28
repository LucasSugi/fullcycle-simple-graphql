FROM python:3.8-slim-buster
COPY requirements.txt .
RUN pip install -r requirements.txt
WORKDIR /app
COPY /api /app/api
COPY /graphql /app/graphql
COPY app.py /app
CMD ["tail", "-f"]
