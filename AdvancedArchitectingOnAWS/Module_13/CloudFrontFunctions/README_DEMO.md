# Demo 

## Show console 

* show cloudfront function
* in **Policies**, show **origin request policy** named **S3-UserDeviceType**
* all is configured at behavior level (origin request policy and cloudfront function)

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