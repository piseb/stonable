FROM python:3.12.3 AS python
EXPOSE 8000
WORKDIR /app
COPY requirements.txt .
RUN pip install -U pip setuptools
RUN pip install --no-cache-dir -r requirements.txt
COPY app .
ENTRYPOINT ["python3"] 
CMD ["manage.py", "runserver", "0.0.0.0:8000"]
