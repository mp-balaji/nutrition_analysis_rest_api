FROM python:3.11-alpine

WORKDIR /app

COPY . /app

RUN apk --no-cache add bash

RUN chmod +x setup.sh migrate.sh run.sh

RUN ./setup.sh

EXPOSE 5000

CMD ["./run.sh"]
