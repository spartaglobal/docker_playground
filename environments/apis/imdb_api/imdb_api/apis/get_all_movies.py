from flask_restx import Namespace, Resource
from imdb_api.mongodb_utils.imdb_queries.get_all_movies_query import get_all_movies

api = Namespace('all-movies', description='get all movies')


@api.route('/')
class AllMovies(Resource):
    @api.doc('all-movies')
    def get(self):
        """List all Movies from the IMDB data collection"""
        return get_all_movies()
