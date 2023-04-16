import sys
from ncclient import manager
from ncclient.xml_ import to_ele

if len(sys.argv) < 3:
    print("Error - Incorrect arguments")
    print('Usage: python3 csr-r1-create-subscription.py <XPath> <subscription-type> [<period_in_ms>]')
    print('Periodic subscription example: python3 csr-r1-create-subscription.py "/interfaces-state/interface[name=\'GigabitEthernet2\']" periodic 1000')
    print('On-Change subscription example: python3 csr-r1-create-subscription.py "/native/hostname" onchange')
    exit(1)
elif sys.argv[2] != "onchange" and sys.argv[2] != "periodic":
    print("Error - Incorrect arguments")
    print('Usage: python3 csr-r1-create-subscription.py <XPath> <subscription-type> [<period_in_ms>]')
    print('Periodic subscription example: python3 csr-r1-create-subscription.py "/interfaces-state/interface[name=\'GigabitEthernet2\']" periodic 1000')
    print('On-Change subscription example: python3 csr-r1-create-subscription.py "/native/hostname" onchange')
    exit(1)
elif sys.argv[2] == "periodic" and len(sys.argv) != 4:
    print("Error - Incorrect arguments")
    print('Usage: python3 csr-r1-create-subscription.py <XPath> <subscription-type> [<period_in_ms>]')
    print('Periodic subscription example: python3 csr-r1-create-subscription.py "/interfaces-state/interface[name=\'GigabitEthernet2\']" periodic 1000')
    exit(1)
elif sys.argv[2] == "onchange" and len(sys.argv) != 3:
    print("Error - Incorrect arguments")
    print('Usage: python3 csr-r1-create-subscription.py <XPath> <subscription-type> [<period_in_ms>]')
    print('On-Change subscription example: python3 csr-r1-create-subscription.py "/native/hostname" onchange')
    exit(1)


r1 = {
    "host": "clab-telemetry-ixiac-lab-r1",
    "port": 830,
    "username": "admin",
    "password": "admin",
    "hostkey_verify": False,
    "device_params": {"name": "csr"}
}

session = manager.connect(**r1)

print ("Session ID: ", session.session_id)

if (sys.argv[2]=="periodic"):
    subscription = "period"
    period = sys.argv[3]
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

""".format(sys.argv[1], subscription, period)

request = session.dispatch(to_ele(rpc))

print(request)

print("Notifications for device clab-telemetry-testbed-r1...")

while True:
    sub_data = session.take_notification()
    if (sub_data != None):
        print(sub_data.notification_xml)
    print("------------------------")
