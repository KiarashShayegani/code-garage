  WITH total_deposits as (  
    SELECT account_id, sum(amount) as sum_deposit
    FROM transactions
    WHERE transaction_type = 'Deposit'
    GROUP BY account_id
), total_withdraw  AS (
    SELECT account_id, sum(amount) as sum_withdraw
    FROM transactions
    WHERE transaction_type = 'Withdrawal'
    GROUP BY account_id
)


SELECT dep.account_id, (dep.sum_deposit - wit.sum_withdraw) as final_balance
FROM total_deposits as dep 
INNER JOIN total_withdraw as wit ON dep.account_id = wit.account_id;
