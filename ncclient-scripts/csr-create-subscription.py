import sys
import subprocess
from ncclient import manager
from ncclient.xml_ import to_ele

if len(sys.argv) < 4:
    print("Error - Incorrect arguments")
    print('Usage: python3 csr-create-subscription.py <container_name> <XPath> <subscription_type> [<period_in_ms>]')
    print('Periodic subscription example: python3 csr-create-subscription.py clab-telemetry-ixiac-lab-r1 "/interfaces-state/interface[name=\'GigabitEthernet2\']" periodic 1000')
    print('On-Change subscription example: python3 csr-create-subscription.py clab-telemetry-ixiac-lab-r1 "/native/hostname" on-change')
    exit(1)
else:
    container_name = sys.argv[1]
    check_container = subprocess.getoutput("docker ps -a | awk '{print $NF}' | grep " + container_name)

if check_container != container_name:
    print("Error - Incorrect arguments: You need to specify the container name of the network device.")
    print('Usage: python3 csr-create-subscription.py <container_name> <XPath> <subscription_type> [<period_in_ms>]')
    print('Periodic subscription example: python3 csr-create-subscription.py clab-telemetry-ixiac-lab-r1 "/interfaces-state/interface[name=\'GigabitEthernet2\']" periodic 1000')
    print('On-Change subscription example: python3 csr-create-subscription.py clab-telemetry-ixiac-lab-r1 "/native/hostname" on-change')
    exit(1)
else:
    if sys.argv[3] != "on-change" and sys.argv[3] != "periodic":
        print("Error - Incorrect arguments")
        print('Usage: python3 csr-create-subscription.py <container_name> <XPath> <subscription_type> [<period_in_ms>]')
        print('Periodic subscription example: python3 csr-create-subscription.py clab-telemetry-ixiac-lab-r1 "/interfaces-state/interface[name=\'GigabitEthernet2\']" periodic 1000')
        print('On-Change subscription example: python3 csr-create-subscription.py clab-telemetry-ixiac-lab-r1 "/native/hostname" on-change')
        exit(1)
    elif sys.argv[3] == "periodic" and len(sys.argv) != 5:
        print("Error - Incorrect arguments for periodic subscription")
        print('Usage: python3 csr-create-subscription.py <container_name> <XPath> <subscription_type> [<period_in_ms>]')
        print('Periodic subscription example: python3 csr-create-subscription.py clab-telemetry-ixiac-lab-r1 "/interfaces-state/interface[name=\'GigabitEthernet2\']" periodic 1000')
        exit(1)
    elif sys.argv[3] == "on-change" and len(sys.argv) != 4:
        print("Error - Incorrect arguments for on-change subscription")
        print('Usage: python3 csr-create-subscription.py <container_name> <XPath> <subscription_type> [<period_in_ms>]')
        print('On-Change subscription example: python3 csr-create-subscription.py clab-telemetry-ixiac-lab-r1 "/native/hostname" on-change')
        exit(1)

r = {
    "host": container_name,
    "port": 830,
    "username": "admin",
    "password": "admin",
    "hostkey_verify": False,
    "device_params": {"name": "csr"}
}

session = manager.connect(**r)

print ("Session ID: ", session.session_id)

if (sys.argv[3]=="periodic"):
    subscription = "period"
    period = sys.argv[4]
else:
    subscription = "dampening-period"
    period = 0

# When building the RPC request XML, use dampening-period for on-change notifications (when supported).
# Otherwise, use period and specify an integer value for the time in centiseconds.

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
