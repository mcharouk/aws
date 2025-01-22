* in a InPrivate window, connect with admin user and assume the role 

```
businessAnalystRole
```

* go to Athena, select Workgroup 

```
datalake-admins-workgroup
```

* Show that tables are not displayed
* Try to execute some query

```
select * from "training-data".cities LIMIT 5;
```

* with admin, add a grant to allow business analyst to query the table.
  * Choose businessAnalystRole as Role to grant
  * Choose Named Data Catalog Resources (note the LF-TAG is a best practice at scale)
  * Select the database
  * Select cities table
  * Data Filter
    * Name : JapaneseCities
    * Column Based Access
      * Exclude Columns : population
    * Row Based Access
      * iso3 = 'JPN'
  * Select Table Permissions : SELECT
    * Note that if DESCRIBE is selected, it's not possible to specify column or row level access
  * Grantable Table Permissions to be left empty
  * Execute Query again with BA Role. 
    * Note that population column is not displayed.
    * Note that only Japan lines are returned