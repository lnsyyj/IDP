# -*- coding: utf-8 -*-

# from boto.s3.connection import S3Connection
import boto
import boto.s3.connection
from ..commons.config import *
import os

def s3_connect():
    conn_obj = boto.connect_s3(aws_access_key_id = get_s3_access_key(), aws_secret_access_key = get_s3_secret_key(), host = get_s3_server(),calling_format = boto.s3.connection.OrdinaryCallingFormat(),is_secure=False)
    return conn_obj

def s3_list_all_bucket(conn_obj):
    for bucket in conn_obj.get_all_buckets():
        print "{name}\t{created}".format(
            name=bucket.name,
            created=bucket.creation_date,
        )

def s3_get_bucket(conn_obj,bucket_name):
    bucket_obj = conn_obj.get_bucket(bucket_name)
    return bucket_obj

def s3_list_all_objects_under_bucket(bucket_obj):
    # objects_list = bucket_obj.list(prefix = "cpu-mem/")
    objects_list = bucket_obj.list(prefix="vdbench/" + str(get_s3_directory_percentage()) + "/result/")
    for obj in objects_list:
        print obj
    return objects_list


def s3_download_object_to_file(bucket_obj, file_object):
    print type(file_object)
    for f in file_object:
        key = bucket_obj.lookup(f.name)
        if f.name.endswith('/'):
            if os.path.exists(f.name.replace('/', '\\')) == False:
                os.makedirs(get_s3_download_object_to_file_local_directory() + f.name)
            continue
        print "s3_download_object_to_file : " + f.name
        key = bucket_obj.get_key(f.name)
        key.get_contents_to_filename( get_s3_download_object_to_file_local_directory() + f.name.replace('/','\\'))