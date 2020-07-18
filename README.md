Full Stack Trivia API Backend

Introduction
Casting-Agency is the fifth and the final project in Udacity nanodgree. It models a company that is responsible for creating movies and managing and assigning actors to those movies. The user can intract with the database useing the API to prform CRUD .The user must have permissions to prform these oparation.the permissions are manged by Auth0.

The API is doploued in Heroku in the folowing base URL :

https://capstone-fsndd.herokuapp.com/
Getting Started
If you want to run the API localy, folow the instraction.

Installing Dependencies
Python 3.7
Follow instructions to install the latest version of python for your platform in the python docs

Virtual Enviornment
We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the python docs

PIP Dependencies
Once you have your virtual environment setup and running, install dependencies by naviging to the /fsnd-capstone directory and running:

pip install -r requirements.txt
This will install all of the required packages we selected within the requirements.txt file.

Running the server
From within the fsnd-capstone directory first ensure you are working using your created virtual environment.

To run the server, execute:

source  setup.sh
python app.py
setup.sh have the variable needed to run and test the app.

Testing
you can test the endpoint using Unittest or Postman.

Unittest
tests for the endpoint are in test_app.py

first you neeed to create a database and name it 'database_test'
To run the tests, run

python test_app.py
Postman
To test the endpoint in Heroku :

download Postmant.
Import Casting-Agency.postman_collection.json .
run the collection.
API Reference
Geting Starting
Base URL:this app can be run locally using the base URL as http://127.0.0.1:5000/,or you can use hosted URL https://capstone-fsndd.herokuapp.com/
Authentication: This version of the application does not have frontend to authnticate users , to use the endpoints you need to provaied a valid Bearer access token,given in setup.sh


Error Handling
Errors are returned as JSON objects in the following format:

{
"success": False,
"error": 400,
"message": "bad request"
}
The API will return three error types when requests fail:

400: Bad Request
401: Unauthorized
404: Resource Not Found
405: Method Not Allowed
422: Not Processable

500: Internal Server Error

End Points
The folowing tests will assume that the access token is porvided with each requaset body in the form:

"Authorization": "Bearer {access_token}".
Actors
GET /actors
General:
Returns a list of actors objects , success value and the number of actors
Sample: curl https://capstone-fsndd.herokuapp.com/actors

{
    "actors": [
        {
            "birth_year": "2002",
            "gender": "f",
            "id": 1,
            "name": "Actor One"
        },
        {
            "birth_year": "1995",
            "gender": "m",
            "id": 2,
            "name": "Actor Two"
        },
        {
            "birth_year": "1998",
            "gender": "m",
            "id": 3,
            "name": "Actor Three"
        }
    ],
    "success": true,
    "total_actors": 3
}
POST /actors
General:
Creates a new actor using the provided name, birth_year and gender. Returns an array contans the actor created and success value.
curl https://capstone-fsndd.herokuapp.com/actors -X POST -H "Content-Type: application/json" -d '{ "name": "Added Actor", "birth_year": 100, "gender": "m" }'

{
    "actors": [
        {
            "birth_year": "1999",
            "gender": "m",
            "id": 6,
            "name": "Added Actor"
        }
    ],
    "success": true
}
PATCH /actors/{int:actor_id}
General:
modify the actor with the id = actor_id using the provided name, birth_year or gender. Returns an array contans the actor modified and success value.
curl https://capstone-fsndd.herokuapp.com/actors/5 -X PATCH -H "Content-Type: application/json" -d '{ "name": "Edited Actor", "gender": "m" }'

{
    "actors": [
        {
            "birth_year": "1980",
            "gender": "f",
            "id": 5,
            "name": "edited actor"
        }
    ],
    "success": true
}
DELETE /actors/{int:actor_id}
General:
Deletes the actors with the provided ID .Returns an array contans the actor and success value.
curl https://capstone-fsndd.herokuapp.com/movies/5 -X DELETE -H "Content-Type: application/json"

{
    "deleted": [
        {
            "birth_year": "200",
            "gender": "f",
            "id": 5,
            "name": "edited actor"
        }
    ],
    "success": true
}
Movie
GET /movie
General:
Returns a list of movie objects , success value and the number of movies
Sample: curl https://capstone-fsndd.herokuapp.com/movies

{
    "movies": [
        {
            "id": 1,
            "release_date": "Mon, 18 Apr 1999 00:00:00 GMT",
            "title": "The sun"
        },
        {
            "id": 2,
            "release_date": "Fri, 21 Jan 2002 00:00:00 GMT",
            "title": "Amazing"
        },
        {
            "id": 3,
            "release_date": "Wed, 14 Nov 2015 00:00:00 GMT",
            "title": "Salt"
        }
    ],
    "success": true,
    "total_movies": 3
}
POST /movies
General:
Creates a new actor using the provided name, birth_year and gender. Returns an array contans the actor created and success value.
curl https://capstone-fsndd.herokuapp.com/movies -X POST -H "Content-Type: application/json" -d '{ "title": "added movie", "release_date": "2001-11-15" }'

{
    "movies": [
        {
            "id": 4,
            "release_date": "Thu, 15 Nov 2001 00:00:00 GMT",
            "title": "movie added"
        }
    ],
    "success": true
}
PATCH /movies/{int:movie_id}
General:
modify the movie with the id = movie_id using the provided release_date or title. Returns an array contans the movie modified and success value.
curl https://capstone-fsndd.herokuapp.com/movies/4 -X PATCH -H "Content-Type: application/json" -d '{ "title": "edited movie", "release_date": "2002-02-01" }'

{
    "movies": [
        {
            "id": 4,
            "release_date": "Sat, 01 Feb 2002 00:00:00 GMT",
            "title": "edited movie"
        }
    ],
    "success": true
}
DELETE /movies/{int:movie_id}
General:
Deletes the movie with the provided ID .Returns an array contans the movie and success value.
curl https://capstone-fsndd.herokuapp.com/movie/4 -X DELETE -H "Content-Type: application/json"

{
    "deleted": [
        {
            "id": 4,
            "release_date": "Sat, 01 Feb 3000 00:00:00 GMT",
            "title": "edited movie"
        }
    ],
    "success": true
}
Actors in a Movie
GET /movies/{int:movie_id}/actors
General:
Returns a list of actors objects assgined to a movie with id = to movie_id, success value and the number of actors
Sample: curl https://capstone-fsndd.herokuapp.com/movies/2/actors

{
    "actors": [
        {
            "birth_year": "1998",
            "gender": "m",
            "id": 3,
            "name": "Actor Three"
        }
    ],
    "success": true,
    "total_actors": 1
}
POST /movies/{int:movie_id}/actors
General:
assgin the actor with the id provided to the movie with the id = movie_id . Returns an array contans the actor assgined and success value.
curl https://capstone-fsndd.herokuapp.com/movies/2/actors -X POST -H "Content-Type: application/json" -d '{ "actor_id": "1" }'

{
    "actors": [
        {
            "birth_year": "2002",
            "gender": "f",
            "id": 1,
            "name": "Actor One"
        }
    ],
    "success": true
}
DELETE /movies/{int:movie_id}/actors
General:
remove the actor with the id provided from working in the movie with the id = movie_id . Returns an array contans the actor removed and success value.
curl https://capstone-fsndd.herokuapp.com/movies/2/actors -X DELETE -H "Content-Type: application/json" -d '{ "actor_id": "1" }'

{
    "actors": [
        {
            "birth_year": "2002",
            "gender": "f",
            "id": 1,
            "name": "Actor One"
        }
    ],
    "success": true
}