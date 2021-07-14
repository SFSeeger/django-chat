FROM python:3
ENV redis_ip=channels_db my_sql_ip=db
WORKDIR /code
COPY requirements.txt /code
RUN pip install -r requirements.txt
COPY . /code/
EXPOSE 8000
#bind to port 0.0.0.0 insead of 127.0.0.1
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
