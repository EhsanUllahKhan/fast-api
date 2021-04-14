FROM python:3.8
COPY . /app
WORKDIR /app
RUN pip install fastapi[all] pymysql python-dotenv sqlalchemy alembic
EXPOSE 8000
# Create the tables
CMD ["alembic" ,"upgrade", "head"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
