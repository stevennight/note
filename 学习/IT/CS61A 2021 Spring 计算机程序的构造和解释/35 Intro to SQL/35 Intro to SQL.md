# 35 Intro to SQL

## 数据库
关系型数据库(relational database)：每种类型的数据存储在表(table)中。每个表有行(row)和列(column)。

通常每个表都会有一个id，为了能够准确引用（通常是仅有的能保证唯一不变的值）。

密码保存通常是加盐哈希值 salted hashed password

### 关联表 Relating Tables
两个表关联

例：<br />
user, badges, user_badges(两个表id关联)<br />
多对多关联：一用户可以有多个得分，多个用户也可以有一个同样的得分。

## SQL
是一种声明式编程语言。

注：课程中使用SQLite来说明。可能与MySQL等其他数据库不一样。
其他数据库：MySQL, PostGreSQL. BigQuery【数据分析】
```sql
CREATE TABLE users (id INTEGER PRIMARY KEY, nickname TEXT, location TEXT);

INSERT INTO users VALUES (1, "Sal", "California");
INSERT INTO users (nickname, location) VALUES ("John", "NY");

UPDATE users SET nickname = "Joan" WHERE id = 2;

DELETE FROM users WHERE id = 2;

SELECT * FROM users;
SELECT * FROM users ORDER BY nickname ASC;
SELECT nickname FROM users;
SELECT * FROM users WHERE nickname = "John" AND location = "California";

/* 聚合 */
CREATE TABLE groceries (id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER, aisle INTEGER);
INSERT INTO groceries VALUES (1, "Bananas", 56, 7);

SELECT MAX(quantity), name, aisle FROM groceries;
SELECT MIN(quantity), name, aisle FROM groceries;
SELECT AVG(quantity) FROM groceries;
SELECT SUM(quantity) FROM groceries;
SELECT COUNT(*) FROM groceries;

SELECT SUM(quantity), aisle FROM groceries GROUP BY aisle;

/* Join */
SELECT * FROM students;
SELECT * FROM student_projects;

SELECT first_name, last_name, title FROM students
    JOIN student_projects ON students.id = student_projects.student_id;
SELECT first_name, last_name, title FROM students
    LEFT OUTER JOIN student_projects ON students.id = student_projects.student_id;
```

### SQL用途
1. 应用程序数据存储
2. 数据分析

### 事务
```sql
BEGIN;

UPDATE products SET quantity = quantity - 1 WHERE id = 1;

INSERT INTO orders (customer, product_id) VALUES ("Animesh", 1);

COMMIT;
```

## Python Web开发
ORM对象关系管理器：ORM object relational manager 开发通常不直接写SQL。
直接SQL要注意SQL注入(SQL Injection)。

框架 Flask

装饰器 decorator @app.route 处理网址路径