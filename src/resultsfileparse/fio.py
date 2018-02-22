#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ..commons.config import *
from ..databases.mariadb import *

def parse_data(data):
    dict = {}
    print "=========================="
    # print type(data)
    rs_data = data.strip('\n').split(',')
    print rs_data
    rs_data_0 = rs_data[0].strip('\n').split('_')
    print rs_data_0
    dict['testmode'] = rs_data_0[1]
    dict['blocksize'] = rs_data_0[2]
    dict['runtime'] = rs_data_0[3][7:]
    dict['iodepth'] = rs_data_0[4][7:]
    dict['numjob'] = rs_data_0[5][6:]
    dict['imagenum'] = rs_data_0[6][8:]
    dict['casenumber'] = rs_data_0[7][4:]
    dict['rwtypepercentage'] = rs_data_0[8]
    dict['datetime'] = rs_data_0[10] + "-" + rs_data_0[11] + "-" + rs_data_0[12] + " " + rs_data_0[13] + ":"  + rs_data_0[14] + ":" + rs_data_0[15][:2]
    dict['iops'] = rs_data[4]
    dict['readwrite'] = rs_data[5]
    dict['latency'] = rs_data[6]
    dict['unit'] = rs_data[8]
    dict['logfilename'] = rs_data[0]
    # dict['']
    print dict
    print "=========================="
    return dict

def parse_fio_result_file():
    with open(get_s3_download_object_to_file_local_directory() + "result.txt", "r") as file:
        line = file.readline()
        print line
        while line:
            dict = parse_data(line)
            mariadb_insert_fio_performance_data(dict)
            line = file.readline()
            print line