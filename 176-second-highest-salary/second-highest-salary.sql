with distinct_salary as(
    select distinct salary from employee order by salary desc
)
select(select salary from distinct_salary limit 1 offset 1)as SecondHighestSalary;