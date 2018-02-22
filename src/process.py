#!/usr/bin/env python
# -*- coding: utf-8 -*-

from s3.connect import *
from resultsfileparse.vdbench import *
from resultsfileparse.fio import *
from resultsfileparse.osdstatus import *
from databases.mariadb import *
from resultsfileparse.cpumem import *
# from resultsfileparse import *

def raw_data_to_structured_data():
    conn = s3_connect()
    bucket = s3_get_bucket(conn, get_s3_bucket())
    objects_list = s3_list_all_objects_under_bucket(bucket)
    s3_download_object_to_file(bucket, objects_list)
    # result log
    # parse_vdbench_result_file(objects_list)
    # mariadb_insert_stability_vdbench_data()

    # cpu mem log
    parse_cpu_mem_result_file(objects_list)


def test_connect_db():
    mariadb_connect_test()

def raw_data_to_structured_data_fio():
    parse_fio_result_file()

def raw_data_to_structured_data_osd():
    parse_osdstatus_result_file()

def raw_data_to_structured_data_cpu_mem():
    parse_cpu_mem_result_file_local()