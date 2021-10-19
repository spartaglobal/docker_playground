import pymongo.errors

from imdb_api.mongodb_utils.mongodb_conn import imdb_collection_mongodb_conn

try:
    imdb_collection_mongodb_conn().create_index([('title', 'text')], default_language='none', language_override="en")
except pymongo.errors.ServerSelectionTimeoutError:
    print("Connection to mongoDB refused - please check DB availability")
