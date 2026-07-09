```sql
SELECT *
FROM sandbox.customers AS c

RIGHT JOIN sandbox.orders AS o
ON o.customer_id = c.id

WHERE c.id IS NULL
;
```
<table caption="customers (1 rows)">
    <thead>
        <tr>
            <th class="col1">id</th>
            <th class="col2">name</th>
            <th class="col3">email</th>
            <th class="col4">id</th>
            <th class="col5">customer_id</th>
            <th class="col6">product</th>
            <th class="col7">order_date</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="col1"></td>
            <td class="col2"></td>
            <td class="col3"></td>
            <td class="col4">4</td>
            <td class="col5"></td>
            <td class="col6">2a649e9b89</td>
            <td class="col7">2025-05-15</td>
        </tr>
    </tbody>
</table>

> Retrieves all orders, only if they are not associated to a customer.
