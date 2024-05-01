### Task 2: Create database and table in your MySQL server

1.Create a new database named website.
```
CREATE DATABASE website;
SHOW DATABASES;
USE website;
```
![task2_1](/screenshot/task2_1.png)
---
---
```
CREATE TABLE member (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  username VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  follower_count INT UNSIGNED NOT NULL DEFAULT 0,
  time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```
2.Create a new table named member, in the website database, designed as below:
![task2_2](/screenshot/task2_2.png)

---

### Task 3: SQL CRUD 
