# Event Types

## Fact events

* does not contain the why
* size of events
* careful with joins (if a business event is composed of multiple entities), they might change too frequently if the event contains too much of information

## Delta event

* delta event contains minimal information and usually does only contain data that has changed
* provide intent (why an object is changing)
* good for event sourcing

For example on a shopping cart:
    * add item
    * remove item
    * add coupon
    * add subscription
    * remove coupon
    * remove subscription
    * update item quantity
    * apply shipping estimates
    * modify subscription dates

* in this example, too much detailed as consumers will have to implement the same logic to reproduce the state of a shopping cart
* each time a new event is introduced, consumers will have to update the logic to get the state
* requires ordering.
* fragile as consumers might have different policies to handle late events.
* risk is to push consumers rules to the producer. Consumer asking to generate events specific to its usage. Instead, it's better that the consumer get the state of an entity and apply business logic in its own service
* difficulty to maintain historical data
  * cannot be compacted as each delta event is required to rebuild the state. In long term, it might be too long to be able to rebuild a state from scratch

## Measurement events (Streaming event)

* more like iot/clickstream data
* not usable on their own, must get a set of these events to provide a meaningful information.
  

## Trigger or Signal events

* contains only ids
* dependent on an API to get all the data needed

# Bootstrap events

* dual writes : no atomic guarantees
* polling the db
  * tied to the db and internal schema. It's ok though if using views for example.
  * cannot detect deletions
  * not real time, depends on the polling frequency. Migh miss intermittent changes
  * db resources usage
* CDC
  * still tied to the model. Not possible to add views
  * can lead to highly normalized data events but it depends on the db and model
* Transactional Outbox
  * careful to update it with the master table within a transaction
  * requires more development
  * outbox write may cause failure to writes in primary table
  * db perf impact


# Dealing with eventual consistency

* Prevent failures
* Halt serving when lags exceeds threshold
* Show stale data
* callback