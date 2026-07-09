
```sql
SELECT *
FROM sandbox.customers AS c

RIGHT JOIN sandbox.orders AS o
ON o.customer_id = c.id
;
```

<table caption="customers (4 rows)">
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
            <td class="col1">1</td>
            <td class="col2">48cf5</td>
            <td class="col3">574f3@6b706.com</td>
            <td class="col4">1</td>
            <td class="col5">1</td>
            <td class="col6">49dcc5e912</td>
            <td class="col7">2025-05-15</td>
        </tr>
        <tr>
            <td class="col1">2</td>
            <td class="col2">1746b</td>
            <td class="col3">118c6@e2dba.com</td>
            <td class="col4">2</td>
            <td class="col5">2</td>
            <td class="col6">7ec76ce3c9</td>
            <td class="col7">2025-05-15</td>
        </tr>
        <tr>
            <td class="col1">3</td>
            <td class="col2">9ea07</td>
            <td class="col3">638dd@d00d3.com</td>
            <td class="col4">3</td>
            <td class="col5">3</td>
            <td class="col6">902688e1e4</td>
            <td class="col7">2025-05-15</td>
        </tr>
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

> Retrieves all orders, even if they are not associated to a customer.
