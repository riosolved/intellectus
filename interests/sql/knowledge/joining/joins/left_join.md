```sql
SELECT *
FROM sandbox.customers AS c

LEFT JOIN sandbox.orders AS o
ON o.customer_id = c.id
;
```

<table caption="customers (10 rows)">
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
            <td class="col6">e5e7cbcfd2</td>
            <td class="col7">2025-05-15</td>
        </tr>
        <tr>
            <td class="col1">2</td>
            <td class="col2">1746b</td>
            <td class="col3">118c6@e2dba.com</td>
            <td class="col4">2</td>
            <td class="col5">2</td>
            <td class="col6">e5e7cbcfd2</td>
            <td class="col7">2025-05-15</td>
        </tr>
        <tr>
            <td class="col1">3</td>
            <td class="col2">9ea07</td>
            <td class="col3">638dd@d00d3.com</td>
            <td class="col4">3</td>
            <td class="col5">3</td>
            <td class="col6">e5e7cbcfd2</td>
            <td class="col7">2025-05-15</td>
        </tr>
        <tr>
            <td class="col1">4</td>
            <td class="col2">6ab19</td>
            <td class="col3">50d88@7453d.com</td>
            <td class="col4"></td>
            <td class="col5"></td>
            <td class="col6"></td>
            <td class="col7"></td>
        </tr>
        <tr>
            <td class="col1">5</td>
            <td class="col2">093cf</td>
            <td class="col3">d5b59@1dece.com</td>
            <td class="col4"></td>
            <td class="col5"></td>
            <td class="col6"></td>
            <td class="col7"></td>
        </tr>
        <tr>
            <td class="col1">6</td>
            <td class="col2">79ffe</td>
            <td class="col3">2f341@98516.com</td>
            <td class="col4"></td>
            <td class="col5"></td>
            <td class="col6"></td>
            <td class="col7"></td>
        </tr>
        <tr>
            <td class="col1">7</td>
            <td class="col2">7649b</td>
            <td class="col3">f799f@d2624.com</td>
            <td class="col4"></td>
            <td class="col5"></td>
            <td class="col6"></td>
            <td class="col7"></td>
        </tr>
        <tr>
            <td class="col1">8</td>
            <td class="col2">fe5ec</td>
            <td class="col3">cca89@53dc0.com</td>
            <td class="col4"></td>
            <td class="col5"></td>
            <td class="col6"></td>
            <td class="col7"></td>
        </tr>
        <tr>
            <td class="col1">9</td>
            <td class="col2">ba813</td>
            <td class="col3">eef72@f045a.com</td>
            <td class="col4"></td>
            <td class="col5"></td>
            <td class="col6"></td>
            <td class="col7"></td>
        </tr>
        <tr>
            <td class="col1">10</td>
            <td class="col2">7e7b6</td>
            <td class="col3">c5c26@249d4.com</td>
            <td class="col4"></td>
            <td class="col5"></td>
            <td class="col6"></td>
            <td class="col7"></td>
        </tr>
    </tbody>
</table>

> Retrieves all customers, even if they did not place an order.
