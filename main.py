#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from src.s3.connect import *
from src.process import *
import platform

if __name__ == '__main__':
    # conn = s3_connect()
    # # s3_list_all_bucket(conn)
    # bucket = s3_get_bucket(conn,get_s3_bucket())
    # objects_list = s3_list_all_objects_under_bucket(bucket)
    # s3_download_object_to_file(bucket,objects_list)
    # ========================================
    # raw_data_to_structured_data()
    # print '-'.join('G20-杭州峰会-放假时间-放假安排'.split('-')[1:])
    # mariadb_insert_stability_vdbench_data()


    # fio 数据
    # raw_data_to_structured_data_fio()

    # osd 数据
    # raw_data_to_structured_data_osd()

    #cpu mem
    raw_data_to_structured_data_cpu_mem()