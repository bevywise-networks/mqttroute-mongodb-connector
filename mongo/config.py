#!/usr/bin/python
###############################################################################
#
# @2018 Bevywise Networks - www.bevywise.com 
#
# This plugin is an extension to the MQTTRoute, the enterprise mqtt broker. 
# This plugin helps you store all the data received by the broker from different edge devices into the MongoDB. 
#
# config.py
#
# Author Name: Vardharajulu K N (VKN)
#
# This file holds all the information of the configuration and the 
# initialization parameters. 
#
# Licensed under the Apache License, Version 2.0 (the "License");
# 
# you may not use this file except in compliance with the License.
# 
# You may obtain a copy of the License at  http://www.apache.org/licenses/LICENSE-2.0
# 
###############################################################################

import ConfigParser, os.path,logger

class Config(object):
    def __init__(self, configFilePath):
        self.configFilePath = configFilePath
        self.configParser = ConfigParser.RawConfigParser()
    
    def _open(self):
        if os.path.isfile(self.configFilePath) == True:
            self.configParser.read(self.configFilePath)
            return True
        else:
            return False

    def get_value(self, section, key):
        return self.configParser.get(section, key)

class Mongo_config(Config):
    def __init__(self, configFilePath):
        super(Mongo_config, self).__init__(configFilePath)

# Write test code for reading the MONGO config file. 
if __name__ == '__main__':
    config=Mongo_config('./plugin.conf')
    log = logger.Logger()
    if config._open() == True:
        log.info(config.get_value('MONGO','HOSTNAME'))
        log.info(config.get_value('MONGO','PORT'))
        log.info(config.get_value('MONGO','COLLECTION'))
