create database `school`;
show databases;
drop database `school`;

set sql_safe_updates=0;

use `凤凰机器人老师资料`;
select * from  `teachers`;
alter table `teachers` add `部门` char(20);
update `teachers`
set `部门`="教师"
where name <>"玲玲" or name <> "月亮";

update `teachers`
set `部门`="销售"
where name ="玲玲" or name ="月亮";

update `teachers`
set `主管`= 4
where `部门`="销售";

create table bm(
	`部门` char(20),
    `number` int,
    primary key(`部门`)
);

drop table `bm`;

select * from `bm`;
insert into `bm` values ("销售",4);
insert into `bm` values ("教师",1);