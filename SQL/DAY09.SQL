# SQL Day 09 Notes: HAVING Clause & Order of Query Execution

## HAVING Clause

The `HAVING` clause is used to filter **groups** created by `GROUP BY`.

Unlike `WHERE`, `HAVING` works **after** grouping and can use aggregate functions.

### Syntax

```sql
SELECT column_name, AGGREGATE_FUNCTION(column_name)
FROM table_name
WHERE condition
GROUP BY column_name
HAVING aggregate_condition;
```

---

## WHERE vs HAVING

| WHERE                          | HAVING                      |
| ------------------------------ | --------------------------- |
| Filters individual rows        | Filters grouped rows        |
| Executed before `GROUP BY`     | Executed after `GROUP BY`   |
| Cannot use aggregate functions | Can use aggregate functions |

### Example (WHERE)

```sql
SELECT *
FROM movies
WHERE year > 2000;
```

Filters rows before grouping.

---

### Example (HAVING)

```sql
SELECT director,
COUNT(*) AS total_movies
FROM movies
GROUP BY director
HAVING COUNT(*) > 1;
```

Returns only directors who have directed more than one movie.

---

## More Examples

### Average Rating Greater Than 8

```sql
SELECT director,
AVG(rating) AS average_rating
FROM movies
GROUP BY director
HAVING AVG(rating) > 8;
```

---

### Movies After 2000 with At Least 2 Movies

```sql
SELECT director,
COUNT(*) AS total_movies
FROM movies
WHERE year > 2000
GROUP BY director
HAVING COUNT(*) >= 2;
```

---

# SQL Query Execution Order

Although we write SQL queries in one order, SQL executes them in the following order:

```text
1. FROM
2. WHERE
3. GROUP BY
4. HAVING
5. SELECT
6. ORDER BY
7. LIMIT
```

---

## Purpose of Each Clause

### 1. FROM

Chooses the table.

```sql
FROM movies
```

---

### 2. WHERE

Filters rows before grouping.

```sql
WHERE year > 2000
```

---

### 3. GROUP BY

Creates groups.

```sql
GROUP BY director
```

---

### 4. HAVING

Filters groups.

```sql
HAVING COUNT(*) > 1
```

---

### 5. SELECT

Chooses the columns to display.

```sql
SELECT director, COUNT(*)
```

---

### 6. ORDER BY

Sorts the output.

```sql
ORDER BY rating DESC
```

---

### 7. LIMIT

Restricts the number of rows returned.

```sql
LIMIT 5
```

---

# Common Mistake

❌ Incorrect

```sql
SELECT director, COUNT(*)
FROM movies
WHERE COUNT(*) > 1
GROUP BY director;
```

Reason:

* `COUNT()` is not available during the `WHERE` step.

---

✅ Correct

```sql
SELECT director, COUNT(*)
FROM movies
GROUP BY director
HAVING COUNT(*) > 1;
```

---

# Memory Trick

```text
FROM
↓
WHERE
↓
GROUP BY
↓
HAVING
↓
SELECT
↓
ORDER BY
↓
LIMIT
```

Remember:

* **WHERE → Filters Rows**
* **GROUP BY → Creates Groups**
* **HAVING → Filters Groups**
* **ORDER BY → Sorts Results**
* **LIMIT → Restricts Output**

---

# Key Takeaways

* `WHERE` filters rows.
* `HAVING` filters groups.
* Aggregate functions (`COUNT`, `SUM`, `AVG`, `MAX`, `MIN`) are used with `HAVING`.
* SQL execution order is different from the order in which queries are written.
* Understanding execution order helps avoid SQL errors and write optimized queries.
