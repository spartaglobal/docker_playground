from definitions import ROOT_DIR
import configparser

__config = configparser.ConfigParser()
__config.read(ROOT_DIR + '/imdb_api/config/config.ini')

MONGODB_CONN_STRING = __config['mongo_config']['mongo_imdb_conn_string']
MONGODB_IMDB_DB = __config['imdb_data']['imdb_db']
MONGODB_IMDB_COLL = __config['imdb_data']['imdb_collection']

if __name__ == '__main__':
    print(MONGODB_CONN_STRING)