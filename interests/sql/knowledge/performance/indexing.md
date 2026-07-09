Assumes: [setup.md](../../setup.md)

##### TABLE: sandbox.performance_indexing_a (table not containing an index)
```sql
DROP TABLE IF EXISTS sandbox.performance_indexing_a
;
CREATE TABLE performance_indexing_a (
	id INT NOT NULL,
	`name` VARCHAR(20)	
)
;
DROP PROCEDURE IF EXISTS sandbox.seed_performance_indexing_a
;
DELIMITER //
CREATE PROCEDURE sandbox.seed_performance_indexing_a()
BEGIN
	DECLARE i INT DEFAULT 1;
	
	WHILE i <= 2000 DO
		INSERT INTO sandbox.performance_indexing_a (
			id,
			`name`
		) VALUES (
			i,
			SUBSTRING(
				MD5(RAND()),
				1,
				5
			)
		);
		
		SET i = i + 1;
	END WHILE;
END
//
DELIMITER ;
CALL sandbox.seed_performance_indexing_a()
;
SELECT * FROM sandbox.performance_indexing_a
;
```

<br />

##### TABLE: sandbox.performance_indexing_b (table containing an index)
```sql
DROP TABLE IF EXISTS sandbox.performance_indexing_b
;
CREATE TABLE sandbox.performance_indexing_b (
	id INT NOT NULL AUTO_INCREMENT,
	`name` VARCHAR(20),
	PRIMARY KEY (id),
	INDEX index_name (`name`)
)
;
DROP PROCEDURE IF EXISTS sandbox.seed_performance_indexing_b
;
DELIMITER //
CREATE PROCEDURE sandbox.seed_performance_indexing_b()
BEGIN
	DECLARE i INT DEFAULT 1;
	
	WHILE i <= 2000 DO
		INSERT INTO sandbox.performance_indexing_b (
			`name`
		) VALUES (
			SUBSTRING(
				MD5(RAND()),
				1,
				5
			)
		);
		
		SET i = i + 1;
	END WHILE;
END
//
DELIMITER ;
CALL sandbox.seed_performance_indexing_b()
;
SELECT * FROM sandbox.performance_indexing_b ORDER BY id ASC
;
```

<br />

##### COMPARISON
```sql
SET @START := NOW(3)
;
SELECT * FROM sandbox.performance_indexing_a WHERE `name` = (
	SELECT `name` FROM sandbox.performance_indexing_a ORDER BY id DESC LIMIT 1
)
;
SET @END := NOW(3)
;
SET @DURATION_A = TIMESTAMPDIFF(
	MICROSECOND,
	@START,
	@END
) / 1000
;
SET @START := NOW(3)
;
SELECT * FROM sandbox.performance_indexing_b WHERE `name` = (
	SELECT `name` FROM sandbox.performance_indexing_b ORDER BY id DESC LIMIT 1
)
;
SET @END := NOW(3)
;
SET @DURATION_B = TIMESTAMPDIFF(
	MICROSECOND,
	@START,
	@END
) / 1000
;
SELECT
@DURATION_A AS performance_indexing_a,
@DURATION_B AS performance_indexing_b
;
```
<table caption="UnknownTable (1 rows)">
    <thead>
        <tr>
            <th class="col1">performance_indexing_a</th>
            <th class="col2">performance_indexing_b</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="col1">31.000000000</td>
            <td class="col2">22.000000000</td>
        </tr>
    </tbody>
</table>

For the most part, searching `performance_indexing_b` with a name will result in faster execution times because of the index: `INDEX index_name (name)`

> - PRIMARY KEY (id): Automatically creates a unique clustered index.
> - On table of `performance_indexing_b` the `INDEX index_name(name)` speeds up `WHERE name = ...`
> - Doing `UNIQUE INDEX` prevents duplicates and optimizes lookups.
> - There can only be one AUTO_INCREMENT column and it must be defined as a key.
