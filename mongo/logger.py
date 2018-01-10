#!/usr/bin/python
###############################################################################
#
# @2018 Bevywise Networks - www.bevywise.com 
#
# This plugin is an extension to the MQTTRoute, the enterprise mqtt broker. 
# This plugin helps you store all the data received by the broker from different edge devices into the MongoDB. 
#
# logger.py
#
# Author Name: Vardharajulu K N (VKN)
#
# The Package contains logger to store Error and warnings in logfile.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# 
# you may not use this file except in compliance with the License.
# 
# You may obtain a copy of the License at  http://www.apache.org/licenses/LICENSE-2.0
# 
###############################################################################

import logging
        
class Logger(object):
    # Initialiser Class
    def __init__(self,logfile='./mongo.log'):
        self.logger = logging.getLogger('mongo')
        self.handler = logging.FileHandler(logfile)
        self.log = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        self.setlogger()

    def setlogger(self):
        self.handler.setFormatter(self.log)
        self.logger.addHandler(self.handler) 
        self.logger.setLevel(logging.DEBUG)

    def info(self,info):
        self.logger.info(info)

    def warn(self,warn):
        self.logger.warn(warn)

    def err(self,err):
        self.logger.warn(err)
    
    def warnings(message, category, filename, lineno, file=None, line=None):
        #self.logger.warn('{}:{}:{}'.format(category, filename, lineno))
        pass
