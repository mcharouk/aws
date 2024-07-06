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

# Demo synopsis

* Username : Marc Charouk
* Game Name : Tic Tac Toe Example
* In TraceMap
  * put 15 minutes period
  * click on SNS node
  * go see the Exceptions in the trace details. Should display invalid email
* Go on cloud formation stack to fix the issue (fix the parameter)
* Cloud formation stack takes time to redeploy, so it may not be necessary to fix the issue in a real demo
* Replay a game, the error should be fixed