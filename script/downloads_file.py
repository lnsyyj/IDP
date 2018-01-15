# -*- coding: utf-8 -*-
from awsauth import S3Auth
import requests


host = "192.168.122.100"
ep = "admin"

s3uid = ""
access = ""
secret = ""

# metadata user
url = "http://%s/%s/metadata/user"%(host, ep)
response = requests.get(url,auth=S3Auth(access, secret))
print '\n metadata  user'
print 'status code: ', response.status_code
print 'content: ', response.content

# metadata bucket
url = "http://%s/%s/metadata/bucket"%(host, ep)
response = requests.get(url,auth=S3Auth(access, secret))
print '\n metadata  bucket'
print 'status code: ', response.status_code
print 'content: ', response.content
