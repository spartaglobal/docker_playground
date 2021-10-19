from imdb_api.mongodb_utils.mongodb_conn import imdb_collection_mongodb_conn;


def find_films_rated_greater_than(imdb_score):
    return list(imdb_collection_mongodb_conn().find({"score": {"$gt": imdb_score}}, {'_id': False}))


def find_films_rated_less_than(imdb_score):
    return list(imdb_collection_mongodb_conn().find({"score": {"$lt": imdb_score}}, {'_id': False}))

