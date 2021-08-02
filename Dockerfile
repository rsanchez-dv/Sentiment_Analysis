FROM python:3.9.1
ADD . /python-flask
WORKDIR /python-flask
EXPOSE 5000
RUN pip install -r requirements.txt
CMD ["python", "flaskapp.py"]