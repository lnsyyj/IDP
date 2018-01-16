# -*- coding: utf-8 -*-
from awsauth import
import requests

host = "10.100.46.195"
ep = "admin"

s3uid = "lenovo"
access = "8RD7LPKW2C1SA0JIR6OK"
secret = "jZoOqGxvHD6Ym2QOhh96CUFc9dfHBLNla9Xhi6Rs"

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
