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
```sql
CREATE TABLE users (id INTEGER PRIMARY KEY, nickname TEXT, location TEXT);

INSERT INTO users VALUES (1, "Sal", "California");
INSERT INTO users (nickname, location) VALUES ("John", "NY");

SELECT * FROM users;
SELECT * FROM users ORDER BY nickname ASC;
```