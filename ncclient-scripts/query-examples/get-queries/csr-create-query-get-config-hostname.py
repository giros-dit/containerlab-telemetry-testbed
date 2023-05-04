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
<native
	xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
	<hostname></hostname>
</native>
"""

# Execute the get RPC
reply = session.get(filter=("subtree", hostname_filter))

print(reply)

session.close_session()