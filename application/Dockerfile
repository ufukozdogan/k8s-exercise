#Getting the slimmest image possible in order to achieve lowest Docker image size.
FROM python:3.10-alpine3.15
WORKDIR /app

COPY . .
RUN pip3 install -r requirements.txt
#Installing the requirements for application. Couple of packages probably can be crossed-out.

ENV FLASK_APP=server.py
# Standard Flask environment.

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]