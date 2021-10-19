from flask_restx import Api

from imdb_api.apis.get_all_movies import api as get_all_movies
from imdb_api.apis.find_movie_by_title import api as find_movie_by_title
from imdb_api.apis.search_movies_based_on_score import api as search_movies_based_on_scores

api = Api(
    title='IMDB Api',
    version='1.0',
    description='An api surfacing approx 3,700 + movies',
)

api.add_namespace(get_all_movies)
api.add_namespace(find_movie_by_title)
api.add_namespace(search_movies_based_on_scores)