FROM python:3.11-slim

RUN apt-get update && apt-get install -y  build-essential curl gcc git && apt-get clean

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

EXPOSE 80

# ENV PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION python

CMD ["uvicorn", "app.main:app","--host", "0.0.0.0", "--reload", "--reload-dir", "app", "--port", "80"]
