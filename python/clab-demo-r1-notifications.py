from ncclient import manager
from ncclient.xml_ import to_ele

r1 = {
    "host": "clab-demo-r1",
    "port": 830,
    "username": "admin",
    "password": "admin",
    "hostkey_verify": False,
    "device_params": {"name": "csr"}
}

session = manager.connect(**r1)

print ("Session ID: ", session.session_id)

# When building the RPC request XML, use dampening-period for on-change notifications (when supported).
# Otherwise, use period and specify an integer value.

rpc = """

    <establish-subscription xmlns="urn:ietf:params:xml:ns:yang:ietf-event-notifications" 
    xmlns:yp="urn:ietf:params:xml:ns:yang:ietf-yang-push">
        <stream>yp:yang-push</stream>
        <yp:xpath-filter>/native/hostname</yp:xpath-filter>
        <yp:dampening-period>0</yp:dampening-period>
    </establish-subscription>

"""

request = session.dispatch(to_ele(rpc))

print(request)

print("Notifications for device clab-demo-r1...")

while True:
    sub_data = session.take_notification()
    if (sub_data != None):
        print(sub_data.notification_xml)
    print("------------------------")
