from flask_restx import Namespace, Resource, reqparse
from imdb_api.mongodb_utils.imdb_queries.find_by_score_query import find_films_rated_less_than, find_films_rated_greater_than

api = Namespace('search-movie-score', description='Search for movies based on their scores')
parser = reqparse.RequestParser()

@api.route('/')
@api.param('score-gt', 'return all films with a score greater than - example url localhost/search-movie-score/?score-gt=8', "query")
@api.param('score-lt', 'return all films with a score less than - example url localhost/search-movie-score/?score-lt=6', "query")
@api.doc('search-movie-score')
class SearchMovieScore(Resource):
    def get(self):
        parser.add_argument('score-gt', required=False, help='cannot be blank')
        parser.add_argument('score-lt', required=False, help='cannot be blank')

        if parser.parse_args()['score-gt'] is not None:
            return find_films_rated_greater_than(int(parser.parse_args()['score-gt']))
        elif parser.parse_args()['score-lt'] is not None:
            return find_films_rated_less_than(int(parser.parse_args()['score-lt']))

