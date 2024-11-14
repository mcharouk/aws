* subscribe to sns topic to see the output of step function with an email (last task in step sends a message on sns topic)
* show JSON state language, syntax overview
* show designer,
  * integration with all AWS Service
  * Exception handling with catch and retries
* Explain how asynchronous task work (manual tasks)
* Execute a workflow (no parameter to supply) and show monitoring
* Show metrics and logs capabilities

# Step function process description

* CheckStockPrice : return a random int between 0 and 100
* GenerateBuySellRecommendation
  * Buy if stock price < 50
  * Sell if stock price > 50
* Request Human Approval
  * Automatic approval
* Buy Stock and Sell Stock : return a json that describes how much quantity it bought/sold (random number) with a transaction id and timestamp
* Report result : send directly to SNS (without Lambda)