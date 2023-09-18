-- Creates replica_user which can be used for dangeours act on database server

CREATE USER IF NOT EXISTS 'replica_user'@'%' IDENTIFIED BY 'hbtn89';
GRANT REPLICATION CLIENT, REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;
