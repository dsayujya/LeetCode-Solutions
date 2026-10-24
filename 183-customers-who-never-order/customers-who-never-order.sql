-- Write your PostgreSQL query statement below
select c.name as Customers from customers c left join orders o ON c.id = o.customerId where o.id is null;