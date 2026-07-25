# SQL Day 15 – ALTER TABLE

## ALTER TABLE
Used to modify the structure of an existing table.

### Add a column
ALTER TABLE table_name
ADD column_name datatype;

### Add with default value
ALTER TABLE table_name
ADD column_name datatype
DEFAULT value;

### Remove a column
ALTER TABLE table_name
DROP column_name;

### Rename a table
ALTER TABLE table_name
RENAME TO new_table_name;

## Important Points
• ALTER TABLE modifies an existing table.
• ADD creates a new column.
• DROP removes a column.
• RENAME TO changes the table name.
• Different databases support different ALTER TABLE features.