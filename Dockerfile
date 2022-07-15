FROM python:3.10.5
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD python main.py