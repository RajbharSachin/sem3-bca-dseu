show databases;
use mysql;
create database mydb;
show tables;
select database();
create table student
	(
	student int,
	fname varchar(20),
	lname varchar(20),
	marks int
	);
desc student;
alter table student rename to student123;
desc student123;
alter table student123 rename column fname to firstname;
desc student123;
alter table student123 add grade char(1);
desc student123;
alter table student123 modify grade varchar(20);
desc student123;
alter table student123 drop column lname;
desc student123;
create table copy_st as select * from student123;
desc copy_st;
drop table student123;
show tables;
create database employeedb;
show databases;
use employeedb;
create table emp (id int varchar(15),salary float ,dept_name varchar(15), phone bigint, dept_id int, date_of_joining int);
show tables;
insert into emp values (1001, "Sachin", 27000, "BCA", 87662, 1100 , 2003);
select * from emp;
insert into emp (id,name,salary,dept_name,phone,dept_id,date_of_joining) values (1002,"Sachin_R",30000,"BCA",828589,1100,2002);
select * from emp;
insert into emp (id,name,dept_name,phone,dept_id,date_of_joining) values (1002,"Sachin_R","BCA",828589,1100,2002);
select * from emp where salary is NULL;
select * from emp where phone is NOT NULL;
select distinct id,salary from emp;
select distinct id,name from emp;
select count(*) from emp;
select distinct count(*) as cnt from emp group by * having count(*)>1;
select distinct count(*) from emp;
select * from emp;
use employeedb;
show tables;
select * from emp;
create table emp (id int ,name varchar(15),salary float ,dept_name varchar(15), phone bigint, dept_id int, date_of_joining int);
delete from emp where salary=NULL;
alter table emp ADD primary key(id);
insert into emp (id,name,salary,dept_name,phone,dept_id,date_of_joining) values (1057,"Harsh_K",80000,"BCA",97175,1100,2003);
insert into emp (id,name,salary,dept_name,phone,dept_id,date_of_joining) values (1045,"Ritik",100000,"BCA",97205,1100,2003);
insert into emp (id,name,salary,dept_name,phone,dept_id,date_of_joining) values (1136,"Shlok",30000,"BCA",88574,1100,2002);
alter table emp modify COLUMN id int PRIMARY KEY;
desc emp;
create table department (Dept_id int ,D_name varchar(15), id  int references emp(id));
desc department;
alter table department ADD foreign key (id) references emp (id);
select * from department;
select * from emp;

create table copy_emp as select * from emp;
update copy_emp set salary=salary+1000;
select * from copy_emp;
insert into copy_emp (id,name,salary,dept_name,phone,dept_id,date_of_joining) values (1136,"james",30000,"BCA",88574,1100,2002);
insert into copy_emp (id,name,salary,dept_name,phone,dept_id,date_of_joining) values (10,"fotty",90000,"Diploma",568271,1100,2002);
desc copy_emp;
update copy_emp set dept_name="electrical" where name="james";
update copy_emp set phone=123456, dept_id=20 where id=10;
truncate table copy_emp;
drop table copy_emp;

select min(salary) as salary_min from emp ;
select max(salary) as salary_max from emp ;
select sum(salary) as salary_sum from emp ;
select avg(salary) as salary_avg from emp ;
select count(salary) as salary_count from emp;

delete from emp where id=1136;
delete from emp where id=1057;
desc emp;

delete from department where id=1057;
select * from department;
delete from emp where id=1057;

select * from emp order by name asc;


alter table emp add location varchar(20);
insert into emp (id,name,salary,dept_name,phone,dept_id,date_of_joining,location) values (10,"fotty",90000,"IT",568271,1100,2002,"Delhi");
insert into emp (id,name,salary,dept_name,phone,dept_id,date_of_joining,location) values (11,"shyam",30000,"CSE",568271,1100,2002,"Delhi");
insert into emp (id,name,salary,dept_name,phone,dept_id,date_of_joining,location) values (11,"shyam",30000,"CSE",568271,1100,2002,"Delhi"),(12,"rahul",60000,"IT",568271,1100,2002,"Mumbai");
select * from emp where dept_name = "IT" AND location = "Delhi";
insert into department values(1100,"BCA",1001);
insert into department values(1100,"BCA",1045);
insert into department values(1100,"IT",10);
insert into department values(1100,"CSE",11);
insert into department values(1100,"IT",12);

