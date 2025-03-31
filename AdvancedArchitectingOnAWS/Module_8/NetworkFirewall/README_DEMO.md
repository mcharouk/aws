# Checks

* connect to EC2 instance and type command

```
curl -L www.youtube.com
```

* Get EC2 DNS address and try it from France IP or another country IP. All should work
* Show network firewall rules

# Routing tables

* Make all the modifications described below before retesting again with EC2

## Public subnet route table

* Change route which has destination 0.0.0.0/0
  * Target : Gateway Load Balancer Endpoint / select Network Firewall 

## Activate inbound traffic rules

* change routing table of IGW
  * Add an edge association to associate it with IGW
  * Add a route
    * Destination : Public Subnet IP Range (provided in CF ouput)
    * Target : Gateway Load Balancer Endpoint / select Network Firewall 


 
