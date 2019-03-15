FROM python:3.7.2-alpine3.8
RUN apk update && apk upgrade && apk add bash
RUN pip install pytz
COPY . ./app
EXPOSE 80
WORKDIR ./app
CMD ["python3", "./serv.py"]