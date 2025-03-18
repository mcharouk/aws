# Private Link

## Producer Side : create endpoint service

* go on VPC, Endpoint services, and create one
* Endpoint Service name

```
private-link-demo-service-endpoint
```
* Load Balancer type : Network
* Leave Acceptance Required
* Supported Address Types : Ipv4

## Consumer Side : Create interface endpoint

* Create an endpoint
* Name

```
private-link-demo-service
```

* Service name
  * go to service endpoint details
  * copy paste service name field

* Select subnets linked to availability zones
* select Security group named

```
PrivateLinkEndpointSG
```

## Producer Side : Accept Endpoint connection

* go to endpoint services, tab endpoint connections
* accept the pending endpoint

## Consumer side

* connect to EC2 instance
* check that endpoint is in available status
* get DNS name of interface endpoint (do not take service name)
  * for that select ENI associated with security group **PrivateLinkEndpointSG**

* should return an ok status (its the health check endpoint)
```
curl http://[DnsName]
```
* should return lambda content
```
curl http://[DnsName]/hello
```