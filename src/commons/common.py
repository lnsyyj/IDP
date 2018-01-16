#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import logger
import logging
import config

logs = logger.setup_logger("global log", config.get_log_file(), level=logging.DEBUG, format=True)

def get_token():
	url = config.get_http_prefix() + ":5000/v2.0/tokens"
	headers = {'Content-Type': 'application/json'}
	body = {
    	"auth": {
        	"tenantName": "admin",
        	"passwordCredentials": {
            	"username": "admin",
            	"password": "Admin_123456"
            	# "password": "12345"
        	}
    	}
	}
	results = requests.post(url=url, headers=headers, data=json.dumps(body))
	json_result = json.loads(results.text)
	return json_result['access']['token']['id']

def get_header():
	token = get_token()
	headers = {
		'Content-type': 'application/json',
		'LOG_USER': 'admin',
		'X-Auth-Token': token
		# 'X-Auth-Token': token + "1"
	}
	return headers

def restful_api_method(url, body, method):
	headers = get_header()
	logs.debug("===================================================================")
	logs.debug(url)
	logs.debug(headers)
	logs.debug(body)
	logs.debug(method)
	if method == 'GET':
		r = requests.get(url=url, headers=headers, data=json.dumps(body))
	if method == 'PUT':
		r = requests.put(url=url, headers=headers, data=json.dumps(body))
	if method == 'POST':
		r = requests.post(url=url, headers=headers, data=json.dumps(body))
	if method == 'DELETE':
		r = requests.delete(url=url, headers=headers, data=json.dumps(body))
	if method == 'HEAD':
		pass
	if method == 'OPTIONS':
		pass
	logs.debug(r)
	logs.debug(r.text)
	logs.debug("===================================================================")
	return r