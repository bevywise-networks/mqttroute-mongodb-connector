#!/usr/bin/python
###############################################################################
#
# @2018 Bevywise Networks - www.bevywise.com 
#
# This plugin is an extension to the MQTTRoute, the enterprise mqtt broker. 
# This plugin helps you store all the data received by the broker from different edge devices into the MongoDB. 
#
# mongo.py
#
# Author Name: Vardharajulu K N (VKN)
#
# The Package contains mongo instance creation, data insertion.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# 
# you may not use this file except in compliance with the License.
# 
# You may obtain a copy of the License at  http://www.apache.org/licenses/LICENSE-2.0
# 
###############################################################################

from pymongo import MongoClient
import logger, os, sys
from config import Config

class Mongo(Config):
    # Initialiser Class
    def __init__(self, filepath):
        super(Mongo, self).__init__(filepath)
        
        if self._open() == True:
            self.log = logger.Logger(self.get_value('LOG','LOG_FILE_PATH'))
            self.log.info("Config File Loaded Sucessfully.")
        else:
            self.log = logger.Logger()
            self.log.err("Config file open error.")
        self.custom_data = {
                        'mongo_host' : self.get_value('MONGO','HOSTNAME'), 
                        'mongo_port' : int(self.get_value('MONGO','PORT')), 
                        'db_name' : self.get_value('MONGO','DB_NAME'),
                        'collection' : self.get_value('MONGO','COLLECTION')
                        }
        self.init_db()

    def init_db(self):
        try:
            self.Mongo_instance = MongoClient(self.custom_data['mongo_host'],self.custom_data['mongo_port'])
            self.db = self.Mongo_instance[self.custom_data['db_name']]
            self.collection = self.db[self.custom_data['collection']]
        except Exception:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            self.log.err("Error in DB connection ")           
            self.log.err('{}:{}:{}'.format(exc_type, fname, exc_tb.tb_lineno))
        else:
            self.log.info("Sucessfully Connected To MongoDB at port - {0} ".format(self.custom_data['mongo_port']))    
            
    def data_consumer(self,data,result = ''):
        try:
            result = self.collection.insert_one(data)
        except Exception:
            self.log.err("Data Insert Error")           
        finally:
            return result
        
# Write code for testing. 
if __name__ == '__main__':
    Mongo(Config)    

