# SQL Day 08 Notes: Order of Execution of a Query

## Introduction

Although we write SQL queries in one order, SQL executes them in a different order. Understanding this execution order helps avoid common mistakes and makes writing complex queries much easier.

---

# Actual SQL Execution Order

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

---

## 1. FROM

* SQL first selects the table from which data will be retrieved.

Example:

```sql
SELECT *
FROM movies;
```

---

## 2. WHERE

* Filters individual rows before grouping.

Example:

```sql
SELECT *
FROM movies
WHERE year > 2000;
```

---

## 3. GROUP BY

* Creates groups based on one or more columns.

Example:

```sql
SELECT director, COUNT(*)
FROM movies
GROUP BY director;
```

---

## 4. HAVING

* Filters the groups created by `GROUP BY`.
* Can use aggregate functions like COUNT(), SUM(), AVG(), MAX(), MIN().

Example:

```sql
SELECT director, COUNT(*)
FROM movies
GROUP BY director
HAVING COUNT(*) > 1;
```

---

## 5. SELECT

* Chooses which columns or expressions will be displayed in the final result.

Example:

```sql
SELECT director, COUNT(*)
FROM movies
GROUP BY director;
```

---

## 6. ORDER BY

* Sorts the final result.

Ascending:

```sql
ORDER BY rating ASC;
```

Descending:

```sql
ORDER BY rating DESC;
```

---

## 7. LIMIT

* Restricts the number of rows returned.

Example:

```sql
SELECT *
FROM movies
LIMIT 5;
```

---

# Common Mistake

❌ Wrong:

```sql
SELECT director, COUNT(*)
FROM movies
WHERE COUNT(*) > 1
GROUP BY director;
```

Reason:

* `WHERE` executes before `GROUP BY`.
* Aggregate functions are not available in `WHERE`.

---

✅ Correct:

```sql
SELECT director, COUNT(*)
FROM movies
GROUP BY director
HAVING COUNT(*) > 1;
```

---

# Difference Between WHERE and HAVING

| WHERE                          | HAVING                      |
| ------------------------------ | --------------------------- |
| Filters rows                   | Filters groups              |
| Executed before GROUP BY       | Executed after GROUP BY     |
| Cannot use aggregate functions | Can use aggregate functions |

---

# Easy Memory Trick

```
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

* **WHERE → Rows**
* **GROUP BY → Groups**
* **HAVING → Groups**
* **ORDER BY → Sorting**
* **LIMIT → Final Output**

---

# Key Takeaways

* SQL executes queries in a different order than they are written.
* `FROM` always executes first.
* `WHERE` filters rows before grouping.
* `GROUP BY` creates groups.
* `HAVING` filters grouped data.
* `SELECT` chooses the output columns.
* `ORDER BY` sorts the results.
* `LIMIT` returns only the required number of rows.
