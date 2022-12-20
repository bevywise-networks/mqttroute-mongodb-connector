################################################################
# @Bevywise.com IOT Initiative. All rights reserved 
# www.bevywise.com Email - support@bevywise.com
#
# custom_store.py
#
# The custom data store hook for storing MQTT Payload in MongoDB. 
# The Custom data hook can be enabled in the broker.conf 
# inside conf/ folder.
# 
# The parameter data will be in dict format and the keys are 'sender','topic', 'message', 'unixtime', 'timestamp'
#
################################################################

import os, sys

from pathlib import Path
current_path = Path(os.getcwd())
plugin_path = os.path.join(current_path.parent.absolute(),'extensions','mongo')
sys.path.append(plugin_path)
conf_path = os.path.join(plugin_path, './plugin.conf')
from mongo import Mongo

global Mon_inst
Mon_inst = Mongo(conf_path)

def handle_Received_Payload(data):

	#
	# Write your code here. Use your connection object to 
	#
	#
	# finish your code here.
	#
	# Send data to your data store
	try:
		result = Mon_inst.data_consumer(data)
		# if result is none then write failed
	except Exception as e:
		print(e)
	 
	
