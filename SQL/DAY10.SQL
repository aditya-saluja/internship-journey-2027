# SQL Day 10 – INSERT

## INSERT
Used to add new rows into a table.

### Insert all columns
INSERT INTO table_name
VALUES (value1, value2, value3);

### Insert specific columns
INSERT INTO table_name (column1, column2)
VALUES (value1, value2);

### Insert multiple rows
INSERT INTO table_name
VALUES
(value1, value2),
(value3, value4);

## Schema
A schema is the structure or blueprint of a table.
It defines:
- Column names
- Data types
- Column order

## Important Points
- INSERT adds new data.
- VALUES must match the number of columns.
- You can insert one or many rows at once.
- Mentioning column names makes queries more flexible.
- SQL expressions can be used while inserting values.