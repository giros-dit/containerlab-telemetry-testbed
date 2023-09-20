import sys
import subprocess
from ncclient import manager
from ncclient.xml_ import to_ele
from kafka import KafkaProducer

if len(sys.argv) < 4:
    print("Error - Incorrect arguments")
    print('Usage: python3 csr-create-periodic-subscription-interfaces-state-kafka.py <container_name> <interface_name> <period_in_cs>')
    print('Example: python3 csr-create-periodic-subscription-interfaces-state-kafka.py clab-telemetry-testbed-r1 GigabitEthernet1 1000')
    exit(1)
else:
    container_name = sys.argv[1]
    check_container = subprocess.getoutput("sudo docker ps -a | awk '{print $NF}' | grep " + container_name)

if check_container != container_name:
    print("Error - Incorrect arguments: You need to specify the container name of the network device.")
    print('Usage: python3 csr-create-periodic-subscription-interfaces-state-kafka.py <container_name> <interface_name> <period_in_cs>')
    print('Example: python3 csr-create-periodic-subscription-interfaces-state-kafka.py clab-telemetry-testbed-r1 GigabitEthernet1 1000')
    exit(1)
else:
    if len(sys.argv) != 4:
        print("Error - Incorrect arguments: You need to specify the container name of the network device.")
        print('Error - Incorrect arguments: Period (in ms) must be specified.')
        print('Usage: python3 csr-create-periodic-subscription-interfaces-state-kafka.py <container_name> <interface_name> <period_in_cs>')
        print('Example: python3 csr-create-periodic-subscription-interfaces-state-kafka.py clab-telemetry-testbed-r1 GigabitEthernet1 1000')
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

print ("\nSession ID: ", session.session_id)

xpath = "/interfaces-state/interface[name=\'" + sys.argv[2] + "\']"
subscription = "period"
period = sys.argv[3]


# When building the RPC request XML, use dampening-period for on-change notifications (when supported).
# Otherwise, use period and specify an integer value for the time in centiseconds.

rpc = """

    <establish-subscription xmlns="urn:ietf:params:xml:ns:yang:ietf-event-notifications"
    xmlns:yp="urn:ietf:params:xml:ns:yang:ietf-yang-push">
        <stream>yp:yang-push</stream>
        <yp:xpath-filter>{0}</yp:xpath-filter>
        <yp:{1}>{2}</yp:{1}>
    </establish-subscription>

""".format(xpath, subscription, period)

request = session.dispatch(to_ele(rpc))

print(request)

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

print("\nYANG-Push notifications for XPath " + xpath + " of network device "+ container_name + ": \n")

while True:
    sub_data = session.take_notification()
    if (sub_data != None):
        producer.send('interfaces-state-subscriptions', value=str(sub_data.notification_xml).encode('utf-8'))
    producer.flush()
