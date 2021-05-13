# Docker Ping Service and Health Service
 
 Swagger Documentation have been created with the help of flask microservices 
 ## 1. PingService
  It exposes 2 APIs one for ping request and another for health
  Below are the snaps for Ping Service:-

  ![img_3.png](img_3.png)

  ![img_4.png](img_4.png)

 ## 2. ReceiverService
  Receiver Service only exposes hardcode ```/info``` api.

  ![img_5.png](img_5.png)

 ## 3. Health
  Checks docker health status

  ![img_6.png](img_6.png)


To run the app:
-git clone repo
-docker-compose up --build
-open the browser and hit the url http://localhost:8080/ and you will see swagger documentation.