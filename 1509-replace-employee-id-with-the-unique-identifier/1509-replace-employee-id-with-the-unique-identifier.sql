# Write your MySQL query statement below
select unique_id, name
from EMployeeUNI as uid
right join Employees as em on uid.id = em.id;