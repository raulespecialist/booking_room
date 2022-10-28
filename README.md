# Resume

This repository is backend API using Django. This API will be used to manage a small business that is focused on renting different rooms for events.


# Implementation
![Graphic description](https://user-images.githubusercontent.com/54911620/198419624-96162dbe-5660-4ecd-9c11-b271a3eeb57c.png)

### Description
Because of the flexibility offered by the framework. We will use Django as a base for our project, since we have the opportunity to use its MVC systems for Frontend and Backend, as well as having the possibility to extend it with a REST API system or extend it with any of the Python libraries, From filtered , partitioning, joins and even advanced PostgreSQL search functions.

I chose PostgreSQL as it has an emphasis on extensibility and standards compliance. It is chosen because it complies with the ACID characteristic and protocol, which means Atomicity, Consistency, Isolation and Durability (acronym in English). Therefore, the information in the database and the reliability of the system are guaranteed. Django would be served via Gunicorn.

Gunicorn is a pure Python WSGI server for UNIX. It has no dependencies and is easy to install and use, it is the industry standard "classic" Python production server. The final advantage of using Gunicorn is that it is by nature quite fast plus coupled with NGINX as a reverse proxy and load balancer to manage incoming traffic and distribute it to slower upstream servers, from legacy database servers to microservices, for example. which is ideal to use in front of Gunicorn.

 Docker is a platform created in order to develop, deploy and run applications within containers, which allows us to encapsulate our application and its services, to help both replication and high availability.

### Install
The installation is done by docker-compose.

    https://github.com/raulespecialist/booking_room.git
    cd booking_room
    docker-compose up

To start using the app, five users have been created from the dockerfile entrypoint.

| user | password |
|-------|-------|
| admin | TestPass3 |
| business1 | TestPass3 |
| business2 | TestPass3 |
| customer1 | TestPass3 |
| customer2 | TestPass3 |


## URLS endpoints

To enter the navigable Root Api http://127.0.0.1:8000/api/v1/

To view or create Rooms http://127.0.0.1:8000/api/v1/room/

To view or create Events http://127.0.0.1:8000/api/v1/event/

To view or create Books http://127.0.0.1:8000/api/v1/book/

## Explanation
To create rooms and events, which can only be done by users of type **'Business'** enter as follows with some of the 'business' users (business1 or business2)

#### First login button

![login-drf](https://user-images.githubusercontent.com/54911620/198420773-d3976136-9c7e-42a6-b276-96fd8a309367.png)
#### Form login

![login-drf1](https://user-images.githubusercontent.com/54911620/198420771-d336663c-9165-4c2b-9201-5b079f4d5430.png)
#### Login success

![login-drf2](https://user-images.githubusercontent.com/54911620/198420768-95244806-69b1-483c-a013-c82da27c3e81.png)


Below each endpoint there is a form to test the POST methods, and DELETE in your case. You can play with them.



