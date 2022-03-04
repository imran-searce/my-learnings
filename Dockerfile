FROM python:3
WORKDIR /app
COPY requirements.txt  app.py ./
RUN pip install -r requirements.txt
#COPY /app .
EXPOSE 5000
CMD ["python3", "app.py"]
