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
interface_filter = """
<interfaces-state
	xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
	<interface>
		<name>GigabitEthernet1</name>
	</interface>
</interfaces-state>
"""

# Execute the get RPC
reply = session.get_config(filter=("subtree", interface_filter))

print(reply)

session.close_session()