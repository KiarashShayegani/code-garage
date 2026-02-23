-- Let's see stocks records with their change percentage added(only the ones which moved more than 10%)
SELECT ticker, date, open, close, (((open - close)/open)*100) AS change
FROM stock_prices
WHERE ((((open - close)/open)*100) >= 10 OR (((open - close)/open)*100) <= -10)
ORDER BY change DESC;

-- Counting the Big Mover Months for stocks:
SELECT ticker, count(*) AS big_mover_months --count((((open - close)/open)*100)) as big_mover_months   PATHETIC!
FROM stock_prices
WHERE ((((open - close)/open)*100) >= 10 OR (((open - close)/open)*100) <= -10)
GROUP BY ticker
ORDER BY big_mover_months DESC;
