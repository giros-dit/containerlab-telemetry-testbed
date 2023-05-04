import sys
import subprocess
from ncclient import manager
from jinja2 import Template

if len(sys.argv) < 2:
    print("Error - Incorrect arguments")
    print('Usage: python3 csr-create-query-get-interface.py <container_name> [<interface_name>]')
    print('Example for the GigabitEthernet1 interface: python3 csr-create-query-get-interface-ietf.py clab-telemetry-testbed-r1 GigabitEthernet1')
    print('Example for all interfaces: python3 csr-create-query-get-interface-ietf.py clab-telemetry-testbed-r1')
    exit(1)
else:
    container_name = sys.argv[1]
    check_container = subprocess.getoutput("docker ps -a | awk '{print $NF}' | grep " + container_name)

if check_container != container_name:
    print("Error - Incorrect arguments: You need to specify the container name of the network device.")
    print('Usage: python3 csr-create-query-get-interface.py <container_name> [<interface_name>]')
    print('Example for the GigabitEthernet1 interface: python3 csr-create-query-get-interface-ietf.py clab-telemetry-testbed-r1 GigabitEthernet1')
    print('Example for all interfaces: python3 csr-create-query-get-interface-ietf.py clab-telemetry-testbed-r1')
    exit(1)
else:
    if len(sys.argv) == 2:
        # Render our Jinja templates
        interface_config_template = Template(open('./jinja2-templates/interfaces-ietf-config.xml').read())
        interface_config_rendered = interface_config_template.render()
        interface_state_template = Template(open('./jinja2-templates/interfaces-ietf-state.xml').read())
        interface_state_rendered = interface_state_template.render()
    elif len(sys.argv) == 3:
        # Render our Jinja templates
        interface_config_template = Template(open('./jinja2-templates/interface-ietf-config.xml').read())
        interface_config_rendered = interface_config_template.render(
            INTERFACE_NAME = sys.argv[2]
        )
        interface_state_template = Template(open('./jinja2-templates/interface-ietf-state.xml').read())
        interface_state_rendered = interface_state_template.render(
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

# Execute the get RPCs
reply_config = session.get(filter=("subtree", interface_config_rendered))

print("\nInterface configuration of network device "+ container_name + ": \n")

print(reply_config)

reply_state = session.get(filter=("subtree", interface_state_rendered))

print("\nInterface operational status of network device "+ container_name + ": \n")

print(reply_state)

session.close_session()