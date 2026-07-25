# SQL Day 13 – CREATE TABLE

## CREATE TABLE
Used to create a new table in the database.

Syntax:
CREATE TABLE table_name (
    column_name datatype,
    column_name datatype
);

## IF NOT EXISTS
Prevents an error if the table already exists.

Syntax:
CREATE TABLE IF NOT EXISTS table_name (...);

## Common Data Types
INTEGER  → Whole numbers
FLOAT / DOUBLE / REAL → Decimal numbers
TEXT / VARCHAR / CHAR → Strings
BOOLEAN → True/False
DATE → Date
DATETIME → Date and Time
BLOB → Binary files

## Common Constraints
PRIMARY KEY → Unique identifier for each row
AUTOINCREMENT → Automatically increases ID
UNIQUE → No duplicate values
NOT NULL → Value cannot be empty
CHECK → Custom validation rule
FOREIGN KEY → Links one table to another

## Remember
CREATE TABLE creates the structure only.
INSERT is used later to add data.