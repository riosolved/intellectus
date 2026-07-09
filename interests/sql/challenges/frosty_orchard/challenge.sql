/* STORY
A frosty orchard grows apples and pears. Each fruit has a type, a price, and a harvest date.
The orchard keeper tracks sales in a separate table, recording which fruits were sold and when.
Some fruits are sold multiple times, and some fruits have not yet been sold.
The keeper wants to know how much revenue each fruit type generated, and how many times each was sold.

YOUR TASK
1. Write a query that returns the fruit type, total revenue (price * quantity sold), and number of sales for each fruit type.
2. Only include fruit types that have at least one sale.
3. Order the results by total revenue descending.
4. The query must use a JOIN between the fruits and sales tables.
5. The query must GROUP BY fruit type.

DATA AND EXPECTED RESULT
CREATE TABLE fruits (
    id INTEGER PRIMARY KEY,
    name TEXT,
    type TEXT,
    price REAL
);

CREATE TABLE sales (
    id INTEGER PRIMARY KEY,
    fruit_id INTEGER,
    quantity INTEGER,
    sale_date DATE
);

INSERT INTO fruits (id, name, type, price) VALUES
(1, 'Red Apple', 'apple', 2.5),
(2, 'Green Pear', 'pear', 3.0),
(3, 'Yellow Apple', 'apple', 2.0);

INSERT INTO sales (id, fruit_id, quantity, sale_date) VALUES
(1, 1, 5, '2024-01-01'),
(2, 1, 3, '2024-01-02'),
(3, 2, 2, '2024-01-03');

EXPECTED RESULT:
type    | total_revenue | count_of_sales
--------|---------------|---------------
apple   | 20.0          | 2
pear    | 6.0           | 1

BACKGROUND
The key idea here is to combine data from two tables using a JOIN.
A JOIN connects rows from one table with matching rows in another table.
In this case, the sales table has a fruit_id column that references the id column in the fruits table.
This allows us to link each sale to its corresponding fruit.
We need to group the results by fruit type to calculate totals per type.
GROUP BY is essential when aggregating data; without it, we can't compute per-type totals.
The total revenue for a fruit type is calculated by summing (price * quantity) for all sales of that type.
COUNT(*) or COUNT(sale_id) counts how many sales occurred for each type.
ORDER BY ensures the results are sorted correctly.
A common mistake is to forget to filter out fruits with no sales — this leads to incorrect totals or missing rows.

HINTS
1. Remember to join the tables on the correct columns.
2. You'll need to multiply price by quantity for revenue calculation.
3. Use GROUP BY and aggregate functions like SUM and COUNT.
4. Make sure you're only including fruit types that have been sold at least once.
*/