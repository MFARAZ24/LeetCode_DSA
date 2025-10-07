select customer_id, count(customer_id)as count_no_trans
from Visits
where visit_id NOT IN(
    select visit_id
    from Transactions
)
GROUP BY customer_id