set sql_safe_updates=0;
show databases;
use `凤凰机器人老师资料`;
select * from `teachers`;

-- 修改内容
update `teachers` 
set `born` = 96 
where born =90 and `name`='小庄';

update `teachers` 
set `主管` = 1 ;

-- 删除内容
delete from `teachers`
where number = 8;

-- 获取资料	排序
select * 
from `teachers` 
order by `born`,`number` 
limit 3;
-- 高到低排序
select * 
from `teachers` 
order by `born`,`number` desc;

-- 获取资料		<>不等于
select * 
from `teachers` 
where `number` <> 3;