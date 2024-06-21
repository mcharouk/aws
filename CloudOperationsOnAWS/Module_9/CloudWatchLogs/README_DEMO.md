## Logs insights

most_recent_by_log_path

```
filter @logStream = 'webServer-i87465854' 
 | parse @message "* - - [* +0000] \"* * HTTP/1.1\" * *" as log_ip, log_time, log_method, log_path, log_status, log_bytes
 | sort @timestamp desc
 | dedup log_path
```


## Create Metric from logs

in log stream view, type in search bar

```
users 500
```

filter name : server-error-on-users
namespace name : CloudWatchDemo
metric name : ServerErrorOnUsers
metric value : 1
default value : 0
unit : Count

it can be seen at log group level, there is a metric filters tab. But metrics does not appear, as we need to ingest more logs for that.