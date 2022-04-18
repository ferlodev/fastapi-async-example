
docker run -it mysql mysql -hsome-mysql -uexample-user -p

docker run --name my-mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root00 -d mysql:5.7

docker pull mariadb


sudo docker run -d -p 3306:3306 --name my-mariadb --env MARIADB_USER=dev --env MARIADB_PASSWORD=dev00 --env MARIADB_ROOT_PASSWORD=root00  mariadb:10.7


sudo docker run --name my-redis -p 6379:6379 -d redis:6.2
