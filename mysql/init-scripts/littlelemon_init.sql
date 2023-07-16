/* To init the root password to mysql native password */
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root@123';

FLUSH PRIVILEGES;

/* Create the database */
CREATE DATABASE IF NOT EXISTS `little_lemon` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

/* Create an little_lemon db admin user */
CREATE USER 'admin'@'localhost' IDENTIFIED BY 'admin@123';

ALTER USER 'admin'@'localhost' IDENTIFIED WITH mysql_native_password BY 'admin@123';

/* Assign privileges to the little_lemon db admin user */
GRANT ALL PRIVILEGES ON `little_lemon`.* TO 'admin'@'localhost';

FLUSH PRIVILEGES;

