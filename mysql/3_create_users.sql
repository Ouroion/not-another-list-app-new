CREATE USER 'dev'@'%' IDENTIFIED WITH mysql_native_password BY 'developer';
ALTER USER 'dev'@'%' IDENTIFIED WITH mysql_native_password BY 'developer';
GRANT ALL PRIVILEGES ON *.* TO 'dev'@'%';

FLUSH PRIVILEGES;
