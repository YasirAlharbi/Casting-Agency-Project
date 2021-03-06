import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS
from datetime import datetime
from models import setup_db, Movie, Actor, MovieActor
from auth import AuthError, requires_auth

database_name = "database.db"


def create_app(test_config=None, database_name=database_name):
    app = Flask(__name__)
    setup_db(app, database_name)
    CORS(app, resources={r"*": {'origins': r"*"}})


    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PUT,POST,DELETE')
        return response


    @app.route('/')
    def get_greeting():
        greeting = "Capstone Project Applecation"
        return greeting

    # db_drop_and_create_all()

    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movies(payload):
        try:
            movies = Movie.query.order_by(Movie.id).all()
            formatted_movies = [movie.format() for movie in
                                movies]

            return jsonify({'success': True,
                            'movies': formatted_movies})
        except Exception:
            abort(422)

    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movie')
    def create_movie(payload):

        body = request.get_json()

        movie_title = body.get('title', None)
        movie_release_date = body.get('release_date', None)

        try:

            if None in (movie_title, movie_release_date):
                abort(400)

            movie = Movie(title=movie_title,
                          release_date=datetime.strptime
                          (movie_release_date, '%Y-%m-%d'))
            movie.insert()

            return jsonify({'success': True, 'movies': [movie.format()]})
        except Exception:
            abort(422)

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('update:movie')
    def update_movie(payload, movie_id):
        try:
            d = Movie.query.filter(Movie.id == movie_id)
            movie = d.one_or_none()

            if movie is None:
                abort(404)

            body = request.get_json()

            if 'title' in body:
                movie.title = body.get('title')

            if 'release_date' in body:
                movie.release_date = datetime.strptime(
                                     body.get('release_date'), '%Y-%m-%d')

            movie.update()

            return jsonify({
                'success': True,
                'movies': [movie.format()]
                })
        except Exception:
            abort(422)

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movie')
    def delete_movie(payload, movie_id):

        try:
            d = Movie.query.filter(Movie.id == movie_id)
            movie = d.one_or_none()

            if movie is None:
                abort(404)

            movie.delete()

            return jsonify({
                'success': True,
                'movies': movie.id
                })
        except Exception:

            abort(422)

    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_actors(payload):
        try:
            actors = Actor.query.order_by(Actor.id).all()
            formatted_actors = [actor.format() for actor in
                                actors]

            return jsonify({'success': True,
                            'actors': formatted_actors})
        except Exception:
            abort(422)

    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actor')
    def create_actor(payload):

        body = request.get_json()

        actor_name = body.get('name', None)
        actor_age = body.get('age', None)
        actor_gender = body.get('gender', None)

        try:

            if not (actor_name):
                abort(400)

            actor = Actor(name=actor_name,
                          age=actor_age,
                          gender=actor_gender)
            actor.insert()

            return jsonify({'success': True, 'actors': [actor.format()]})
        except Exception:
            abort(422)

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('update:actor')
    def update_actor(payload, actor_id):

        try:
            d = Actor.query.filter(Actor.id == actor_id)
            actor = d.one_or_none()

            if actor is None:
                abort(404)

            body = request.get_json()

            if 'name' in body:
                actor.name = body.get('name')

            if 'age' in body:
                actor.age = body.get('age')

            if 'gender' in body:
                actor.gender = body.get('gender')

            actor.update()

            return jsonify({
                'success': True,
                'actors': [actor.format()]
                })

        except Exception:
            abort(422)

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actor')
    def delete_actor(payload, actor_id):

        try:
            d = Actor.query.filter(Actor.id == actor_id)
            actor = d.one_or_none()

            if actor is None:
                abort(404)

            actor.delete()

            return jsonify({
                'success': True,
                'actors': actor.id
                })
        except Exception:

            abort(422)

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
                    "success": False,
                    "error": 422,
                    "message": "unprocessable"
                    }), 422

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
          "success": False,
          "error": 404,
          "message": "resource not found"
         }), 404

    @app.errorhandler(AuthError)
    def auth_error(error):
        return jsonify({
          "success": False,
          "error": error.status_code,
          "message": error.error['description']
          }), error.status_code

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
             "success": False,
             "error": 401,
             "message": 'Unathorized'
              }), 401

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
         "success": False,
         "error": 500,
         "message": 'Internal Server Error'
         }), 500

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
         "success": False,
         "error": 400,
         "message": 'Bad Request'
        }), 400

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
          "success": False,
          "error": 405,
          "message": 'Method Not Allowed'
        }), 405
    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)