# -*- coding: utf-8 -*-

from s3.connect import *
from resultsfileparse.vdbench import *
# from resultsfileparse import *

def raw_data_to_structured_data():
    conn = s3_connect()
    bucket = s3_get_bucket(conn, get_s3_bucket())
    objects_list = s3_list_all_objects_under_bucket(bucket)
    s3_download_object_to_file(bucket, objects_list)
    parse_vdbench_result_file(objects_list)