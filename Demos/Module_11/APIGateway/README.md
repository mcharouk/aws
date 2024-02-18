## Demo instruction

* Create an API of type **REST**
* Create 2 resources : resource and {id}
* Lambda proxy integration should be set to **true**
* deploy to a stage
* Create a WAF Rule (geolocation to block requests from Romania)
* Create a Web ACL from WAF and assign the api gateway from there

## Sample event

```
{
    "pathParameters": {
        "id": "3"
    }
}
```

## Console

### Authorization

* Authorizers have a specific menu (on the left)
* In **method request**
  * it's here that the authorization can be configured

### Cache

* Cache is activated in the **stage** properties
* In **method request**
  * the cache box is to include the parameter to generate the cache key  

### API Key And UsagePlans

* In **method request**
  * specify if api key is required
* API is created in a specific menu
* Usage plans are created in a specific menu. Once created they can be associated with
  * a stage
  * api keys

### Throttling

* configured in the stage (rate and burst)
