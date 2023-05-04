import sys
import subprocess
from ncclient import manager
from jinja2 import Template

if len(sys.argv) < 2:
    print("Error - Incorrect arguments")
    print('Usage: python3 csr-create-query-get-interface-xe-native.py <container_name> [<interface_index>]')
    print('Example for the GigabitEthernet1 interface: python3 csr-create-query-get-interface-xe-native.py clab-telemetry-testbed-r1 GigabitEthernet1')
    print('Example for all interfaces: python3 csr-create-query-get-interface-xe-native.py clab-telemetry-testbed-r1')
    exit(1)
else:
    container_name = sys.argv[1]
    check_container = subprocess.getoutput("docker ps -a | awk '{print $NF}' | grep " + container_name)

if check_container != container_name:
    print("Error - Incorrect arguments: You need to specify the container name of the network device.")
    print('Usage: python3 csr-create-query-get-interface-xe-native.py <container_name> [<interface_index>]')
    print('Example for the GigabitEthernet1 interface: python3 csr-create-query-get-interface-xe-native.py clab-telemetry-testbed-r1 GigabitEthernet1')
    print('Example for all interfaces: python3 csr-create-query-get-interface-xe-native.py clab-telemetry-testbed-r1')
    exit(1)
else:
    if len(sys.argv) == 2:
        # Render our Jinja template
        interface_template = Template(open('./jinja2-templates/interfaces-xe-native-state.xml').read())
        interface_rendered = interface_template.render()
    elif len(sys.argv) == 3:
        # Render our Jinja template
        interface_template = Template(open('./jinja2-templates/interface-xe-native-state.xml').read())
        interface_rendered = interface_template.render(
            INTERFACE_NAME = sys.argv[2]
        )

r = {
    "host": container_name,
    "port": 830,
    "username": "admin",
    "password": "admin",
    "hostkey_verify": False,
    "device_params": {"name": "csr"}
}

session = manager.connect(**r)

print ("\nSession ID: ", session.session_id)

# Execute the get RPC
reply = session.get(filter=("subtree", interface_rendered))

print("\nInterface configuration and operational status of network device "+ container_name + ": \n")

print(reply)

session.close_session()