select * from emp where location IS NULL;
select * from emp where location IS NOT NULL;

select * from emp LIMIT 3;

select * from emp where name LIKE 's%';
select * from emp where name LIKE '_h%';

select * from emp where location IN ("delhi");
select * from emp where location NOT IN ("delhi");














create database dseu;
use dseu;

create table dseu_student
	(
	rollno int,
	fname varchar(20),
	lname varchar(20),
	marks int
	);
select * from dseu_student;

insert into dseu_student values (1057, "Harsh", "Kumar", 49);
insert into dseu_student values (1055, "Harjeet", "yadav", 50);

desc dseu_student; 


SELECT id FROM emp UNION SELECT D_name FROM Department;
SELECT emp.id, department.D_name, emp.phone FROM emp INNER JOIN department ON emp.dept_name=department.D_name;
SELECT * FROM emp LEFT JOIN department ON emp.dept_name=department.D_name;
SELECT emp.id, department.D_name, emp.phone FROM emp LEFT JOIN department ON emp.dept_name=department.D_name;
SELECT emp.id, department.D_name, emp.phone FROM emp RIGHT JOIN department ON emp.dept_name=department.D_name;

SELECT * FROM emp FULL JOIN department ON emp.dept_id=department.Dept.id;
SELECT emp.id, department.D_name, emp.phone FROM emp RIGHT JOIN department ON emp.dept_name=department.D_name
UNION ALL
SELECT emp.id, department.D_name, emp.phone FROM emp RIGHT JOIN department ON emp.dept_name=department.D_name;


create table course
	(
	course_id int,
	roll_no int
	);
create table student
	(
	roll_no int,
	name varchar(20),
	state varchar(20),
	phone_no int,
    age int
	);
insert into course values (1,1),(2,2),(2,3),(3,4),(4,5),(4,6),(4,7),(5,8);
insert into student values (1, "Ratan", "delhi", 495323,56),(2, "Ritik", "new delhi", 2586,19),(3, "sachin", "u p", 4953,20),(4, "harsh", "bihar", 1234,20),(5, "karmvir", "dhansa", 789453,19),(6, "sachink", "delhi", 895423,10),(7, "saloni", "new delhi", 754525,19),(8, "ashish", "bihar", 95323,19);
SELECT * from course;
SELECT * from student;
desc course;
desc student;
SELECT course.course_id, student.name, student.phone_no FROM course INNER JOIN student ON course.course_id = student.roll_no;
SELECT course.course_id, student.name, student.phone_no FROM course LEFT JOIN student ON course.course_id = student.roll_no;
SELECT course.course_id, student.name, student.phone_no FROM course RIGHT JOIN student ON course.course_id = student.roll_no;
SELECT course.course_id, student.name, student.phone_no FROM course FULL JOIN student ON course.course_id = student.roll_no;
SELECT course.course_id, student.name, student.phone_no FROM course LEFT JOIN student ON course.course_id = student.roll_no
UNION ALL
SELECT course.course_id, student.name, student.phone_no FROM course LEFT JOIN student ON course.course_id = student.roll_no;

create database GeneralStore;
use GeneralStore;
create table Customer
	(
	Cust_id int Primary key,
	Cust_name varchar(30)
    );
create table Item
	(
	Item_id int Primary key,
	Item_name varchar(30),
    Price float
    );
create table Sale
	(
	bill_no int Primary key,
	bill_date date,
    cust_id int,
    item_id int,
    qty_sold int,
    foreign key(cust_id) references customer(cust_id),
    foreign key(item_id) references item(item_id)
    );
    
