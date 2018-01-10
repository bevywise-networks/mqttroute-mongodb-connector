################################################################
# @Bevywise.com IOT Initiative. All rights reserved 
# www.bevywise.com Email - support@bevywise.com
#
# custom_store.py
#
# The custom data store hook for the Big Data Storage. 
# The Custom data hook can be enabled in the broker.conf 
# inside conf/ folder.
# 
# The parameter data will be in dict format and the keys are 'sender','topic', 'message', 'unixtime', 'timestamp'
#
################################################################
import time
from mongo import Mongo
filepath = "./plugin.conf"
Mon_inst = Mongo(filepath)
	
def handle_Received_Payload(data):

	# Write your code here. Use your connection object to 
	# Send data to your data store
	result = Mon_inst.data_consumer(data)
	# if result is none then write failed
	 
# Write code for testing. 
if __name__ == '__main__':
	param1 = {'topic': 'mytopic', 'unixtime': 1514960289, 'message': 'hello I am publisher1', 'sender': 'publisherclient1', 'timestamp': '2018-01-03 11:48:09'}
	handle_Received_Payload(param1)
	