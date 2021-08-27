use big_data;	

-- 서브쿼리: 두 조건을 동시에 알 수 없을 때. (한 조건을 먼저 알아내고 그 다음에 조건을 알 수 있을 때)
-- 서브쿼리를 먼저 수행 후, 메인쿼리로 넘어감.
-- 여러개의 서브쿼리 사용가능.
-- 서브쿼리 안에서는 (select *) 를 쓰지 않음.
-- 단, where exists (select *)의 경우에는 가능하다.
-- AND와 비교하여, 자원절약 가능.
-- where = (서브쿼리) : equal('=')은 1개의 row결과(단일row)만 반환한다. -> in으로 대체
-- 메인 쿼리문의 select가 두 테이블 이상을 조회할 경우 join(and)를 사용해야한다.
-- 메인 쿼리문의 테이블을 서브쿼리에서 사용 가능. (but 반대는 불가)

select* 
from customer, product,orderproduct
group by or_customer;	

-- melon 고객이 주문한 제품의 제품번호, 수량, 단가 출력
select o.or_customer, p.pro_num, p.price, p.amount from product as p, orderproduct as o
where o.or_customer='melon' and p.pro_num=or_product;	

-- 직업이 학생인 고객이 구매한 제품코드, 이름, 구매일자
select o.or_product, c.cus_name, c.job, c.id, o.or_date
from customer as c, orderproduct as o
where c.job='학생' and o.or_customer=c.id;	

-- 고명석이 주문한 제품명
select id, cus_name, pro_name, pro_num from product as p, customer as c, orderproduct as o
where c.cus_name = '고명석' and c.id=o.or_customer and o.or_product=p	.pro_num;

-- 배송지가 서울인 고객의 이름, 제품명, 주문날짜 
select c.id, c.cus_name, p.pro_name, o.or_date , o.or_address	
from orderproduct as o, customer as c, product as p
where o.or_address like '서울%' and o.or_customer=c.id and o.or_product=p.pro_num;	

-- --------------------------------------------------------------
select c.id, c.age, o.or_product, o.or_date, o.or_customer 
from customer as c, orderproduct as o
where c.age>=30 and o.or_customer = c.id;	
-- ------------------------------------------------------------------
select c.id, c.age, o.or_product, o.or_date, o.or_customer 
from customer as c, orderproduct as o
where o.or_customer in (select id from customer where age>=30);		

select * from orderproduct	 	
where or_customer in (select id from customer where age>=30);	
-- ------------------------------------------------------------------
select pro_name, price, company from product
where company = 	
(select company from product where pro_name='달콤비스킷');

select cus_name, credit from customer
where credit = (select max(credit) from customer);

select pro_name, company from product	
where pro_num in (select or_product from orderproduct where or_customer='banana');	

select pro_name, company from product, orderproduct
where or_customer='banana' and pro_num=or_product;	

select cus_name from customer	
where exists (select * from orderproduct where or_date='2019-03-15' and or_customer = id);	

select cus_name, or_date from customer, orderproduct
where or_date = '2019-03-15' and or_customer = id;

select cus_name, id from customer
where id in	(select or_customer from orderproduct where or_date = '2019-03-15' and or_customer = id);

-- 주문량이 평균 이상인 고객의 이름과 id
select cus_name, id from customer
where id in 
(select or_customer from orderproduct 
where or_amount >= (select avg(or_amount) from orderproduct));

-- 나이가 30이상인 고객이 주문한 상품의 상품명, 단가, 금액
select c.cus_name, c.age, p.pro_name, p.price, o.or_amount, p.price*o.or_amount as total_price	
from customer as c, orderproduct as o, product as p
where c.age>=30 and c.id = o.or_customer and p.pro_num = o.or_product;
-- 상품명, 상품코드, 단가
select pro_name, pro_num, price from product
where pro_num in 
	(select or_product from orderproduct where or_customer in 
		(select id from customer where age>=30));