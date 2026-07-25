# SQL Day 16 – DROP TABLE

## DROP TABLE
Used to permanently remove an entire table from the database.

Syntax:
DROP TABLE table_name;

## IF EXISTS
Prevents an error if the table does not exist.

Syntax:
DROP TABLE IF EXISTS table_name;

## DELETE vs DROP

DELETE
- Removes rows
- Table still exists
- Structure remains

DROP TABLE
- Removes the entire table
- Deletes rows, schema, and constraints
- Table no longer exists

## Important Points
• DROP TABLE permanently removes the table.
• IF EXISTS prevents errors if the table is missing.
• Foreign key dependencies may need to be removed before dropping a table.