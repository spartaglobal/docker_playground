<img src="https://boolerang.co.uk/wp-content/uploads/job-manager-uploads/company_logo/2018/04/SG-Logo-Black.png" alt="Sparta Logo" width="200"/>

---

# IMDB API

# Contents
* [The aim of this API](#the-aim-of-this-api)
* [How to use this environment](#how-to-use-this-environment)
  * [Setup with docker-compose](#setup-with-docker-compose)
  * [Building directly from this project](#building-directly-from-this-project)
* [API Response Structure](#api-response-structure)
* [Endpoints](#endpoints)



# The aim of this API

The core aim of this API is to provide an environment for an exposed API and an exposed database to be able to practice with things like:

* Consuming from an API for a front end website
* Building data injected test frameworks to validate  the correct information is being exposed

This API has been built to connect and expose data from this training database [mongoDB Seeded DB](https://github.com/spartaglobal/docker_playground/tree/master/environments/databases/mongoseed).

# How to use this environment

### Setup with docker-compose
The easiest way to use this service is to create a docker-compose.yml file as below:

```yaml
version: '3'

services:
  imdb_api:
    image:  spartagl/imdb-api:latest
    ports:
      - '5000:5000'
    depends_on:
      - mongoDB_seed
    links:
      - mongoDB_seed
  mongoDB_seed:
    image: spartagl/mongoseed:latest
    ports:
      - '27017:27017'
```

This will automatically set up the environment for you with the api exposed on `localhost:5000` and you will be able to connect to the mongoDB instance using the details which can be found [here](https://github.com/spartaglobal/docker_playground/tree/master/environments/databases/mongoseed).

### Building directly from this project

If you have cloned this repository you can simply run the `docker-compose.yml` by simply using your IDE or running the below in the command line:

* `docker-compose up`

# The IMDB-API

Swagger documentation on the end points can be found at the base url of `localhost:5000` although they will be documented in this README as well.

## API Response Structure
all responses will be returned in a JSON array/list.

Each individual film repsonse will be structured as below:

```json
{
  "title": String,
  "score": Float,
  "year": String,
  "duration": Integer,
  "rating": String,
  "budget": Integer,
  "genres": String Array/List,
  "gross": Integer,
  "director": String,
  "actors": String Array/List,,
  "language": String,
  "country": String
},
```
Example output

```json
[
    {
        "title": "Pirates of the Caribbean: At World's End",
        "score": 7.1,
        "year": "2007",
        "duration": 169,
        "rating": "PG-13",
        "budget": 300000000,
        "genres": [
            "Action",
            "Adventure",
            "Fantasy"
        ],
        "gross": 309404152,
        "director": "Gore Verbinski",
        "actors": [
            "Johnny Depp",
            "Orlando Bloom",
            "Jack Davenport"
        ],
        "language": "English",
        "country": "USA"
    },
    {
        "title": "John Carter",
        "score": 6.6,
        "year": "2012",
        "duration": 132,
        "rating": "PG-13",
        "budget": 263700000,
        "genres": [
            "Action",
            "Adventure",
            "Sci-Fi"
        ],
        "gross": 73058679,
        "director": "Andrew Stanton",
        "actors": [
            "Daryl Sabara",
            "Samantha Morton",
            "Polly Walker"
        ],
        "language": "English",
        "country": "USA"
    }
]
```


## Endpoints
* `localhost:5000/all-movies` Returns all records/movies available
* `localhost:5000/search-movie-title?title-word=batman` -> search Movie title for a specific word in movie titles
  * query param `title-word` as in the example above
  * **NOTE** - must be a full matching word as there is no fuzzy logic search at the moment
* `localhost:5000/search-movie-score/?<lower or great than param>=score` -> Returns all films relating to the IMDB score
  * `localhost:5000/search-movie-score/?score-lt=2` -> return all films with a score lower than 2
  * `localhost:5000/search-movie-score/?score-gt=9` -> return all films with a score greater than 9




