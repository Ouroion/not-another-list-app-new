#!/bin/bash

container_name="natl_mysql"
database_name="natl"
echo "Database Container: ${container_name}"

docker run \
    -e "MYSQL_ROOT_PASSWORD=developer" \
    -p 3306:3306 \
    -d \
    --name=${container_name} mysql/mysql-server:latest-aarch64

#echo "Run the following commands inside the docker container"
#echo "CREATE USER ‘dev’@’%’ IDENTIFIED BY ‘developer’;"
#echo "GRANT ALL ON *.* TO ‘dev’@’%’;"

container_id=$(docker ps -aqf "name=natl_mysql")
echo "Database Container Id: ${container_id}"

docker cp create_users.sql ${container_id}:/
docker cp create_database.sql ${container_id}:/
docker cp create_test_data.sql ${container_id}:/


sleep 15
docker exec -it natl_mysql mysql --user=root --password=developer -e "source /create_users.sql"
docker exec -it natl_mysql mysql --user=root --password=developer -e "source /create_database.sql"
docker exec -it natl_mysql mysql --user=root --password=developer -e "source /create_test_data.sql"

