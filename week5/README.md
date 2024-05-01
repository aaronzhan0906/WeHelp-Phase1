### Task 2: Create database and table in your MySQL server

1. Create a new database named website.
```
CREATE DATABASE website;
SHOW DATABASES;
USE website;
```
![task2_1](https://github.com/aaronzhan0906/WeHelp-Phase1/blob/main/week5/screenshot/task2_1.png?raw=true)


2. Create a new table named member, in the website database, designed as below:
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
![task2_2](https://github.com/aaronzhan0906/WeHelp-Phase1/blob/main/week5/screenshot/task2_2.png?raw=true)

<br> 

---
### Task 3: SQL CRUD 
1.INSERT a new row to the member table where name, username and password must be set to test. INSERT additional 4 rows with arbitrary data.
```
INSERT INTO member (name, username, password) VALUES ('test', 'test', 'test');
INSERT INTO member (name, username, password, follower_count) VALUES
	('AAAAA', 'aaaaausername', '11111', 100),
	('BBBBB', 'bbbbbusername', '222222', 50),
	('CCCCC', 'cccccusername', '333', 75),
	('DDDDD', 'dddddusername', '44444444', 200);
```
![task3_1](https://github.com/aaronzhan0906/WeHelp-Phase1/blob/main/week5/screenshot/task3_1.png?raw=true)
![task3_2](https://github.com/aaronzhan0906/WeHelp-Phase1/blob/main/week5/screenshot/task3_2.png?raw=true)

2.SELECT all rows from the member table.
```
SELECT * FROM member;
```
![task3_2](https://github.com/aaronzhan0906/WeHelp-Phase1/blob/main/week5/screenshot/task3_2.png?raw=true)

3.SELECT all rows from the member table, in descending order of time.
```
SELECT * FROM member ORDER BY time DESC;
```
![task3_3](https://github.com/aaronzhan0906/WeHelp-Phase1/blob/main/week5/screenshot/task3_3.png?raw=true)

4.SELECT total 3 rows, second to fourth, from the member table, in descending order of time. Note: it does not mean SELECT rows where id are 2, 3, or 4.
```
SELECT * FROM member ORDER BY time DESC LIMIT 3 OFFSET 1;
```
![task3_4](https://github.com/aaronzhan0906/WeHelp-Phase1/blob/main/week5/screenshot/task3_4.png?raw=true)

5.SELECT rows where username equals to test.
```
SELECT * FROM member WHERE username = 'test';
```
![task3_5](https://github.com/aaronzhan0906/WeHelp-Phase1/blob/main/week5/screenshot/task3_5.png?raw=true)

6.SELECT rows where name includes the es keyword.
```
SELECT * FROM member WHERE name LIKE '%es%';
```
![task3_6](https://github.com/aaronzhan0906/WeHelp-Phase1/blob/main/week5/screenshot/task3_6.png?raw=true)

7.SELECT rows where both username and password equal to test.
```
SELECT * FROM member WHERE username = 'test' AND password = 'test';
```
![task3_7](https://github.com/aaronzhan0906/WeHelp-Phase1/blob/main/week5/screenshot/task3_7.png?raw=true)

8.UPDATE data in name column to test2 where username equals to test.
```
SET SQL_SAFE_UPDATES=0;
UPDATE member SET name='test2' WHERE username='test';
SELECT * FROM member;
```
![task3_8](https://github.com/aaronzhan0906/WeHelp-Phase1/blob/main/week5/screenshot/task3_8.png?raw=true)


<br> 

---
### Task 4: SQL Aggregation Functions
1.SELECT how many rows from the member table.
```
SELECT COUNT(*) FROM member;
```
![task4_1](https://github.com/aaronzhan0906/WeHelp-Phase1/blob/main/week5/screenshot/task4_1.png?raw=true)


2.SELECT the sum of follower_count of all the rows from the member table.
```
SELECT SUM(follower_count) FROM member;
```
![task4_2](https://github.com/aaronzhan0906/WeHelp-Phase1/blob/main/week5/screenshot/task4_2.png?raw=true)

3.SELECT the average of follower_count of all the rows from the member table.
```
SELECT AVG(follower_count) FROM member;
```
![task4_3](https://github.com/aaronzhan0906/WeHelp-Phase1/blob/main/week5/screenshot/task4_3.png?raw=true)

4.SELECT the average of follower_count of the first 2 rows, in descending order of follower_count, from the member table.
```
FROM (
	SELECT follower_count
	FROM member
	ORDER BY follower_count DESC
	LIMIT 2
) temp;
```
![task4_4](https://github.com/aaronzhan0906/WeHelp-Phase1/blob/main/week5/screenshot/task4_4.png?raw=true)



<br> 

---
### Task 5: SQL JOIN
1.Create a new table named message, in the website database. designed as below:
```
CREATE TABLE message (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  member_id BIGINT NOT NULL,
  content VARCHAR(255) NOT NULL,
  like_count INT UNSIGNED NOT NULL DEFAULT 0,
  time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (member_id) REFERENCES member(id)
);

INSERT INTO message (member_id, content, like_count) VALUES
(5, '這是第一條留言', 10),
(2, '這是第二條留言', 8),
(1, '這是第三條留言', 15),
(1, '這是第四條留言', 20),
(3, '這是第五條留言', 5);
```
![task5_1](https://github.com/aaronzhan0906/WeHelp-Phase1/blob/main/week5/screenshot/task5_1.png?raw=true)

2.SELECT all messages, including sender names. We have to JOIN the member table to get that.
```
SELECT message.id, member.username AS sender_name, message.content, message.like_count, message.time
FROM message
JOIN member ON message.member_id = member.id;
```
![task5_2](https://github.com/aaronzhan0906/WeHelp-Phase1/blob/main/week5/screenshot/task5_2.png?raw=true)

3.SELECT all messages, including sender names, where sender username equals to test. We have to JOIN the member table to filter and get that.
```
SELECT message.id, member.username AS sender_name, message.content, message.like_count, message.time
FROM message
JOIN member ON message.member_id = member.id
WHERE member.username = 'test';

```
![task5_3](https://github.com/aaronzhan0906/WeHelp-Phase1/blob/main/week5/screenshot/task5_3.png?raw=true)

4.Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages where sender username equals to test.
```
SELECT AVG(message.like_count) AS specific_sender_avg_like_count
FROM message
JOIN member ON message.member_id = member.id
WHERE member.username = 'test';
```
![task5_4](https://github.com/aaronzhan0906/WeHelp-Phase1/blob/main/week5/screenshot/task5_4.png?raw=true)

5.Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages GROUP BY sender username.
```
SELECT member.username AS sender_name, AVG(message.like_count) AS avg_like_count
FROM message
JOIN member ON message.member_id = member.id
GROUP BY member.username;
```
![task5_5](https://github.com/aaronzhan0906/WeHelp-Phase1/blob/main/week5/screenshot/task5_5.png?raw=true)
