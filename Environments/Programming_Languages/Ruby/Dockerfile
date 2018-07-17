FROM ubuntu:xenial
MAINTAINER kcorn1982@gmail.com

RUN mkdir /home/ruby

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y ruby
RUN gem install bundler

EXPOSE 80 8080 4567