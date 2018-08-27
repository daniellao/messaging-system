FROM python:3.6.4
RUN mkdir /demoCA
WORKDIR /demoCA
RUN mkdir certs private
RUN chmod g-rwx,o-rwx private
RUN echo '01' > serial
RUN touch index.txt
RUN openssl req -x509 -newkey rsa -out cacert.pem -outform PEM -subj "/C=NL/L=Eindhoven/CN=localhost" -passout pass:root
ADD . /app
VOLUME /app
WORKDIR /app
RUN pip install -e git://github.com/requests/requests.git#egg=requests --src ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["./wait-for-it.sh", "redis0:6379", "--", "python", "app.py"]
