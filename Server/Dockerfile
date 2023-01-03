FROM python:latest

EXPOSE  8000
WORKDIR /usr/app/src

COPY BankWebServices.py ./BankWebServices.py
COPY database.py ./database.py

RUN pip3 install spyne
RUN pip3 install psycopg2
RUN pip3 install lxml