--1
SELECT c_name, vq_total, vq_comments
FROM Customer, verifiedQuote
WHERE c_address Like '%Boardfish%'
AND vq_custkey = c_custkey;

--2
SELECT (b_price + m_price + e_price) as TOTAL, b_name, m_name, e_name
FROM Brand, Model, extraPackages
WHERE b_brandkey = 54
AND m_name = 'Accord'
AND e_price = 424.00;

--3
SELECT m_name, q_total
FROM Model, estimatedQuote, Brand
WHERE m_brandkey = b_brandkey AND b_brandkey = q_brandkey AND m_price < '25000';

--4
SELECT c_name, c_phone
FROM Customer, verifiedQuote
WHERE c_custkey = vq_custkey AND vq_total > '50000';

--5
SELECT c_name, total(vq_total)
FROM verifiedQuote, Customer
WHERE c_custkey = vq_custkey
GROUP BY vq_custkey
    HAVING count(vq_custkey) = 2;

SELECT vq_custkey, count(vq_custkey)
FROM verifiedQuote
GROUP by vq_custkey;

--6
SELECT e_name
FROM extraPackages
WHERE e_price < 3000 AND e_modelkey = '104';

--7
SELECT b_name, b_price, m_name, m_price
FROM Brand, Model
WHERE b_brandkey = m_brandkey;

--8
SELECT m_name, e_name, e_price
FROM Model, extraPackages
WHERE m_modelkey = e_modelkey;

--9
SELECT c_address, vq_custkey, b_price
FROM Customer, verifiedQuote, Brand, estimatedQuote
WHERE c_custkey = vq_custkey
AND vq_quotekey = q_quotekey
AND q_brandkey = b_brandkey;

--10
SELECT b_price
FROM Brand
GROUP BY b_brandkey;

-- #11
SELECT c_phone
FROM Customer
WHERE c_phone Like '123%';

-- #12
SELECT c_ordernumber
FROM Customer
ORDER BY c_ordernumber;

-- #13
SELECT q_total, vq_total
FROM Customer, estimatedQuote, verifiedQuote
WHERE c_custkey = vq_custkey AND vq_quotekey = q_quotekey;

-- #14
SELECT e_name
FROM extraPackages, Model
WHERE m_name = 'Corolla'
AND m_modelkey = e_modelkey;

-- #15
SELECT c_name, vq_total
FROM customer, verifiedQuote
WHERE c_custkey = vq_custkey AND vq_total = 786585;

-- #16
SELECT m_name
FROM Model
WHERE m_weight = 3290;

-- #17
SELECT e_name, e_price
FROM extraPackages
WHERE e_price = 2750.00;

-- #18
SELECT vq_comments
FROM verifiedQuote
GROUP BY vq_comments;

-- #19
SELECT max(q_total), c_name
FROM estimatedQuote, Customer, verifiedQuote
WHERE q_quotekey = vq_quotekey
AND vq_custkey = c_custkey;

-- #20
SELECT Distinct c_name, b_name, m_name, e_name, vq_total
FROM Customer, Brand, Model, extraPackages, verifiedQuote, estimatedQuote
WHERE c_custkey = vq_custkey
AND vq_quotekey = q_quotekey
AND q_brandkey = b_brandkey
AND b_brandkey = m_brandkey
AND c_name = 'Kongo';

