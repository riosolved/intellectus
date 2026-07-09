### CHALLENGE

Find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table.
The STATION table is described as follows:
<table>
  <thead>
    <tr>
      <th colspan="2">STATION</th>
    </tr>
    <tr>
      <th>Field</th>
      <th>Type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ID</td>
      <td>NUMBER</td>
    </tr>
    <tr>
      <td>CITY</td>
      <td>VARCHAR2(21)</td>
    </tr>
    <tr>
      <td>STATE</td>
      <td>VARCHAR2(2)</td>
    </tr>
    <tr>
      <td>LAT_N</td>
      <td>NUMBER</td>
    </tr>
    <tr>
      <td>LONG_W</td>
      <td>NUMBER</td>
    </tr>
  </tbody>
</table>

Where LAT_N is the northern latitude and LONG_W is the western longitude.

For example, if there are three records in the table with CITY values 'New York', 'New York', 'Bengalaru', there are 2 different city names: 'New York' and 'Bengalaru'. The query returns 1, because Total Number of Records - number of unique city names = 3 - 2 = 1.

### SOLUTION 
```sql
SELECT
    DATA._ALL - DATA._DISTINCT AS DIFFERENCE
FROM (
    SELECT (
        SELECT
            COUNT(*)
        FROM STATION
    ) AS _ALL,
    (
        SELECT
            COUNT(
                DISTINCT(CITY)
            )
        FROM STATION
    ) AS _DISTINCT
) AS DATA
;
```