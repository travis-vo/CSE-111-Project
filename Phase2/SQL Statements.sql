-- #11
SELECT c_phone
FROM Customer
WHERE c_phone Like '%number%';

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
WHERE m_name = 'mname1';

-- #15
SELECT c_name, vq_total
FROM customer, verifiedQuote
WHERE c_custkey = vq_custkey AND vq_total = 'vqtotal4';

-- #16
SELECT m_name
FROM Model
WHERE m_weight = 'weight1';

-- #17
SELECT e_name, e_price
FROM extraPackages
WHERE e_price = 'eprice3';

-- #18
SELECT vq_comments
FROM verifiedQuote
GROUP BY vq_comments;

-- #19
SELECT max(q_total), c_name
FROM estimatedQuote, Customer, verifiedQuote
WHERE q_quotekey = vq_quotekey AND vq_custkey = c_custkey;

-- #20
SELECT c_name, b_name, m_name, e_name, vq_total
FROM Customer, Brand, Model, extraPackages, verifiedQuote, estimatedQuote
WHERE c_custkey = vq_custkey AND vq_quotekey = q_quotekey AND q_brandkey = b_brandkey AND b_brandkey = m_brandkey AND c_name = 'Kongo';