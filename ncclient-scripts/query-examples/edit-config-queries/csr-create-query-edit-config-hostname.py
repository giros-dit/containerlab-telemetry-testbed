from ncclient import manager

r = {
    "host": "clab-telemetry-testbed-r1",
    "port": 830,
    "username": "admin",
    "password": "admin",
    "hostkey_verify": False,
    "device_params": {"name": "csr"}
}

session = manager.connect(**r)

print ("Session ID: ", session.session_id)

# Create a configuration filter
hostname_filter = """
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
	<native
		xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
		<hostname>r1-ios-xe-csr1000v</hostname>
	</native>
</config>
"""

# Execute the edit-config RPC
reply = session.edit_config(target="running", config=hostname_filter)

print(reply)

session.close_session()