```sql
SELECT
a.`name` AS employee,
b.`name` AS manager
FROM sandbox.employees AS a

JOIN sandbox.employees AS b
ON b.id = a.manager_id
;
```

<table caption="employees (3 rows)">
    <thead>
        <tr>
            <th class="col1">employee</th>
            <th class="col2">manager</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="col1">3cf6d</td>
            <td class="col2">83949</td>
        </tr>
        <tr>
            <td class="col1">b89a0</td>
            <td class="col2">83949</td>
        </tr>
        <tr>
            <td class="col1">6db09</td>
            <td class="col2">83949</td>
        </tr>
    </tbody>
</table>

> Returns all records where an employee has a manager.
