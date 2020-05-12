# Dockerfile - this is a comment. Delete me if you want.

FROM python:3.6-alpine
COPY . /microblog

WORKDIR /microblog

RUN pip install -r requirements.txt
ENV FLASK_APP microblog.py

EXPOSE 5000
ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]
