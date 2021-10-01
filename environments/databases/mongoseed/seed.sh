#!/bin/sh
mongoimport --db students --collection student_data --type json --file /student_data.json --jsonArray
mongoimport --db random_user_details --collection user_details --type json --file /user_data.json --jsonArray
mongoimport --db imdb --collection movies --type json --file /imdb.json --jsonArray
mongoimport --db quiz --collection quiz_questions --type json --file /quiz.json --jsonArray