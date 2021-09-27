FROM python:3-alpine
WORKDIR /service
COPY rq.txt .
RUN pip install -r rq.txt
COPY . ./
EXPOSE 8080
ENTRYPOINT ["python3", "mainapp.py"]