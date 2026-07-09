# SETUP
The following are a set of SQL commands for setting up the sandbox environment. This is required before executing any additional commands within the SQL exercises space. 

##### DATABASE
Setup:
```sql
CREATE DATABASE IF NOT EXISTS sandbox;
```

Dispose:
```sql
DROP DATABASE IF EXISTS sandbox;
```

<br />

##### TABLE: CUSTOMER
Setup:
```sql
CREATE TABLE sandbox.customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(50),
    email VARCHAR(100)
)
;
DELIMITER //
CREATE PROCEDURE seed_customers()
BEGIN
    DECLARE i INT DEFAULT 1;
    DECLARE `name` VARCHAR(50) DEFAULT '';
    DECLARE email VARCHAR(100) DEFAULT '';

    WHILE i <= 10 DO
        SET `name` = SUBSTRING(
            MD5(RAND()),
            1,
            5
        );
        
        set email = CONCAT(
            SUBSTRING(
                MD5(RAND()),
                    1,
                    5
            ),
            '@',
            SUBSTRING(
                MD5(RAND()),
                    1,
                    5
            ),
            '.com'		
        );
    
        INSERT INTO sandbox.customers (
            `name`,
            email
        ) VALUES (
            `name`,
            email
        );
        
        SET i = i + 1;	
    END WHILE;
END
//
DELIMITER ;
CALL seed_customers()
;
SELECT * FROM sandbox.customers
;
```

Dispose:
```sql
DROP TABLE IF EXISTS sandbox.customers;
DROP PROCEDURE IF EXISTS sandbox.seed_customers;
```

<br />

##### TABLE: ORDERS
Setup:
```sql
CREATE TABLE sandbox.orders (
	id INT AUTO_INCREMENT PRIMARY KEY,
	customer_id INT,
	product VARCHAR(100),
	order_date DATE,
	FOREIGN KEY (customer_id) REFERENCES sandbox.customers(id)
)
;
DELIMITER //
CREATE PROCEDURE seed_orders()
BEGIN
	INSERT INTO sandbox.orders (
		customer_id,
		product,
		order_date
	)
	SELECT id, (
		SUBSTRING(
			MD5(RAND()),
			1,
			10
		)
	), CURDATE()
	FROM sandbox.customers AS c
	ORDER BY c.id
	LIMIT 3;

	INSERT INTO sandbox.orders (
		product,
		order_date
	) VALUES (
		SUBSTRING(
			MD5(RAND()),
			1,
			10
		),
		CURDATE()
	);
END
//
DELIMITER ;
CALL seed_orders()
;
SELECT * FROM sandbox.orders
;
```

Dispose:
```sql
DROP TABLE IF EXISTS sandbox.orders;
DROP PROCEDURE IF EXISTS sandbox.seed_orders;
```

<br />

##### TABLE: EMPLOYEES
Setup:
```sql
CREATE TABLE sandbox.employees (
	id INT AUTO_INCREMENT PRIMARY KEY,
	`name` VARCHAR(50),
	manager_id INT DEFAULT NULL,
	FOREIGN KEY (manager_id) REFERENCES sandbox.employees(id)
)
;
DELIMITER //
CREATE PROCEDURE seed_employees()
BEGIN
	DECLARE i INT DEFAULT 1;
	DECLARE `name` VARCHAR(100) DEFAULT '';
	
	WHILE i<= 10 DO
		SET `name` = SUBSTRING(
			MD5(RAND()),
			1,
			5
		);
		
		INSERT INTO sandbox.employees (
			`name`
		) VALUES (
			`name`
		);
		
		SET i = i + 1;
	END WHILE;
	
	SET i = 0;

	# NOTE : CREATE IN-TABLE RELATIONSHIPS
	WHILE i < 3 DO
		UPDATE sandbox.employees
		SET manager_id = 1
		WHERE id = (
			SELECT id
			FROM sandbox.employees
			ORDER BY id DESC
			LIMIT i, 1
		);

		SET i = i + 1;
	END WHILE;
END
//
DELIMITER ;
CALL seed_employees()
;
SELECT * FROM sandbox.employees
;
```

Dispose:
```sql
DROP TABLE IF EXISTS sandbox.employees;
DROP PROCEDURE IF EXISTS sandbox.seed_employees;
```

<br />
