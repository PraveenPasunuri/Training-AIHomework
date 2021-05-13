# Example of Dockerfile

FROM python:3.8.5-alpine3.12

WORKDIR /app

EXPOSE 8080
ENV FLASK_APP=main.py

COPY . /app
RUN pip install -r requirements.txt

ENTRYPOINT [ "flask"]
HEALTHCHECK --interval=10s --timeout=10s --start-period=55s \
   CMD curl -f --retry 10 --max-time 15 --retry-delay 10 --retry-max-time 60 "http://localhost:8080/" || exit 1   

CMD [ "run", "--host", "0.0.0.0", "--port",  "8080"]
