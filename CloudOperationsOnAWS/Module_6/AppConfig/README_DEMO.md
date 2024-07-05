# Demo

## Goals

* Goal of demo
  * rollback capabilities with cloudwatch alarm
  * validation features  

## Configuration

Configuration profile name

```
TestConfigProfile
```

Configuration
```
{
  "isDebugEnabled": false
}
```

Json schema
```
{
  "$id": "https://github.com/mygithub-handle/my-app-repo/blob/master/config/schema.json",
  "title": "My app config",
  "type": "object",
  "required": [
    "isDebugEnabled"
  ],
  "properties": {
    "isDebugEnabled": {
      "type": "boolean",
      "description": "flag that indicates if debug mode is enabled",
      "default": false
    }
  }
}
```

## Application

Application name

```
TestAppConfig
```

## Environment

Environment name

```
dev
```

Alarm Role Name

```
ssmCloudWatchAlarmDiscoveryRole
```

Alarm Name

```
AppConfigAlarm
```


* !! don't forget to click on Add to add alarm !!