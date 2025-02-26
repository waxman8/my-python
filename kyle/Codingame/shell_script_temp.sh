


podman run --name postgresml -e POSTGRES_USER=username -e POSTGRES_PASSWORD=password -p 5433:5432 -v postgresml_data:/var/lib/postgresql -d ghcr.io/postgresml/postgresml:2.7.12 sudo -u postgresml psql -d postgresml


docker run \
    -it \
    -v postgresml_data:/var/lib/postgresql \
    -p 5433:5432 \
    -p 8000:8000 \
    ghcr.io/postgresml/postgresml:2.7.12 \
    sudo -u postgresml psql -d postgresml