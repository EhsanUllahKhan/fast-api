FROM python:3.8
COPY . /app
WORKDIR /app
RUN pip install fastapi[all] pymysql python-dotenv sqlalchemy 
ENTRYPOINT [ "uvicorn" ]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
