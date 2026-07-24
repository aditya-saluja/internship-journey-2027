# SQL Day 07 Notes: Aggregate Functions & GROUP BY

## Aggregate Functions

Aggregate functions are used to summarize multiple rows into a single value.

### Common Aggregate Functions

**1. COUNT()**

* Counts the number of rows.

```sql
SELECT COUNT(*) FROM movies;
```

**2. SUM()**

* Returns the total of a numeric column.

```sql
SELECT SUM(box_office_million) FROM movies;
```

**3. AVG()**

* Returns the average value.

```sql
SELECT AVG(length_minutes) FROM movies;
```

**4. MAX()**

* Returns the highest value.

```sql
SELECT MAX(rating) FROM movies;
```

**5. MIN()**

* Returns the lowest value.

```sql
SELECT MIN(rating) FROM movies;
```

---

## COUNT(*) vs COUNT(column)

* `COUNT(*)` → Counts all rows.
* `COUNT(column)` → Counts only non-NULL values in that column.

Example:

```sql
SELECT COUNT(*) FROM employees;
SELECT COUNT(bonus) FROM employees;
```

---

## AS Keyword

Used to rename the output column.

Example:

```sql
SELECT SUM(box_office_million) AS total_collection
FROM movies;
```

---

## GROUP BY

`GROUP BY` divides rows into groups and performs aggregate functions on each group.

Example:

```sql
SELECT director,
COUNT(title)
FROM movies
GROUP BY director;
```

Another Example:

```sql
SELECT director,
AVG(length_minutes)
FROM movies
GROUP BY director;
```

---

## WHERE with Aggregate Functions

`WHERE` filters rows before aggregation.

Example:

```sql
SELECT SUM(box_office_million)
FROM movies
WHERE rating > 8;
```

---

# SQL Execution Order

1. FROM
2. WHERE
3. GROUP BY
4. Aggregate Functions (COUNT, SUM, AVG, MAX, MIN)
5. SELECT
6. ORDER BY

---

# Important Pattern

| Question  | Function |
| --------- | -------- |
| How many? | COUNT()  |
| Total?    | SUM()    |
| Average?  | AVG()    |
| Highest?  | MAX()    |
| Lowest?   | MIN()    |

---

# GROUP BY Pattern

If the question says:

* For each director
* For each department
* For each year
* For each city

Use:

```sql
GROUP BY column_name
```

Example:

```sql
SELECT director,
MAX(box_office_million)
FROM movies
GROUP BY director;
```

---

# Common Mistake

❌ Wrong

```sql
SELECT salary,
SUM(salary)
FROM employees;
```

✅ Correct

```sql
SELECT SUM(salary)
FROM employees;
```

Only include a normal column in `SELECT` when it is also present in `GROUP BY`.

---

# Key Takeaways

* Aggregate functions return summarized values.
* `COUNT(*)` counts rows.
* `SUM()` returns total.
* `AVG()` returns average.
* `MAX()` returns highest value.
* `MIN()` returns lowest value.
* Use `AS` to rename output columns.
* Use `GROUP BY` to perform calculations for each group.
* Use `WHERE` to filter rows before aggregation.
