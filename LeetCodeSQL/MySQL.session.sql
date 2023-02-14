
--@block
show databases;

--@block
use db1;


-- 196. Delete Duplicate Emails
--@block
Create table If Not Exists Person (Id int, Email varchar(255));
Truncate table Person;
insert into Person (id, email) values ('1', 'john@example.com');
insert into Person (id, email) values ('2', 'bob@example.com');
insert into Person (id, email) values ('3', 'john@example.com');

--@block
select * from person;

--@block
delete p1 
from person p1, person p2
where p1.email = p2.email and p1.id > p2.id;

--@block
SELECT * FROM person;

-- 197. Rising Temperature
--@block
Create table If Not Exists Weather (id int, recordDate date, temperature int);
Truncate table Weather;
insert into Weather (id, recordDate, temperature) values ('1', '2015-01-01', '10');
insert into Weather (id, recordDate, temperature) values ('2', '2015-01-02', '25');
insert into Weather (id, recordDate, temperature) values ('3', '2015-01-03', '20');
insert into Weather (id, recordDate, temperature) values ('4', '2015-01-04', '30');

--@block
select * from weather;

--@block
select x.id from weather x,weather y where x.temperature>y.temperature and datediff(x.recordDate,y.recordDate)=1;

