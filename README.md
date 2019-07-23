## Assignment for Instahyre

***Code Navigation***

This project consists of a main folder `src` which contains all the project files. The files outside the source folder consists of `docker-compose.yml`, `Dockerfile` and a `local.env` file which are used for running the docker containers. The `src` folder contains the entrypoint of the Flask project `app.py`, `settings` folder which contains your application settings and an `apis` folder that stores all your urls and views.

Specify the urls in `urls.py` file in the api folder as list of tuples with following format:

    (endpoint, view_func, methods, description)
example:

    ("/", views.index, ["GET"], "index page")



To run both the server run for Flask and MongoDb

    sudo docker-compose build
and then

    sudo docker-compose up
This will run the server at port http://localhost:8400/

The index view will be displayed in your browser.


***The Assignment and APIs***


1.User Register \
2.User Searching<p>
	2.1 By Name 	 multiple responces auto and relevant maching \
	2.2 By Phone No    only single responce \
3.Spam adding \
4.View User Profile  
5.Login Of User Done Needs Cleaning 

Go through the structure of the project 

logic is in api layer (i.e. views.py) and all the business logic is in the service layer (i.e. user_service.py).
Schema goes in the models/*.py file.

Refer docstrings in the above mentioned files and function 
