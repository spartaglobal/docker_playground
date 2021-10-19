from imdb_api.mongodb_utils.mongodb_conn import imdb_collection_mongodb_conn


def find_movie_by_title(film_title):
    # Must be a full word as mongoDB does not support partial text searches from an index
    return list(imdb_collection_mongodb_conn().find({"$text": {"$search": film_title,
                                                          "$caseSensitive": False,
                                                          "$diacriticSensitive": False}
                                                }, {'_id': False}))



