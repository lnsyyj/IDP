# -*- coding: utf-8 -*-

from ..commons.config import *

def parse_vdbench_result_file(file_object):
    for f in file_object:
        if f.name.endswith('/'):
            continue
        with open( get_s3_download_object_to_file_local_directory() + f.name.replace('/','\\'),"r") as file:
            print get_s3_download_object_to_file_local_directory() + f.name.replace('/', '\\')
            line = file.readline()
            print line
            while line:
                line = file.readline()
                print line
            # print file