## Slack todo App for mark and list Work

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


***functionality***

* /addtodo taskName (add task in the channel list)
* /markdown taskName (mark the task complete and remove the task form database)
* /listtodo [prefix(optional)] (list down all the task of channel or if prefix is given list task for that prefix )

Go through the structure of the project 

logic is in api layer (i.e. views.py) and all the business logic is in the service layer (i.e. user_service.py).
Schema goes in the models/*.py file.

Refer docstrings in the above mentioned files and function 

***Improvement or Suggestion***

As of now I am using Flask and mongodb as server and database respectively , this require a compute unit for all the time 

* Instead of compute unit we can user Lambda or serverless as a api endpoint this will reduce the cost and complexity
* Any Simple dataStore to hold value like dynamoDb or s3 

