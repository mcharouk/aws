## Application Insights

* create a resource group with Tag **DemoName=XRay**. Provide any name
* create a new application in Insights with resource group

* create additional alarms
* create specific dashboard for problems detected
* monitor events related to components
* list problems detected

To resolve problem, it must be in status STABILIZING first at least. We have to wait some time after the resolution to obtain this status

```
aws application-insights update-problem --problem-id [PROBLEM_ID] --update-status RESOLVED
```

## Normal run

* execute testAPI.py, it will run a few queries to be able to observe some logs
* In **city** lambda code
  * show annotations
  * show sub segments
  * show patch
* look at the results in traceMap.
  *  When we click on a node, we can see its metrics, alarms, logs, dashboard, traces, trace analytics
* On traces screen, we can search for traces by annotation. 
  * Try with Country annotation for example
* Show traces
  * we can see details of response times
  * we can see logs corresponding to the trace (aggregation of all components logs)

## Exceptions

* update **City** lambda code, uncomment line 49 to 51 to generate random errors
* execute testAPI.py to generate some errors
* on application insights, a problem is detected. Logs might take time to appear in problem dashboard (2 mins)
* Look at tracemap. Errors appears in Red
* Look at traces, Errors appears clearly on the table
* Click on a trace in error status, to see details
  * We can see which step throw an error
  * Clicking on segment or subsegment in error, go in exception tab to see the error


## Powertools

* used X-Ray
* used Event pattern objects
* used parameter (parameter store)
* user structured logging
