# Cloudfront 

## Request collapsing

* [Sending multiple requests to cloudfront at the same time](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/RequestAndResponseBehaviorCustomOrigin.html#request-custom-traffic-spikes)
* To resume first request goes to the origin. Subsequent requests are in a wait state, and get data from the cache when it's available

