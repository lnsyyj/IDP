# IDP
Internal data processing

database:

    sudo yum install mariadb-server

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


    pip install wheel
    https://www.lfd.uci.edu/~gohlke/pythonlibs/
    pip install MySQL_python-1.2.5-cp27-none-win_amd64.whl


grafana:

    wget https://s3-us-west-2.amazonaws.com/grafana-releases/release/grafana-4.6.3-1.x86_64.rpm
    sudo yum install initscripts fontconfig urw-fonts -y
    sudo rpm -Uvh grafana-4.6.3-1.x86_64.rpm

    # start service
    systemctl daemon-reload
    systemctl start grafana-server
    systemctl status grafana-server
    sudo systemctl enable grafana-server.service

    # log location
    tailf /var/log/grafana/grafana.log

    # grafana configuration file position
    /etc/sysconfig/grafana-server
    /etc/grafana/grafana.ini