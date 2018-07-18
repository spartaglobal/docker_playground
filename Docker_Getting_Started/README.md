# Docker Getting Started

Docker is a huge topic and has an incredible amount of uses. This getting started guide aims to help you get Docker installed, a container downloaded and running your first container. 

## Docker Platform

Before moving forward with the next steps it would be important to read the information in order as below to help get a picture of what Docker can provide:

1. [Docker Overview -> Link to Docker docs](https://docs.docker.com/engine/docker-overview/) -
2. What is Docker and the benefit -> Video coming soon

## Installing Docker

All the information needed to install Docker can be found [here](https://docs.docker.com/install/).


## Your first container

To get a feel for Docker as a whole we will simply install the Docker hello-world container and run that container.

**Important** -> At this point you should have Docker installed on your machine based on the instructions linked above.

####Getting the hello-world container

to begin let's check that Docker is installed by running:  

`docker` This should produce a long list of possible docker commands you could also run `docker -v` which should show you the version of docker installed.

First of all let's check if we have any containers installed locally by using `docker images` which will hopefully bring up:

```bash
REPOSITORY    TAG     IMAGE ID     CREATED     SIZE
```
this means we have no containers at present so let's run `docker pull hello-world` which should produce:

```bash
Using default tag: latest
latest: Pulling from library/hello-world
9db2ca6ccae0: Pull complete
Digest: sha256:4b8ff392a12ed9ea17784bd3c9a8b1fa3299cac44aca35a85c90c5e3c7afacdc
Status: Downloaded newer image for hello-world:latest
```
Now if we run our `docker images` we should now see:

```bash
REPOSITORY    TAG         IMAGE ID       CREATED      SIZE
hello-world   latest      2cb0d9787c4d   6 days ago   1.85kB
```
#### Running the container

Now we need to run the container which can be done by running `docker run hello-world` which should produce:

```bash
Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/engine/userguide/
```
As you can see this container has simply been built to echo the message above and then shuts itself down.

## Summary

By following the basic instructions above you have hopefully now installed docker, pulled your first container and run it. explore the environments and instructions throughout this project to begin learning.