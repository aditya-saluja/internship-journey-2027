-- PRACTICE QUESTIONS 
-- 1- LIMIT - (KITNE CHAHIYE EK BAAR MEIN)
-- EX- Q1. Third highest scorer

SELECT player, runs
FROM players
ORDER BY runs DESC
LIMIT 1 OFFSET 2;

-- 2- OFFSET(KITNE KA GAP LENA HEIN )
-- EX-Q1. Third highest scorer
SELECT player, runs
FROM players
ORDER BY runs DESC
LIMIT 1 OFFSET 2;


-- 3-ORDER BY (ASC , DESC ORDER MEIN ARRANGE KRNA )
-- EX-Third highest scorer
SELECT player, runs
FROM players
ORDER BY runs DESC
LIMIT 1 OFFSET 2;




-- 4- DISTINCT(NO DUPLICATES )
-- EX-Distinct teams with pagination

SELECT DISTINCT team
FROM players
ORDER BY team ASC
LIMIT 2 OFFSET 1;