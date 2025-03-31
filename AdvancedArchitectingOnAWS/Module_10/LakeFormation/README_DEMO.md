# Check Business Analyst has no access

* in a InPrivate window, connect with admin user and assume the role 

```
businessAnalystRole
```

* go to Athena, select Workgroup 

```
datalake-admins-workgroup
```

* Business Analyst role has a grant on the table, so it can see it, but it has no grant on any column so query will fail 
* Try to execute some query

```
select * from "training-data".cities LIMIT 5;
```

* Should fail : (COLUMN_NOT_FOUND: line 1:8: Relation contains no accessible columns)

# Grant Business Analyst for access 

* with admin, go to Data Permissions 
  * add a grant to allow business analyst to query the table.
  * Choose businessAnalystRole as Role to grant
  * Choose Named Data Catalog Resources (note the LF-TAG is a best practice at scale)
  * Select the database
  * Select cities table
  * Data Filter
    * Name
     ```
     JapaneseCities
     ```
    * Column Based Access
      * Exclude Columns : population
    * Row Based Access
     ```
     iso3 = 'JPN'
     ```
  * Select Table Permissions : SELECT
    * Note that if DESCRIBE is selected, it's not possible to specify column or row level access
  * Grantable Table Permissions to be left empty

# Check table has been granted

* Execute Query again with BA Role. 
  * Note that population column is not displayed.
  * Note that only Japan lines are returned