<img src="https://boolerang.co.uk/wp-content/uploads/job-manager-uploads/company_logo/2018/04/SG-Logo-Black.png" alt="Sparta Logo" width="200"/>

# MongoDB Seeded Database

This image has been set up to provide various data collections to allow you to access and practice against a seeded, local MongoDB instance.


**CONTENTS**
* [Running the container](#running-the-container)
* [Connecting to the DB](#connecting-to-the-db)
* [MongoDB Compass](#mongodb-compass)
  * [MongoDB filter queries](#mongodb-filter-queries)
* [Available collections](#available-collections)
  * [IMDB Data Structure](#imdb-data-structure)
  * [Quiz Data Structure](#quiz-data-structure)
  * [User data structure](#user-data-structure)
  * [Student details data structure](#student-details-data-structure)



# Running the container

The below snippet will get the container up and running locally:

`docker run -d --name <name_your_container> -p 27017:27017 spartagl/mongoseed`

# Connecting to the DB

The DB credentials are as below:

Username = root
password = password

Whether using code or an app such as mongoDB Compass (See below) you will need to connect to the DB using the below connection string:

`mongodb://root:password@localhost:27017`

## MongoDB Compass

To interact with the data within the seeded MongoDB instance you can use mongoDB Compass which can be downloaded from [here](https://www.mongodb.com/try/download/compass).

Once you have mongoDB Compass installed you will need to input the connection string stated above.

![](img/mongoDB_conn.png)

You should then see the available databases:

![](img/mongoDB_dbs.png)

Select a database, and you will then see the available collection:

![](img/collection.png)

Once you click on the collection you will be able to view the objects available:

![](img/data.png)

You will also see the filter bar where you can begin writing queries too return specific objects:

![](img/filter.png)

## MongoDB filter queries
The documentation at [docs.mongodb.com](https://docs.mongodb.com/compass/current/query/filter/) are a great place to start learning about filter queries.

# Available collections
At the moment there are 4 different databases that contain collections:
* DB -> imdb; collection -> movies
* DB -> quiz ; collection -> quiz_questions
* DB -> random_user_details; collection -> user_details
* DB -> students; collection -> student_data

for both the `student_data` and `user_details` the data has been randomly generated. The `imdb` and `quiz` data have been taken from public sources.


## IMDB Data Structure

```json
 {
  "title": "Avatar",
  "score": 7.9,
  "year": "2009",
  "duration": 178,
  "rating": "PG-13",
  "budget": 237000000,
  "genres": [
    "Action",
    "Adventure",
    "Fantasy",
    "Sci-Fi"
  ],
  "gross": 760505847,
  "director": "James Cameron",
  "actors": [
    "CCH Pounder",
    "Joel David Moore",
    "Wes Studi"
  ],
  "language": "English",
  "country": "USA"
}
```

## Quiz Data Structure
***IMPORTANT NOTE*** - there are many areas within the data with unicode in place of certain characters. These are in place on purpose to practice data transformation. 
```json
{
      "category": "Entertainment: Video Games" ,
      "type": "multiple" ,
      "difficulty": "easy" ,
      "question": "What is the name of &quot;Team Fortress 2&quot; update, in which it became Free-to-play?" ,
      "correct_answer": "&Uuml;ber Update" ,
      "incorrect_answers": [
        "Pyromania Update" ,
        "Mann-Conomy Update" ,
        "Engineer Update"
      ]
    }
```

## User data structure

```json
{
  "id": 1,
  "first_name": "Flory",
  "last_name": "Boffey",
  "email": "fboffey0@pen.io",
  "company_name": "Lind Inc",
  "company_city": "Askiz",
  "job_title": "Information Systems Manager",
  "linkedIn_skill": "Access Control"
}
```

## Student details data structure

```json
{
  "first_name": "kara",
  "last_name": "darcey",
  "gender": "Gender Fluid",
  "email": "kara.darcey-71355@hotmail.com",
  "phone_number": "+447774443947",
  "current_status": "In Post Graduate Study",
  "university": "Aberystwyth University",
  "graduation_year": "2020",
  "degree": "business and tourism management with foundation year london",
  "visa": "No"
}
```
