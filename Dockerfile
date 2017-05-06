FROM python:3.4

WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
CMD python main.py
