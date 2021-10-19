from imdb_api.mongodb_utils.mongodb_conn import imdb_collection_mongodb_conn


def get_all_movies():
    return list(imdb_collection_mongodb_conn().find({}, {'_id': False}))

