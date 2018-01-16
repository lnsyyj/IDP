# -*- coding: utf-8 -*-

from boto.s3.connection import S3Connection

def connect_s3():
    conn = S3Connection('<aws access key>', '<aws secret key>')


if __name__ == '__main__':
    pass