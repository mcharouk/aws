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