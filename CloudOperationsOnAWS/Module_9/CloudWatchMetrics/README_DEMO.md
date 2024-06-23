## Metrics Insights

* Calculate metric by aggregating data from multiple plants
* N.B. only last 3 hours can be queried (metrics insights limitation)

```
SELECT MAX(Temperature) FROM "ExampleCorp-Factory" GROUP BY MachineName
```
## Math expression

* show pre built dashboard

## Variable

Create a variable from metric

* Dimensions : FactoryName
* Select menu (dropdown)
* Use results of a search metric. Editor : 

```
{ExampleCorp-Factory,FactoryName,MachineName} MetricName=Temperature
```

* Click on FactoryName after clicking on Search