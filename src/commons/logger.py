#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import config

# Initialize logger
def setup_logger(name, log_file, level=logging.DEBUG, format=False):
	handler = logging.FileHandler(log_file)
	if format is True:
		formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
		handler.setFormatter(formatter)
	logger = logging.getLogger(name)
	logger.setLevel(level)
	logger.addHandler(handler)
	return logger