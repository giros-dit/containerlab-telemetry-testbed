from ncclient import manager
import sys

ROUTER = sys.argv[1]
INTERFACE = sys.argv[2]
IP = sys.argv[3]
PREFIX = sys.argv[4]

yang_server = {
    "host": ROUTER,
    "port": 830,
    "username": "admin",
    "password": "admin",
    "hostkey_verify": False,
    "device_params": {"name": "default"}
}

config = f"""
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <interfaces xmlns="http://openconfig.net/yang/interfaces">
    <interface>
      <name>{INTERFACE}</name>

      <config>
        <name>{INTERFACE}</name>
        <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">
          ianaift:ethernetCsmacd
        </type>
        <enabled>true</enabled>
      </config>

      <subinterfaces>
        <subinterface>
          <index>0</index>

          <config>
            <index>0</index>
            <enabled>true</enabled>
          </config>

          <ipv4 xmlns="http://openconfig.net/yang/interfaces/ip">
            <addresses>
              <address>
                <ip>{IP}</ip>

                <config>
                  <ip>{IP}</ip>
                  <prefix-length>{PREFIX}</prefix-length>
                </config>

              </address>
            </addresses>
          </ipv4>

        </subinterface>
      </subinterfaces>

    </interface>
  </interfaces>
</config>
"""

with manager.connect(**yang_server) as session:
    print("- Configuring IP " + IP + " on interface " + INTERFACE + " of router device " + ROUTER + "...")
    reply = session.edit_config(target="running", config=config)
    print(reply)
    print("")