desc sale;
desc item;
desc customer;
insert into sale values (1000,'2022-09-20',1,101,50),(1001,'2022-09-20',2,102,50),(1002,'2022-09-20',3,103,50),(1003,'2022-09-20',3,104,5),(1004,'2022-11-30',4,105,10),(1005,'2022-11-29',5,106,100),(1006,'2022-11-28',6,107,87),(1007,'2022-11-26',7,108,12),(1008,'2022-11-27',8,109,19),(1009,'2022-11-26',9,110,15),(1010,'2022-12-06',10,111,5);
insert into item values (101,"science",100),(102,"maths",202.454),(103,"DBMS",500),(104,"computer network",199.63),(105,"political science",200),(106,"history",150),(107,"english",1500),(108,"python",565),(109,"hacking",852),(110,"tourism",850),(111,"sanskrit",851);
insert into customer values (1,"ratan"),(2,"ritik"),(3,"sachin"),(4,"karmvir"),(5,"Aaditya"),(6,"Ashish"),(7,"Sonali"),(8,"Sachink"),(9,"Adarsh"),(10,"Sapna");
SELECT * from SALE;
SELECT * from ITEM;
SELECT * from CUSTOMER;
insert into sale values (1013,'2022-12-06',10,111,5);
SELECT price, qty_sold, (price*qty_sold) Total_Price FROM item, sale WHERE item.Item_id=sale.Item_id;
SELECT customer.cust_id, Customer.cust_name FROM Customer, Item, sale WHERE Item.Price>200 AND customer.cust_id=sale.cust_id AND Item.Item_id=sale.item_id;
SELECT cust_id, count(Item_id) FROM sale GROUP BY cust_id;
SELECT i.Item_Name FROM item i, sale s WHERE s.cust_id=5 AND i.item_id-s.item_id;
SELECT Item.item_id,Item.item_name FROM item, sale WHERE Item.item_id=sale.item_id AND sale.bill_date=curdate();

SELECT CHAR_LENGTH("SQL Lab");
SELECT CONCAT("SQL ","Lab ","is ","fun "); 
SELECT UCASE("sql lab"); 
SELECT LCASE("SQL LAB"); 
SELECT RTRIM("SQL Lab  "); 
SELECT LTRIM("  	SQL Lab"); 
SELECT REVERSE("SQL Lab"); 
SELECT SUBSTR("SQL Lab",3); 
SELECT STRCMP("SQL","sql");
SELECT REPLACE("SQL Lab in SQL Period","SQL","html");

SELECT ABS(-245.563);
SELECT CEIL(2.7);
SELECT FLOOR(2.3);
SELECT GREATEST(3,2,4,5,6);
SELECT LEAST(3,2,4,5,6);
SELECT LOG(2);
SELECT LOG10(2);
SELECT 12.1 DIV 3;
SELECT 18 MOD 4;
SELECT POW (2,3);
SELECT SQRT(9);
SELECT TRUNCATE(3.144444,3);

CREATE TABLE Persons (
    Personid int  NOT NULL AUTO_INCREMENT PRIMARY KEY,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int
);

INSERT INTO Persons (FirstName,LastName)
VALUES ('Lars','Monsen');
INSERT INTO Persons (FirstName,LastName)
VALUES ('Larry','Wheels'),('Nawaz','Sharif');

SELECT * FROM Persons;

SELECT * from department;



CREATE VIEW viewDeptIds AS
SELECT Dept_id 
FROM department
WHERE Dept_id = 1101;
SELECT * FROM viewDeptIds;
UPDATE viewDeptIds
SET Dept_id = 1101
WHERE Dept_id = 1103;
SELECT * FROM viewDeptIds;

CREATE VIEW Deptid_Empid AS
SELECT department.Dept_id, emp.id
FROM department,emp
WHERE department.D_name = emp.dept_name;
SELECT * FROM Deptid_Empid;
drop view viewDeptIds;


SELECT CURRENT_DATE();
SELECT sysdate();
SELECT DATE("2019-12-15 09:34:21");
SELECT MONTH("2022-12-15 09:34:21") AS MONTH;
SELECT YEAR("2022-10-15 09:34:21") AS YEAR;
SELECT QUARTER("2022-12-15 09:34:21") AS QUARTER;
SELECT WEEK("2022-12-15 09:34:21") AS WEEK;
SELECT EXTRACT( MONTH FROM "2022-10-15 09:34:21") AS DATE;
SELECT YEARWEEK("2022-12-15 09:34:21") AS YEAR_WEEK;
SELECT WEEKOFYEAR("2022-12-15 09:34:21") AS YEAR_WEEK;


