-- 显示全部数据库
show databases;

-- 创建数据库
create database `凤凰机器人珠海一校`;

-- 删除数据库
drop database `凤凰机器人珠海一校`;

-- 使用数据库
use `凤凰机器人珠海一校`;

-- 显示数据库下的所有表格
show tables;

-- 创建表格
create table `teachers`(
	`id` int auto_increment,
    `name` char(20),
    `birth_date` char(20),
    `sex` char(10),
    `salary` int,
    `branch_id` int,
    `sup_id` int,
    primary key(`id`)
);

-- 删除表格
drop table `teachers`;

-- 显示表格所有键
select * from `teachers`;

-- 添加键
alter table `teachers` add `asas` char(20);

-- 删除键
alter table `teachers` drop `asas`;

-- 给表格添加内容
insert into `teachers`(`name`,`birth_date`,`sex`,`salary`,`branch_id`,`sup_id`) values("大白","1995-7-6","male",9000,2,2);

-- 修改表内容之前把安全设置关闭
set sql_safe_updates=0;

-- 修改表格内容
update `teachers`
set name="so"
where `name`="sook";

-- 删除表格内容
delete from `teachers`
where `id`=9;

-- 实例1：把branch里的管理改成id是1
select * from `branch`;
update `branch`
set `manager_id` = 1
where `branch_name` = "董事会";

-- 创建新表客户Client
create table `client`(
	`client_id` int auto_increment,
    `client_name` char(20) ,
    `phone` long,
    primary key (`client_id`)
);

drop table `client`;

-- 显示`Client`表
select * from `client`;

--  添加客户名单
insert into `client`(`client_name`,`phone`) values ("孔炜彤",13543007162);
insert into `client`(`client_name`,`phone`) values ("梁梓熠",13543036153);
insert into `client`(`client_name`,`phone`) values ("王瀚正",13709696982);
insert into `client`(`client_name`,`phone`) values ("廖其烨",15113651105);
insert into `client`(`client_name`,`phone`) values ("樊耀铭",13425034286);
insert into `client`(`client_name`,`phone`) values ("易诗涵",13417791103);
insert into `client`(`client_name`,`phone`) values ("戴一诺",13823096560);
insert into `client`(`client_name`,`phone`) values ("陈泽涛",18666977996);

-- 创建员不同客户关系表
create table `works_with`(
	`emp_id` int,
    `client_id` int,
    `total_sales` int,
    primary key(`emp_id`,`client_id`)
);

select * from `works_with`;