FROM python:3.12-rc-bullseye
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src/* /app/
EXPOSE 8080
ENTRYPOINT ["python3", "typing_test.py"]