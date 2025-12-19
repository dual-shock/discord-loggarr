

FROM python:3-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV HOST-PORT=12345
ENV CONTAINER-PORT=8080
ENV PYTHONUNBUFFERED=1

EXPOSE 8080

CMD ["python", "testing.py"]