SELECT DATEADD(day, 10, CAST(GETDATE() AS DATE)) As DateAdd;   
SELECT GETDATE() 'Now', DATEADD(ss,2,GETDATE()) 'Now + 2 seconds';
SELECT CURRENT_DATE();
SELECT DATEDIFF(day, '2023/01/01', '2023/01/11') AS NoOfDays;
SELECT GETDATE();
SELECT EXTRACT(WEEK FROM "2023-01-11");
SELECT sysdate();
SELECT EXTRACT( MONTH FROM "2022-10-15 09:34:21") AS DATE;
SELECT DAYOFYEAR("2023-01-11");  
SELECT CAST(eomonth(GETDATE()) AS date);



create database empdb;
use empdb;
create table emp(
	Employee_ID int,
    First_name varchar(20),
    Last_name varchar(20),
    Email varchar(30),
    Phone_number int,
    Hire_date date,
    Job_ID int,
    Salary int,
    Manager_ID int,
    Department_ID int);
    
insert into emp values(163,'vikas','tomar','kvikas@gm.com',987875,'2024-02-15',1,4500000,31,1001);
select * from emp;
delete from emp where Hire_date= '2024-03-15';
alter table emp ADD primary key(Employee_ID);

insert into emp values(164,'kunal','amar','amar@gm.com',487875,'2022-04-12',2,4500000,31,1001),
(165,'nal','ama','nal@gm.com',487875,'2022-04-12',2,4500000,31,1001),
(166,'ankit','mar','anki@gm.com',487875,'2022-04-12',2,6500000,31,1001),
(167,'virat','kohli','vk@gm.com',47875,'2022-05-12',2,6500000,32,1002),
(168,'sachin','singh','sachin@gm.com',478735,'2022-05-12',2,3500000,32,1002),
(169,'akhand','pandit','akpandit@gm.com',67875,'2022-05-12',2,4500000,33,1003);

select First_name,Last_name,Department_ID from emp where salary=(select min(Salary) from emp) group by Department_ID;
select First_name,Last_name from emp where salary > (select salary from emp where Employee_id=163);
select First_name,Last_name,Department_ID,Job_ID from emp where Job_ID=(select Job_ID from emp where Employee_ID=169);
insert into emp values(170,'payam','tomar','tom@gm.com',687875,'2024-03-15',3,6660000,31,1003);
select First_name,Last_name,Employee_ID,Salary from emp where First_name=(select First_name from emp where Manager_ID=31 && First_name='payam');





select * from emp;
create trigger empl
before insert 
on 
empdbfor each row
set new.id;

create database BCA; show databases;
select DATABASE();
use BCA;
show tables;
create table student
	(
	student int,
	fname varchar(20),
	lname varchar(20),
	marks int
	);
desc student;
show databases;



ALTER TABLE emp ADD age int CHECK (Age>=18);
create database hms;

desc emp;
select * from emp;
SELECT count(Salary),Employee_ID FROM emp GROUP BY Salary;
SELECT count(Salary),Employee_ID FROM emp GROUP BY Salary HAVING count(Salary)>1;
SELECT * FROM emp WHERE Salary BETWEEN 30000 AND 50000;
select * from student;
SELECT name FROM student WHERE roll_no = ANY(SELECT roll_no FROM course WHERE age=19);
SELECT name FROM student WHERE roll_no = ALL(SELECT roll_no FROM course WHERE age=19);

SELECT dept.deptno, emp.ename, emp.sal FROM dept INNER JOIN emp ON dept.deptno = emp.deptno;

SELECT dept.deptno, emp.ename, emp.sal FROM dept LEFT JOIN emp ON dept.deptno = emp.deptno;

SELECT dept.deptno, emp.ename, emp.sal FROM dept RIGHT JOIN emp ON dept.deptno = emp.deptno;

SELECT dept.deptno, emp.ename, emp.sal FROM dept LEFT JOIN emp ON dept.deptno = emp.deptno
UNION ALL
SELECT dept.deptno, emp.ename, emp.sal FROM dept RIGHT JOIN emp ON dept.deptno = emp.deptno;
