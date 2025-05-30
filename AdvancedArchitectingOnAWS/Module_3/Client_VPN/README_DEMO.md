# Client VPN Endpoint

* create Client VPN Endpoint with name

```
ClientVPNDemo
```

* client IPv4 Cidr

```
10.1.0.0/22
```

* select server certificate with domain as server1.example.com
* check box Use Mutual authentication
* select client certificate with domain as server1.example.com (same than server)
* DNS parameters, for both servers, use default AWS DNS

```
10.0.0.2
```

* For VPC, select Client VPN one
* For Sec Group, Select **client_vpn_sg**

# Target Network associations

* Associate a public subnet (to provide internet access)

# Authorization Rules

* Provide All Access to VPC Range

```
10.0.0.0/16
```

* Provide All Access to Internet

```
0.0.0.0/0
```

# Route table

* Add a route  for internet access
  * Destination CIDR : 0.0.0.0/0
  * Target subnet : Public subnet Id

# Test connection

!!  Client VPN might take a significant time to successfuly create, maybe it's good to continue module content, and come back at a latter time !!

* execute script exportClientVPNConfig.py
  * it downloads VPN Client configuration, and script will add client certificate infos at the end of it
  * file is generated with name **client-config.ovpn**
* Open AWS VPN Client
* Default profile should match the file generated by the script
* Connect
* try to ping EC2 private IP Address (provided by CF)
* Internet connectivity
  * try to nslookup www.google.com
  * try to navigate on browser