from ncclient import manager
import sys

ROUTER = sys.argv[1]
PREFIX = sys.argv[2]
NEXT_HOP = sys.argv[3]

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

  <network-instances xmlns="http://openconfig.net/yang/network-instance">

    <network-instance>
      <name>default</name>

      <protocols>

        <protocol>
          <identifier>STATIC</identifier>
          <name>STATIC</name>

          <config>
            <identifier>STATIC</identifier>
            <name>STATIC</name>
            <enabled>true</enabled>
          </config>

          <static-routes>

            <static>
              <prefix>{PREFIX}</prefix>

              <config>
                <prefix>{PREFIX}</prefix>
              </config>

              <next-hops>

                <next-hop>
                  <index>1</index>

                  <config>
                    <next-hop>{NEXT_HOP}</next-hop>
                    <metric>0</metric>
                  </config>

                </next-hop>

              </next-hops>

            </static>

          </static-routes>

        </protocol>

      </protocols>

    </network-instance>

  </network-instances>

</config>
"""

with manager.connect(**yang_server) as session:
    print("- Configuring static route with prefix " + PREFIX + " and next hop " + NEXT_HOP + " on router device " + ROUTER + "...")
    reply = session.edit_config(target="running", config=config)
    print(reply)
    print("")