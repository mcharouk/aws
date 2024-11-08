* DataModeler to explore the schema of the table
* Visualizer to show data, use DynamoDB Local
* Add a connection by getting credential from sso console
* User Operation Builder to query real DynamoDB tables

* use NoSQLWorkbench profile to create and delete the table in DynamoDB

## Connection

### Automatic procedure

* Execute python script
```
python update-connection-credentials.py
```
* this script updates credentials of NOSQLWorkbench profile

### Manual procedure

* go to AWS SSO Portal
* get temp credentials of Administrator role
* copy/paste them in the NoSQLWorkbench profile
* restart NOSQL Workbench

## Queries

Try execute query and scans. Only one query is allowed

PartiQL Example

```
select FirstName, LastName from Employee where LoginAlias = 'johns'
```

PartiQL : Query a GSI

```
SELECT FirstName, LastName, LoginAlias, ManagerLoginAlias, Skills  
FROM "Employee"."Name" 
WHERE FirstName = 'Diego' 
AND LastName = 'Ramirez';
```

Query another GSI

```
SELECT ManagerLoginAlias, LoginAlias, FirstName, LastName
FROM "Employee"."DirectReports" 
WHERE ManagerLoginAlias = 'johns';
```

## Other options

* Can save query samples as Operations
* Can generate code from a query (Python, Java, NodeJS)