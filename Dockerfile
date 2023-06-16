FROM python:3-alpine
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . ./
EXPOSE 8081
ENTRYPOINT ["python3", "prova.py"]

