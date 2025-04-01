# Demo 

* Cloudfront makes time to deploy when a change is requested, this is why distribution is pre configured in the demo

## Show console 

* show cloudfront function
* in **Policies**, show **origin request policy** named **S3-UserDeviceType**
* Origin Request Policy is used to
  * forward fields to origin
  * forward fields to edge computing functions (CloudFront functions / Lambda@edge)
* all is configured at behavior level (origin request policy and cloudfront function)
* Note that cloudfront function logs destination can be configured in Distribution settings (Logging section)
  * In this demo, no destination has been provided so it's not possible to see the logs

## Execute demo scripts

* change directory to demo folder
* show scripts in folder
  * desktop script has no user agent as it's already called from a desktop
  * mobile, smart-tv and tablet all set user agent to simulate device type
  * all points to the same cloudfront URL
  * redirection is made by Cloudfront function to get the right image
* execute scripts

```
.\desktop-script.ps1
```

```
.\mobile-script.ps1
```

```
.\smart-tv-script.ps1
```

```
.\tablet-script.ps1
```