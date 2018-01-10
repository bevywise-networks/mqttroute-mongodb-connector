#!/usr/bin/python
###############################################################################
#
# @2018 Bevywise Networks - www.bevywise.com 
#
# This plugin is an extension to the MQTTRoute, the enterprise mqtt broker. 
# This plugin helps you store all the data received by the broker from different edge devices into the MongoDB. 
#
# __init__.py
#
# Author Name: Vardharajulu K N (VKN)
#
# The Package contains MQTTRoute plugin for MongoDB.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# 
# you may not use this file except in compliance with the License.
# 
# You may obtain a copy of the License at  http://www.apache.org/licenses/LICENSE-2.0
# 
###############################################################################

from mongo import Mongo

__all__ = ['Mongo']
__all__ = [x.encode('ascii') for x in __all__]
