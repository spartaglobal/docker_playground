FROM mongo

WORKDIR /

COPY data/* /
COPY seed.sh /docker-entrypoint-initdb.d/
ENV MONGO_INITDB_ROOT_USERNAME=root
ENV MONGO_INITDB_ROOT_PASSWORD=password