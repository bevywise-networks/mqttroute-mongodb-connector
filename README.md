## mqttroute-mongodb-connector

This plugin connects MQTTRoute with the Mongodb to store received payload info into Mongodb for further analysis and decision making. 

# MQTTRoute 
MQTTRoute is a powerful and high performance MQTTBroker that enables communication between various MQTT Devices and MQTT Sensors. MQTTRoute has FREE and affordable premium versions. 

# configure and setup mqttroute-mongodb-connector
	1. open plugin.conf and configure the hostname and port no of the MongoDB Server.
	2. copy the  pugin.conf and paste it in to Bevywise/MQTTRoute/lib.
	3. copy the  folder mongo and paste it in to Bevywise/MQTTRoute/lib.
	4. replace custom_store.py with Bevywise/MQTTRoute/lib/custom_store.py.
	5. Open Bevywise/MQTTRoute/conf/data_store.conf 
		1. Update CUSTOMSTORAGE = ENABLED
		2. Update DATASTORE = CUSTOM 
	6. Start the MQTTRoute and it will start storing all the payload into Mongo DB Server.

