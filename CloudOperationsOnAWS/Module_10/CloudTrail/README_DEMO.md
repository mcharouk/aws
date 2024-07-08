* Select pre-created database
* Select dedicated workgroup

Athena Query

```
CREATE EXTERNAL TABLE cloudtrail_logs_aws_cloudtrail_logs_637423642269_095b0741 (
    eventVersion STRING,
    userIdentity STRUCT<
        type: STRING,
        principalId: STRING,
        arn: STRING,
        accountId: STRING,
        invokedBy: STRING,
        accessKeyId: STRING,
        userName: STRING,
        sessionContext: STRUCT<
            attributes: STRUCT<
                mfaAuthenticated: STRING,
                creationDate: STRING>,
            sessionIssuer: STRUCT<
                type: STRING,
                principalId: STRING,
                arn: STRING,
                accountId: STRING,
                username: STRING>,
            ec2RoleDelivery: STRING,
            webIdFederationData: MAP<STRING,STRING>>>,
    eventTime STRING,
    eventSource STRING,
    eventName STRING,
    awsRegion STRING,
    sourceIpAddress STRING,
    userAgent STRING,
    errorCode STRING,
    errorMessage STRING,
    requestParameters STRING,
    responseElements STRING,
    additionalEventData STRING,
    requestId STRING,
    eventId STRING,
    resources ARRAY<STRUCT<
        arn: STRING,
        accountId: STRING,
        type: STRING>>,
    eventType STRING,
    apiVersion STRING,
    readOnly STRING,
    recipientAccountId STRING,
    serviceEventDetails STRING,
    sharedEventID STRING,
    vpcEndpointId STRING,
    tlsDetails STRUCT<
        tlsVersion: STRING,
        cipherSuite: STRING,
        clientProvidedHostHeader: STRING>
)
COMMENT 'CloudTrail table for cloudtrail-demo-marccharouk-847856739 bucket'
ROW FORMAT SERDE 'org.apache.hive.hcatalog.data.JsonSerDe'
STORED AS INPUTFORMAT 'com.amazon.emr.cloudtrail.CloudTrailInputFormat'
OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION 's3://cloudtrail-demo-marccharouk-847856739/AWSLogs/637423642269/CloudTrail/'
TBLPROPERTIES ('classification'='cloudtrail');
```

Queries sample

```
-- distinct principals that generate trails
select distinct useridentity.sessionContext.sessionIssuer.arn
from cloudtrail_logs_aws_cloudtrail_logs_637423642269_095b0741;

-- api calls with the most write calls by service
SELECT eventsource, eventname, count(*) from cloudtrail_logs_aws_cloudtrail_logs_637423642269_095b0741 
where readonly ='false'
group by eventsource, eventname 
order by count(*) DESC
LIMIT 50;

-- select event name and see request parameters and response elements
SELECT eventtime, eventsource, eventname, errorcode, requestparameters, responseelements from cloudtrail_logs_aws_cloudtrail_logs_637423642269_095b0741 
where eventname = 'CreateTagOption'
;
```