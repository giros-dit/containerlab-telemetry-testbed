import sys
import subprocess
from ncclient import manager
from ncclient.xml_ import to_ele

container_name = sys.argv[1]
check_container = subprocess.getoutput("docker ps -a | awk '{print $NF}' | grep " + container_name)

if check_container != container_name:
    print("Error - Incorrect arguments")
    print("You need to specify the container name of the network device.")
    print('Usage: python3 csr-r1-create-subscription.py <container_name> <XPath> <subscription-type> [<period_in_ms>]')
    print('Periodic subscription example: python3 csr-r1-create-subscription.py clab-telemetry-ixiac-lab-r1 "/interfaces-state/interface[name=\'GigabitEthernet2\']" periodic 1000')
    print('On-Change subscription example: python3 csr-r1-create-subscription.py clab-telemetry-ixiac-lab-r1 "/native/hostname" onchange')
    exit(1)
else:
    if len(sys.argv) < 4:
        print("Error - Incorrect arguments")
        print('Usage: python3 csr-r1-create-subscription.py <container_name> <XPath> <subscription-type> [<period_in_ms>]')
        print('Periodic subscription example: python3 csr-r1-create-subscription.py clab-telemetry-ixiac-lab-r1 "/interfaces-state/interface[name=\'GigabitEthernet2\']" periodic 1000')
        print('On-Change subscription example: python3 csr-r1-create-subscription.py clab-telemetry-ixiac-lab-r1 "/native/hostname" onchange')
        exit(1)
    elif sys.argv[3] != "onchange" and sys.argv[3] != "periodic":
        print("Error - Incorrect arguments")
        print('Usage: python3 csr-r1-create-subscription.py <container_name> <XPath> <subscription-type> [<period_in_ms>]')
        print('Periodic subscription example: python3 csr-r1-create-subscription.py clab-telemetry-ixiac-lab-r1 "/interfaces-state/interface[name=\'GigabitEthernet2\']" periodic 1000')
        print('On-Change subscription example: python3 csr-r1-create-subscription.py clab-telemetry-ixiac-lab-r1 "/native/hostname" onchange')
        exit(1)
    elif sys.argv[3] == "periodic" and len(sys.argv) != 5:
        print("Error - Incorrect arguments for periodic subscription")
        print('Usage: python3 csr-r1-create-subscription.py <container_name> <XPath> <subscription-type> [<period_in_ms>]')
        print('Periodic subscription example: python3 csr-r1-create-subscription.py clab-telemetry-ixiac-lab-r1 "/interfaces-state/interface[name=\'GigabitEthernet2\']" periodic 1000')
        exit(1)
    elif sys.argv[3] == "onchange" and len(sys.argv) != 4:
        print("Error - Incorrect arguments for on-change subscription")
        print('Usage: python3 csr-r1-create-subscription.py <container_name> <XPath> <subscription-type> [<period_in_ms>]')
        print('On-Change subscription example: python3 csr-r1-create-subscription.py clab-telemetry-ixiac-lab-r1 "/native/hostname" onchange')
        exit(1)

r1 = {
    "host": container_name,
    "port": 830,
    "username": "admin",
    "password": "admin",
    "hostkey_verify": False,
    "device_params": {"name": "csr"}
}

session = manager.connect(**r1)

print ("Session ID: ", session.session_id)

if (sys.argv[3]=="periodic"):
    subscription = "period"
    period = sys.argv[4]
else:
    subscription = "dampening-period"
    period = 0

# When building the RPC request XML, use dampening-period for on-change notifications (when supported).
# Otherwise, use period and specify an integer value.

rpc = """

    <establish-subscription xmlns="urn:ietf:params:xml:ns:yang:ietf-event-notifications"
    xmlns:yp="urn:ietf:params:xml:ns:yang:ietf-yang-push">
        <stream>yp:yang-push</stream>
        <yp:xpath-filter>{0}</yp:xpath-filter>
        <yp:{1}>{2}</yp:{1}>
    </establish-subscription>

""".format(sys.argv[2], subscription, period)

request = session.dispatch(to_ele(rpc))

print(request)

print("\nYANG-Push notifications for XPath " + sys.argv[2] + " of network device "+ container_name + ": \n")

while True:
    sub_data = session.take_notification()
    if (sub_data != None):
        print(sub_data.notification_xml)
    print("------------------------")
