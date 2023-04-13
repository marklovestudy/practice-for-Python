-- 创建显示删除数据库
create database `凤凰机器人老师资料`;
show databases;
drop database `凤凰机器人`;

-- 使用数据库 创建文件，使用文件，定义文件键，设置键的数据类型大小，自增，默认，删除表文件，查看表，在表文件中添加内容
set sql_safe_updates = 0;
use `凤凰机器人老师资料`;
create table teachers(
	`number` int not null auto_increment,
    `name` char(20),
    `born` int8,
    `professional` char(20) default '机器人',
    primary key(`number`)
);

-- 添加和删除键，删除键前可以加column
alter table `teachers` add `主管` int default 1;
alter table `teachers` drop column `主管`; 

drop table `teachers`;
show tables;
select * from `teachers`;
insert into `teachers`(`name`,`born`,`professional`) values("大飞",90,'比赛');
insert into `teachers`(`name`,`born`,`professional`) values("威威",96,'机械');
insert into `teachers`(`name`,`born`,`professional`) values("mark",83,'编程');
insert into `teachers`(`name`,`born`,`professional`) values("玲玲",82,'销售');
insert into `teachers`(`name`,`born`,`professional`) values("西瓜",98,'乐高');
insert into `teachers`(`name`,`born`,`professional`) values("小庄",96,'机器');
insert into `teachers`(`name`,`born`,`professional`) values("月亮",98,'销售');



