from imdb_api.config.config_manager import MONGODB_CONN_STRING, MONGODB_IMDB_DB, MONGODB_IMDB_COLL
import pymongo


def imdb_collection_mongodb_conn():
    try:
        return pymongo.MongoClient(MONGODB_CONN_STRING, serverSelectionTimeoutMS=5000)[MONGODB_IMDB_DB][MONGODB_IMDB_COLL]
    except ConnectionError:
        print("Unable to connect to MongoDB IMDB collection.")
