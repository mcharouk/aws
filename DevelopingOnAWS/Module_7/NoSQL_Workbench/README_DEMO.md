* DataModeler to explore the schema of the table
* Visualizer to show data, use DynamoDB Local
* Add a connection by getting credential from sso console
* User Operation Builder to query real DynamoDB tables


## Connection

### Automatic procedure

* Execute python script
```
python update-connection-credentials.py
```
* Check in console that expiration time is OK 

### Manual procedure
* go to .aws/cli/cache
* get last json by modified date. Role credentials are stored here

* Already created a profile named NoSQLWorkbench, update the credentials in .aws/credentials file
* if profile is not present, create a new connection by providing the role credentials

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