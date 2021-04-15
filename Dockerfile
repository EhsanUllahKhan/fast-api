# FROM python:3.8

# # FROM mysql:5.7
# COPY . /app
# WORKDIR /app
# RUN pip install fastapi[all] pymysql python-dotenv sqlalchemy alembic
# # CMD [ "" ]
# EXPOSE 8000
# # Create the tables
# # CMD ["alembic" ,"upgrade", "head"]
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
FROM python:3.8

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app/

# Install dependencies
RUN pip install fastapi[all] pymysql python-dotenv sqlalchemy alembic

COPY . /app/
RUN chmod 644 main.py
EXPOSE 8000
