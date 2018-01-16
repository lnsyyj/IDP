# IDP
Internal data processing

database:

    sudo yum install mariadb-server
    mariadb-server-5.5.56-2.el7.x86_64
    mariadb-5.5.56-2.el7.x86_64
    mariadb-libs-5.5.56-2.el7.x86_64

    sudo systemctl start mariadb
	sudo systemctl status mariadb
	sudo systemctl enable mariadb

	sudo mysql_secure_installation

	mysqladmin -u root -p version

create database

    MariaDB [(none)]> CREATE DATABASE ceph CHARACTER SET = 'utf8' COLLATE = 'utf8_general_ci';
	MariaDB [(none)]> use ceph;


    SET FOREIGN_KEY_CHECKS=0;
    -- ----------------------------
    -- Table structure for stability
    -- ----------------------------
    DROP TABLE IF EXISTS `stability`;
    CREATE TABLE `stability` (
    `id` bigint(20) NOT NULL AUTO_INCREMENT,
    `datatime` datetime DEFAULT NULL,
    `interval` int(255) DEFAULT NULL,
    `iorate` double DEFAULT NULL,
    `MBsec` double(255,0) DEFAULT NULL,
    `bytesio` int(11) DEFAULT NULL,
    `readpct` double DEFAULT NULL,
    `resptime` double DEFAULT NULL,
    `readresp` double DEFAULT NULL,
    `writeresp` double(255,0) DEFAULT NULL,
    `respmax` double(255,0) DEFAULT NULL,
    `respstddev` double(255,0) DEFAULT NULL,
    `queuedepth` double(255,0) DEFAULT NULL,
    `cpupercentagesysu` double(255,0) DEFAULT NULL,
    `cpupercentagesys` double(255,0) DEFAULT NULL,
    `clustercapacitypercentage` double(11,0) DEFAULT NULL,
    PRIMARY KEY (`id`)
    ) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;