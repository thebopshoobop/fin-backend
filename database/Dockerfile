FROM postgres

# run create.sql on init
ADD create.sql /docker-entrypoint-initdb.d

# switch to postgres user
USER postgres
