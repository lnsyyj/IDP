#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ..commons.config import *
from ..databases.mariadb import *


def parse_data(data):
    dict = {}
    rs_data = data.strip('\n').split(',')
    dict['datetime'] = rs_data[0]
    dict['osdupquantity'] = rs_data[1]
    dict['osdinquantity'] = rs_data[2]
    print dict
    return dict


def parse_osdstatus_result_file():
    with open(get_s3_download_object_to_file_local_directory() + "4", "r") as file:
        line = file.readline()
        print line
        while line:
            dict = parse_data(line)
            mariadb_insert_osdstatus_performance_data(dict)
            line = file.readline()
            print line