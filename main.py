#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from src.s3.connect import *
from src.process import *

if __name__ == '__main__':
    # conn = s3_connect()
    # # s3_list_all_bucket(conn)
    # bucket = s3_get_bucket(conn,get_s3_bucket())
    # objects_list = s3_list_all_objects_under_bucket(bucket)
    # s3_download_object_to_file(bucket,objects_list)
    raw_data_to_structured_data()