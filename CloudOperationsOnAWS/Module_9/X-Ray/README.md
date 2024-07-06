# Cloud formation manual modifications

The stack is failing when deleting it

* added dependency on AttachGateway for resource 
	* EcsInstanceAsg
	* PubSubnet1RouteTableAssociation
	* PubSubnet2RouteTableAssociation
	* PubSubnet3RouteTableAssociation
	* ScorekeepLoadBalancer
* If not here, cloudformation tries to delete the IGW and VPC, although ASG (and EC2) are still running, and the delete operation fails
* Have to delete manually the auto scaling group to unlock deletion of other resources, i don't know why


* Must set ScorekeepService desired tasks to 0 and wait some seconds
* Must set ASG max instance to 0 and wait some seconds
