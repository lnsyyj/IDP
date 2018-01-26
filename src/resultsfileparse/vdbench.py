#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ..commons.config import *
from ..databases.mariadb import *

def parse_vdbench_result_file(file_object):
    result_dict = {}
    for f in file_object:
        file_name = ('-'.join(f.name.split('-')[1:])).encode()
        if f.name.endswith('/'):
            continue
        with open( get_s3_download_object_to_file_local_directory() + f.name.replace('/','\\'),"r") as file:
            print get_s3_download_object_to_file_local_directory() + f.name.replace('/', '\\')
            line = file.readline()
            print line
            while line:
                if line.startswith('20',0,len(line)) == True:
                    rs_data =  line.strip('\n').split(' ')
                    mariadb_insert_stability_vdbench_data(rs_data, file_name)
                line = file.readline()


def parse_cpu_mem_result_file(file_object):
    result_dict = {}
    for f in file_object:
        if f.name.endswith('/'):
            continue
        with open( get_s3_download_object_to_file_local_directory() + f.name.replace('/','\\'),"r") as file:
            print get_s3_download_object_to_file_local_directory() + f.name.replace('/', '\\')
            line = file.readline()
            print line
            while line:
                rs_data =  line.strip('\n').split(' ')
                mariadb_insert_system_monitor_data(rs_data)
                line = file.readline()