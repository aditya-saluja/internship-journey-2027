# SQL Day 11 – UPDATE

## UPDATE
Used to modify existing rows in a table.

Syntax:
UPDATE table_name
SET column = value
WHERE condition;

## Multiple columns
UPDATE table_name
SET column1 = value1,
    column2 = value2
WHERE condition;

## Important
• UPDATE changes existing data.
• SET specifies new values.
• WHERE selects which rows to update.
• Without WHERE, every row is updated.
• Always test the WHERE condition with a SELECT query before running UPDATE.