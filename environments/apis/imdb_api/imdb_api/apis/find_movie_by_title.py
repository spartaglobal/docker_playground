from flask_restx import Namespace, Resource, fields, reqparse
from imdb_api.mongodb_utils.imdb_queries.find_movie_by_title_query import find_movie_by_title

api = Namespace('search-movie-title', description='Search film word in title, the search is not case sensitive but must be full words i.e. no fuzzy matching')
parser = reqparse.RequestParser()


@api.route('/')
@api.param('title-word', 'Word to search movie titles - example url localhost/search-movie-title/?title-word=batman', "query")
@api.doc('search-movie-title')
class SearchMovieTitle(Resource):
    def get(self):
        """Will search for a specific word in a film title and return all relating films"""
        parser.add_argument('title-word', required=True, help='cannot be blank')
        return find_movie_by_title(parser.parse_args()['title-word'])
