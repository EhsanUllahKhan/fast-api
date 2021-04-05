FROM python:3.8
RUN pip install fastapi[all] pymysql python-dotenv
COPY . /app
CMD ["uvicorn", "./fast-api/main:app", "--host", "0.0.0.0", "--port", "15400"]
