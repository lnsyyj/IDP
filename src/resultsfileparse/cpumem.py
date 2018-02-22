#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ..commons.config import *
from ..databases.mariadb import *
import time

def parse_data(data):
    dict = {}
    rs_data = data.strip('\n').split(' ')
    print rs_data
    dict['datetime'] = rs_data[1] + " " + rs_data[2]
    dict['machineid'] = rs_data[0]
    dict['cpu_used_percentage'] = rs_data[3]
    dict['mem_used_percentage'] = rs_data[4]
    print dict
    return dict


def parse_cpu_mem_result_file_local():
    filelist = ['cpu_mem_20192.168.0.203','cpu_mem_20192.168.0.204']
    for filename in filelist:
        print filename
        with open(get_s3_download_object_to_file_local_directory() + filename, "r") as file:
            line = file.readline()
            print line
            while line:
                dict = parse_data(line)
                time.sleep(0.05)
                mariadb_insert_cpu_mem_data(dict)
                line = file.readline()
                print line