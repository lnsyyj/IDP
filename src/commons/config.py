#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

class global_var(object):
    '''global var'''
    # S3 Configuration
    s3_server = "192.168.199.151"
    s3_access_key = "8RD7LPKW2C1SA0JIR6OK"
    s3_secret_key = "jZoOqGxvHD6Ym2QOhh96CUFc9dfHBLNla9Xhi6Rs"
    s3_bucket = "ceph-stability"
    s3_download_object_to_file_local_directory = "F:\\"      #windows

    # MySQL or MariaDB Configuration
    mysql_ip = "192.168.199.151"
    mysql_port = "3306"
    mysql_account = "root"
    mysql_password = "root"
    mysql_db_name = "ceph"

    token_port = "80"
    current_path = os.path.dirname(os.path.abspath(__file__))  # The script executes the current directory
    log_file = current_path + "/../../" + "logs" + "/" + "auto_api_test.log"  # Script execution log
    # mysql_ip = "10.100.46.246"

def get_s3_server():
    return global_var.s3_server

def get_s3_access_key():
    return global_var.s3_access_key

def get_s3_secret_key():
    return global_var.s3_secret_key

def get_s3_bucket():
    return global_var.s3_bucket

def get_s3_download_object_to_file_local_directory():
    return global_var.s3_download_object_to_file_local_directory

def get_mysql_ip():
    return global_var.mysql_ip

def get_mysql_port():
    return global_var.mysql_port

def get_mysql_account():
    return global_var.mysql_account

def get_mysql_password():
    return global_var.mysql_password

def get_mysql_db_name():
    return global_var.mysql_db_name

def get_log_file():
    return global_var.log_file