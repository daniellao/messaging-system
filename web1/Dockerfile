FROM python:3.6.4
COPY . /app
WORKDIR /app
VOLUME /app
RUN pip install -r requirements.txt
CMD ["./wait-for-it.sh", "redis0:6380", "--", "python", "app.py"]
