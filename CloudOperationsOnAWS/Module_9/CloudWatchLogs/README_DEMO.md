## Logs insights

* logs make take a little time to appear in Insights, around 2-3 mins

* Execute these saved queries 
  * pattern_tab : basic query to show pattern tab and to show what logs looks like
  * extract_structured_from_plain_text : it shows how we can parse a structured log expression
  * count_per_log_status_and_hour : it shows we can aggregate data
  * most_recent_by_log_path (take from below) : it's to show dedup feature
    * dedup takes the most recent record grouped by some dimension

most_recent_by_log_path

```
filter @logStream = 'webServer-i87465854' 
 | parse @message "* - - [* +0000] \"* * HTTP/1.1\" * *" as log_ip, log_time, log_method, log_path, log_status, log_bytes
 | sort @timestamp desc
 | dedup log_path
```


## Create Metric from logs

* this metric filter applies on all logs that match /users and error with status code 500
* open log stream view
* type in search bar

```
[ip, user, username, timestamp, request="*/users*", status_code=500, bytes]
```

* Creation Params 
  * filter name : server-error-on-users
  * namespace name : CloudWatchDemo
  * metric name : ServerErrorOnUsers
  * metric value : 1
  * default value : 0  OR set dimensions
  * unit : Count

* it can be seen at log group level, there is a metric filters tab. But metrics does not appear, as we need to ingest more logs for that.
* Resolution is 1-min for all filter metrics