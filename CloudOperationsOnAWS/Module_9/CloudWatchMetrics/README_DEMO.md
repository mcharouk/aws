## Metrics Insights

* Calculate metric by aggregating data from multiple plants
* N.B. only last 3 hours can be queried (metrics insights limitation)

There are 2 factories

Each factory has 3 machine which have the same name

```
SELECT MAX(Temperature) FROM "ExampleCorp-Factory" GROUP BY MachineName
```
## Math expression

* go on pre built dashboard
* click on the widget and View in Metrics to demonstrate Math expression
  * for a single factory, we can display min, max, and average temperature for all its hovens

## Variable

Create a variable from metric

* Dimensions : FactoryName
* Select menu (dropdown)
* Use results of a search metric. Editor : 

```
{ExampleCorp-Factory,FactoryName,MachineName} MetricName=Temperature
```

* Click on FactoryName after clicking on Search