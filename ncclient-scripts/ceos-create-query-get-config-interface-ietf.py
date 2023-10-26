import sys
import subprocess
from ncclient import manager
from jinja2 import Template

if len(sys.argv) < 2:
    print("Error - Incorrect arguments")
    print('Usage: python3 ceos-create-query-get-config-interface-ietf.py <container_name> [<interface_name>]')
    print('Example for the Ethernet1 interface: python3 ceos-create-query-get-config-interface-ietf.py clab-telemetry-testbed-xe-ceos-r2 Ethernet1')
    print('Example for all interfaces: python3 ceos-create-query-get-config-interface-ietf.py clab-telemetry-testbed-xe-ceos-r2')
    exit(1)
else:
    container_name = sys.argv[1]
    check_container = subprocess.getoutput("docker ps -a | awk '{print $NF}' | grep " + container_name)

if check_container != container_name:
    print("Error - Incorrect arguments: You need to specify the container name of the network device.")
    print('Usage: python3 ceos-create-query-get-config-interface-ietf.py <container_name> [<interface_name>]')
    print('Example for the Ethernet1 interface: python3 ceos-create-query-get-config-interface-ietf.py clab-telemetry-testbed-xe-ceos-r2 Ethernet1')
    print('Example for all interfaces: python3 ceos-create-query-get-config-interface-ietf.py clab-telemetry-testbed-xe-ceos-r2')
    exit(1)
else:
    if len(sys.argv) == 2:
        # Render our Jinja template
        interface_template = Template(open('./jinja2-templates/interfaces-ietf-config.xml').read())
        interface_rendered = interface_template.render()
    elif len(sys.argv) == 3:
        # Render our Jinja template
        interface_template = Template(open('./jinja2-templates/interface-ietf-config.xml').read())
        interface_rendered = interface_template.render(
            INTERFACE_NAME = sys.argv[2]
        )

r = {
    "host": container_name,
    "port": 830,
    "username": "admin",
    "password": "admin",
    "hostkey_verify": False,
    "device_params": {"name": "default"}
}

session = manager.connect(**r)

print ("\nSession ID: ", session.session_id)

# Execute the get-config RPC
reply = session.get_config(source="running", filter=("subtree", interface_rendered))

print("\nInterface configuration of network device "+ container_name + ": \n")

print(reply)

session.close_session()