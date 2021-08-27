use big_data;		

-- insert into table(columns) values(new_data) : 새로운 data를 table에 입력.
-- columns 생략 가능 (순차적으로 입력됨)
-- not null data는 필수로 입력되어야 함.
-- insert into table(colums) select- from- where- : 필요한 data를 기존자료에서 조회하여, 해당 table의 column에 입력 

-- delete (column) from table where 조건 : 조건에 해당하는 부분을 삭제 (조건없이 일괄삭제 가능)
-- (column을 생략한 경우, 해당하는 row data 전체를 삭제함) 
-- update table set 수정내용 where 조건 : 조건에 해당하는 부분을 수정하여 table 내용을 update시킴.
-- where 없이 일괄 delete/set : Edit / Preferences / SQL Editor / safe update 체크 해제

-- view: 가상 table (실제 저장하지 않고 논치적으로만 존재)
-- view를 통해 다른 view 생성, 기본 table 검색 가능(but 내용수정은 제한적), order by 사용불가
-- create view view_name(view_columns) as select column from table where 조건 (with check option);
-- : 조건에 해당하는 column의 data들로 새로운 view 생성.
-- with check option : 조건에 만족하지 않는 새로운 data가 view에 들어오는 것을 방지

select * from customer where rownum = 1;	

insert into customer(id, cus_name, age, grade, job, credit)
values ('strawberry', '최유경', 30, 'vip', '공무원', 100);	

insert into customer(id, cus_name, age, grade, credit)	
values ('tomato', '정은심', 36, 'gold', 4000);	

select * from product where 'id' = 2;		
update product set pro_num='' where pro_num='p01';

create table 한빛제품(
han_name varchar(20),
han_amount int,
han_price int);	

insert into 한빛제품(han_name, han_amount, han_price)
select pro_name, amount, price from product
where company = '한빛제과';

select* from 한빛제품;

select* from product;			

update product
set pro_name = '통큰파이', price=3000	
where pro_num='p03';

update product
set price = price*1.1;

update orderproduct
set or_amount = 5
where or_customer in (select id from customer where cus_name='정소화');	

select* from orderproduct;					

delete from orderproduct
where or_date = '2019-05-22';

delete from orderproduct
where or_customer in (select id from customer where cus_name='정소화');

create view vip_customer(vip_name, vip_id, vip_credit, vip_age) 
as select cus_name, id, credit, age from customer where grade ='vip'
with check option; 

select * from vip_customer;	

select * from vip_customer where vip_age>=25;

update customer
set credit=credit*1.5 where grade='vip';

-- 3000원 이상인 제품을 구매한 고객의 아이디, 성명, 제품명	
select o.or_customer, c.cus_name, p.pro_name, p.price from customer as c, product as p, orderproduct as o
where c.id=o.or_customer and o.or_product=p.pro_num and p.price>=3000;	

-- 나이가 30이하인 고객이 주문한 제품의 제품명, 단가
select pro_name, price from product
where pro_num in (select or_product from orderproduct where or_customer in
(select id from customer where age<=30));


