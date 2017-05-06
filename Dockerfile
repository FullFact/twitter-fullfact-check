FROM python:3.4

ADD .
RUN pip install -r requirements.txt
CMD python main.py
