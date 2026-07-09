> **ATTENTION**
> 
> "FULL JOIN" is not supported in MySQL.
>
> Supported databases inclued: PostgreSQL, Microsoft SQL Server, Oracle, Snowflake, and IBM Db2.

```sql

SELECT
c.id AS customer_id,
c.`name`,
o.id AS order_id,
o.product
FROM sandbox.customers AS c

LEFT JOIN sandbox.orders AS o
ON o.customer_id = c.id

WHERE o.customer_id IS NULL

UNION

SELECT
c.id AS customer_id,
c.`name`,
o.id AS order_id,
o.product
FROM sandbox.customers AS c

RIGHT JOIN sandbox.orders AS o
ON o.customer_id = c.id

WHERE c.id IS NULL
;
```
<table caption="customers (8 rows)">
    <thead>
        <tr>
            <th class="col1">customer_id</th>
            <th class="col2">name</th>
            <th class="col3">order_id</th>
            <th class="col4">product</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="col1">4</td>
            <td class="col2">6ab19</td>
            <td class="col3"></td>
            <td class="col4"></td>
        </tr>
        <tr>
            <td class="col1">5</td>
            <td class="col2">093cf</td>
            <td class="col3"></td>
            <td class="col4"></td>
        </tr>
        <tr>
            <td class="col1">6</td>
            <td class="col2">79ffe</td>
            <td class="col3"></td>
            <td class="col4"></td>
        </tr>
        <tr>
            <td class="col1">7</td>
            <td class="col2">7649b</td>
            <td class="col3"></td>
            <td class="col4"></td>
        </tr>
        <tr>
            <td class="col1">8</td>
            <td class="col2">fe5ec</td>
            <td class="col3"></td>
            <td class="col4"></td>
        </tr>
        <tr>
            <td class="col1">9</td>
            <td class="col2">ba813</td>
            <td class="col3"></td>
            <td class="col4"></td>
        </tr>
        <tr>
            <td class="col1">10</td>
            <td class="col2">7e7b6</td>
            <td class="col3"></td>
            <td class="col4"></td>
        </tr>
        <tr>
            <td class="col1"></td>
            <td class="col2"></td>
            <td class="col3">4</td>
            <td class="col4">2a649e9b89</td>
        </tr>
    </tbody>
</table>

> The above returns all unique rows from both tables where there is no match.
