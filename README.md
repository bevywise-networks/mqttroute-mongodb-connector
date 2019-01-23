## mqttroute-mongodb-connector

This plugin connects Bevywise MQTT Broker with the Mongodb to store received payload info into Mongodb for further analysis and decision making. 

# Bevywise MQTTRoute 
Bevywise MQTT Broker is a powerful and high performance MQTTBroker that enables communication between various MQTT Devices and MQTT Sensors. Bevywise MQTT Broker has FREE and affordable premium versions. 

# configure and setup mqttroute-mongodb-connector
	1. Open plugin.conf and configure the 
		1. update hostname and port no of the MongoDB Server in MONGO section.
		2. If AUTHENTICATION is enabled in MQTTRoute, then update the Mongodb credentials otherwise set AUTHENTICATION_ENABLED = FALSE  
		3. 2.update log file path to your own folder location. [default = Bevywise/MQTTRoute/extension]
	2. Copy and paste the mongo folder and pugin.conf in to Bevywise/MQTTRoute/extension.
	3. Replace custom_store.py with Bevywise/MQTTRoute/extension/custom_store.py.
	4. Open Bevywise/MQTTRoute/conf/data_store.conf 
		1. Update CUSTOMSTORAGE = ENABLED
		2. Update DATASTORE = CUSTOM 
	5. Start the MQTTRoute and it will start storing all the payload into Mongo DB Server.

