# Ruby Docker Env

The aim of this docker container is to provide a basic ubuntu:xenial environment with the latest ruby version.

## Building the environment from the Dockerfile

To create this environment access the Dockerfile in this folder [or click here](https://github.com/spartaglobal/Docker_Playground/blob/master/Environments/Programming_Languages/Ruby/Dockerfile). Locally create a Dockerfile, copy and past the details and save.

Access the folder via the command line / terminal and type `docker build -t ubuntu/xenial .`.

Let's briefly break down the command:

`docker build` -> Is the command to begin to set up a container from a Dockerfile

`-t` -> Name and optionally a tag in the ‘name:tag’ format

`ubuntu/xenial` -> is the name of the base container we want to build from which will be pulled from the docker hub.

`.` -> the dot is stating to look in the current directory. If you wish you can state the absolute path of the Dockerfile you wish to run.

You should see the container start to build from the Dockerfile you have in your local directory some of the output should look as below:

```bash
Sending build context to Docker daemon  2.048kB
Step 1/7 : FROM ubuntu:xenial
xenial: Pulling from library/ubuntu
3620e2d282dc: Pull complete 
ef22f5e4b3b2: Pull complete 
99f229f854da: Pull complete 
4fe433abe16a: Pull complete 
c9b72a16d85e: Pull complete 
Digest: sha256:bad7847cac1e3e9a5821593b1e1e07729c37eaaec4edf44f4db89867212e61e5
Status: Downloaded newer image for ubuntu:xenial
 ---> e13f3d529b1a
Step 2/7 : MAINTAINER kcorn1982@gmail.com
 ---> Running in 7d1df54716ac
Removing intermediate container 7d1df54716ac
 ---> edaefcc72215
Step 3/7 : RUN mkdir /home/ruby
 ---> Running in edf3851efba2
Removing intermediate container edf3851efba2
 ---> 2a5bb7ce660f
Step 4/7 : RUN apt-get update && apt-get -y upgrade
``` 

Once the dockerfile has built the environment if you run `docker images` you should see the below:

```bash
REPOSITORY     TAG       IMAGE ID       CREATED         SIZE
ubuntu/xenial  latest    8a84a4ab0f57   19 minutes ago  192MB
```

## Running the container
We now need to run the container to create our ongoing development environment. We will build this using the below command:


`docker run -it --name rubyenv1  -v <input absolute path for your system>:/home/ruby -p 80:80 -p 8080:8080 -p 4567:4567 ubuntu/xenial /bin/bash`

As usual let's break down the command;

`docker run` -> command to define the container’s resources at runtime

`--name <container name>` -> If you do not assign a container name with the --name option, then the daemon generates a random string name for you. Defining a name can be a handy way to add meaning to a container.

`-v <local volume>:<docker volume>` This command exposes a local folder and the advice here would be to create a folder, commonly aligned to where you will manage your git project from, and align it to a folder within the container itself. which in turn means your can work locally and have these volumes mirror each other to then execute your code.

`-p 80:80` -> Using `-p` means you are exposing ports we have exposed via our Dockerfile and in this instance we're doing each one manually.

`ubuntu/xenial` -> We are building the container from our recently created ubuntu/xenial image. 

`/bin/bash` -> This command is optional but we are running our container with bash.

Once this has run you should see the root terminal `root@30d72b7991ea` or something similar. Let's run a few commands now to ensure your environment is running:

`ruby -v` should produce  `ruby 2.3.1p112 (2016-04-26) [x86_64-linux-gnu]`

`gem -v` should produce `2.5.2.1`

At this stage it would also be worth creating a file called `test.rb` within your mapped local folder and within this file type `puts "This is now working"` and save.

If we now access the /home/ruby folder in your docker image `cd /home/ruby` and type `ls` you should be able to see your `test.rb` file and by running `ruby test.rb` we should see your output of `"This is now working"`.
  