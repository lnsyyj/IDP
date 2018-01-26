#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ..commons.config import *
from datetime import datetime
from ..commons.config import *
import MySQLdb

def mariadb_connect_test():
    db = MySQLdb.connect(get_mysql_ip(),get_mysql_account(),get_mysql_password(),get_mysql_db_name())
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print "Database version : %s " % data
    db.close()

def mariadb_insert_stability_vdbench_data(data, file_name):
    db = MySQLdb.connect(get_mysql_ip(), get_mysql_account(), get_mysql_password(), get_mysql_db_name())
    dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print dt
    cursor = db.cursor()
    # sql = "INSERT INTO stability(id, datatime, outputinterval, iorate, MBsec, bytesio, readpct, resptime, readresp, writeresp, respmax, respstddev, queuedepth, cpupercentagesysu, cpupercentagesys, clustercapacitypercentage, operationtabledate) \
    #       VALUES ( NULL, '%s', '%d', '%f', '%f', '%d', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%s' )" % \
    #       (data[0] + " " + data[1], int(data[2]), float(data[3]), float(data[4]), int(data[5]), float(data[6]), float(data[7]), float(data[8]), float(data[9]), float(data[10]), float(data[11]), float(data[12]), float(data[13]), float(data[14]), 30,dt)
    sql = "INSERT INTO stability(id, datetime, outputinterval, iorate, MBsec, bytesio, readpct, resptime, readresp, writeresp, respmax, respstddev, queuedepth, cpupercentagesysu, cpupercentagesys, clustercapacitypercentage, operationtabledate, testcase) \
              VALUES ( NULL, '%s', '%d', '%f', '%f', '%d', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%s', '%d')" % \
          (data[0] + " " + data[1], int(data[2]), float(data[3]), float(data[4]), int(data[5]), float(data[6]),
           float(data[7]), float(data[8]), float(data[9]), float(data[10]), float(data[11]), float(data[12]),
           float(data[13]), float(data[14]), get_s3_directory_percentage(), dt, int(file_name))
    try:
        print sql
        cursor.execute(sql)
        db.commit()
    except NameError, msg:
        print msg
        db.rollback()
    db.close()

def mariadb_insert_system_monitor_data(data):
    db = MySQLdb.connect(get_mysql_ip(), get_mysql_account(), get_mysql_password(), get_mysql_db_name())
    dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print dt
    cursor = db.cursor()
    sql = "INSERT INTO system_monitor(id, datetime, machineid, cpu_used_percentage, mem_used_percentage, operationtabledate) \
              VALUES ( NULL, '%s', '%d','%f', '%f', '%s')" % \
          ( data[1] + " " + data[2], int(data[0]), float(data[3]), float(data[4]), dt)
    try:
        print sql
        cursor.execute(sql)
        db.commit()
    except NameError, msg:
        print msg
        db.rollback()
    db.close()