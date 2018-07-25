FROM ubuntu:xenial
MAINTAINER kcorn1982@gmail.com

RUN mkdir /home/ruby
COPY pg_hba.conf /tmp/pg_hba.conf
EXPOSE 80 8080 4567 3000

RUN apt-get update && apt-get -y upgrade
RUN apt-get install sudo -y

RUN sudo apt-get install postgresql postgresql-contrib -y
RUN cat /tmp/pg_hba.conf > /etc/postgresql/9.5/main/pg_hba.conf
RUN service postgresql start &&\
    sudo -u postgres psql postgres --c "UPDATE pg_database SET datistemplate = FALSE WHERE datname = 'template1';" &&\
    sudo -u postgres psql postgres --c "DROP DATABASE template1;" &&\
    sudo -u postgres psql postgres --c "CREATE DATABASE template1 WITH TEMPLATE = template0 ENCODING = 'UNICODE';" &&\
    sudo -u postgres psql postgres --c "UPDATE pg_database SET datistemplate = TRUE WHERE datname = 'template1';" &&\
    sudo -u postgres psql postgres --c "\c template1" &&\
    sudo -u postgres psql postgres --c "VACUUM FREEZE;" &&\
    sudo -u postgres psql postgres --c "\q"

RUN apt-get install -y ruby
RUN gem install bundler
RUN sudo apt-get install build-essential patch ruby-dev zlib1g-dev liblzma-dev -y
RUN sudo apt-get install libsqlite3-dev -y
RUN sudo apt-get install nodejs -y
RUN sudo apt-get install libpq-dev -y
RUN gem install rails
