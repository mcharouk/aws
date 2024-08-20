* DataModeler to explore the schema of the table
* Visualizer to show data, use DynamoDB Local
* Add a connection by getting credential from sso console
* User Operation Builder to query real DynamoDB tables


## Queries

Try execute query and scans

PartiQL Example

```
select FirstName, LastName from Employee where LoginAlias = 'johns'
```

PartiQL : Query a GSI

```
select * from "Employee"."Name" where FirstName = 'Diego' and LastName = 'Ramirez'
```