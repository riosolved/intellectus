```sql
SELECT *
FROM sandbox.orders AS o

INNER JOIN sandbox.customers AS c
ON c.id = o.customer_id
;
```

<table caption="orders (3 rows)">
    <thead>
        <tr>
            <th class="col1">id</th>
            <th class="col2">customer_id</th>
            <th class="col3">product</th>
            <th class="col4">order_date</th>
            <th class="col5">id</th>
            <th class="col6">name</th>
            <th class="col7">email</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="col1">1</td>
            <td class="col2">1</td>
            <td class="col3">e5e7cbcfd2</td>
            <td class="col4">2025-05-15</td>
            <td class="col5">1</td>
            <td class="col6">48cf5</td>
            <td class="col7">574f3@6b706.com</td>
        </tr>
        <tr>
            <td class="col1">2</td>
            <td class="col2">2</td>
            <td class="col3">e5e7cbcfd2</td>
            <td class="col4">2025-05-15</td>
            <td class="col5">2</td>
            <td class="col6">1746b</td>
            <td class="col7">118c6@e2dba.com</td>
        </tr>
        <tr>
            <td class="col1">3</td>
            <td class="col2">3</td>
            <td class="col3">e5e7cbcfd2</td>
            <td class="col4">2025-05-15</td>
            <td class="col5">3</td>
            <td class="col6">9ea07</td>
            <td class="col7">638dd@d00d3.com</td>
        </tr>
    </tbody>
</table>

> Fetching all orders with an associated customer, excluding rows from either table where no matches exist.
