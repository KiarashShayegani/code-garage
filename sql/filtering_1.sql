SELECT * FROM customers
WHERE (age BETWEEN 18 AND 22)
AND (state IN ('Victoria','Tasmania','Queensland'))
AND (gender <> 'n/a')
AND (customer_name LIKE 'A%' OR customer_name LIKE 'B%'); 

-- Another filtering example on customers table(subquery):
SELECT max(counter) AS maximum_female_customers_in_a_state
FROM
(
SELECT state, gender, count(customer_id) as counter
FROM customers
WHERE (age >= 18)
AND (gender = 'Female')
GROUP BY state, gender
ORDER BY state
) 
AS maximum_customers;
