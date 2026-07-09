> **ATTENTION**
> 
> "FULL JOIN" is not supported in MySQL.
>
> Supported databases inclued: PostgreSQL, Microsoft SQL Server, Oracle, Snowflake, and IBM Db2.

We must emulate a FULL JOIN in MySQL.
```sql
SELECT
c.id AS customer_id,
c.`name`,
o.id AS order_id,
o.product
FROM sandbox.customers AS c

LEFT JOIN sandbox.orders AS o
ON o.customer_id = c.id

UNION

SELECT
c.id AS customer_id,
c.`name`,
o.id AS order_id,
o.product
FROM sandbox.customers AS c

RIGHT JOIN sandbox.orders AS o
ON o.customer_id = c.id
;
```
<table caption="customers (11 rows)">
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
            <td class="col1">1</td>
            <td class="col2">48cf5</td>
            <td class="col3">1</td>
            <td class="col4">49dcc5e912</td>
        </tr>
        <tr>
            <td class="col1">2</td>
            <td class="col2">1746b</td>
            <td class="col3">2</td>
            <td class="col4">7ec76ce3c9</td>
        </tr>
        <tr>
            <td class="col1">3</td>
            <td class="col2">9ea07</td>
            <td class="col3">3</td>
            <td class="col4">902688e1e4</td>
        </tr>
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

The above returns all unique rows from both tables, matched or not. Filling in NULLs when there's no match.
- LEFT JOIN gives us all customers, including those without orders.
- RIGHT JOIN gives us all orders, including those with no matching customer.
- UNION combines both result sets, effectively simulating a FULL JOIN.

> **NOTE**
> 
> UNION will remove duplicates.
>
> Using UNION ALL we can prevent duplicates being removed, thus giving us all records.
