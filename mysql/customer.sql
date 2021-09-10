-- use.schema(data base) : 해당 schema에 접근
-- create tabe table이름(column1:data1, column2:data2, ....)
-- data: 문자의 경우, ''안에 입력 
-- 코드 실행(쿼리문 단위): ctrl + i + enter, 전체코드 실행은 i 제외하고.

-- select column : 해당 column(속성)을 조회
-- select distinct column: 중복을 제외하고 조회
-- select column as newname : 해당 column(속성)을 newname으로 조회
-- from   : 테이블
-- where  : 조건
-- and : join 
-- group by 속성(리스트) having 조건  : (조건에 맞는)속성을 그룹지어 관리(ex. 부분합)
-- order by 속성(리스트) asc/desc    : 속성을 기준으로 오름차순/내림차순 정렬
-- order by 속성(날짜.시간관련) desc limit 20; : 최근 데이터 순으로 20개 출력

-- Table명 as 별명 : 별명으로 사용
-- 집계함수 : count(), min(), max(), sum(숫자만), avg(숫자만)
-- (null은 제외, where에서는 사용불가, select/having에서 사용)
-- group by 사용시, count()는 해당 그룹의 개수를 나타냄


use big_data;

CREATE TABLE CUSTOMER (
id VARCHAR(20) NOT NULL,
cus_name varchar(100) NOT NULL,
age int,
grade varchar(20) not null,
job varchar(20),
credit int default 0,
primary key(id)
);



create table product(
pro_num char(3) not null,
pro_name varchar(20),
amount int,
price int,
company varchar(20),
primary key(pro_num),
check(amount >=0 and amount <=10000) -- check(속성 및 제한조건): 입력값의 제한
);

create table orderproduct(
or_num char(3) not null,
or_customer varcharacter(20),
or_product char(3),
or_amount int,
or_address varchar(30),
or_date date,
primary key(or_num),
foreign key(or_customer) references customer(id), -- id를 참조하는 외래 키 발생
foreign key(or_product) references product(pro_num) -- pro_num를 참조하는 외래 키
);

INSERT INTO customer VALUES ('apple', '정소화', 20, 'gold', '학생', 1000);
INSERT INTO customer VALUES ('banana', '김선우', 25, 'vip', '간호사', 2500);
INSERT INTO customer VALUES ('carrot', '고명석', 28, 'gold', '교사', 4500);
INSERT INTO customer VALUES ('orange', '김용욱', 22, 'silver', '학생', 0);
INSERT INTO customer VALUES ('melon', '성원용', 35, 'gold', '회사원', 5000);
INSERT INTO customer VALUES ('peach', '오형준', NULL, 'silver', '의사', 300);
INSERT INTO customer VALUES ('pear', '채광주', 31, 'silver', '회사원', 500);

INSERT INTO product VALUES ('p01', '그냥만두', 5000, 4500, '대한식품');
INSERT INTO product VALUES ('p02', '매운쫄면', 2500, 5500, '민국푸드');
INSERT INTO product VALUES ('p03', '쿵떡파이', 3600, 2600, '한빛제과');
INSERT INTO product VALUES ('p04', '맛난초콜릿', 1250, 2500, '한빛제과');
INSERT INTO product VALUES ('p05', '얼큰라면', 2200, 1200, '대한식품');
INSERT INTO product VALUES ('p06', '통통우동', 1000, 1550, '민국푸드');
INSERT INTO product VALUES ('p07', '달콤비스킷', 1650, 1500, '한빛제과');

INSERT INTO orderproduct VALUES ('o01', 'apple', 'p03', 10, '서울시 마포구', '19/01/01');
INSERT INTO orderproduct VALUES ('o02', 'melon', 'p01', 5, '인천시 계양구', '19/01/10');
INSERT INTO orderproduct VALUES ('o03', 'banana', 'p06', 45, '경기도 부천시', '19/01/11');
INSERT INTO orderproduct VALUES ('o04', 'carrot', 'p02', 8, '부산시 금정구', '19/02/01');
INSERT INTO orderproduct VALUES ('o05', 'melon', 'p06', 36, '경기도 용인시', '19/02/20');
INSERT INTO orderproduct VALUES ('o06', 'banana', 'p01', 19, '충청북도 보은군', '19/03/02');
INSERT INTO orderproduct VALUES ('o07', 'apple', 'p03', 22, '서울시 영등포구', '19/03/15');
INSERT INTO orderproduct VALUES ('o08', 'pear', 'p02', 50, '강원도 춘천시', '19/04/10');
INSERT INTO orderproduct VALUES ('o09', 'banana', 'p04', 15, '전라남도 목포시', '19/04/11');
INSERT INTO orderproduct VALUES ('o10', 'carrot', 'p03', 20, '경기도 안양시', '19/05/22');



select id, cus_name, grade 
from customer;

select * from customer;

select id, cus_name, age, grade, job, credit
from customer;

select company from product;

select distinct company -- distinct: 중복을 제외한 모든 값을 조회
from product;

select pro_name, price as pro_price -- select 속성명 as new속성명 : new속성명으로 변경하여 조회
from product;

-- select pro_name, price+500 as 'correct_price' -- select 속성명+a as ''("") : a를 더하여 ''로 조회
select pro_name, price, price*0.7 as sale_price  -- 속성명을 ''("")로 쓸 경우 띄어쓰기 가능.
from product;                                   

select pro_name, amount, price, company from product
where company='한빛제과';   -- select 속성 / where 조건 : 조건이 성립하는 속성을 조회

select pro_name, price, company from product
where price>=2000 and price<=3000;

select or_product, or_amount, or_date, or_customer from orderproduct
where or_customer='apple' or or_amount>=15;

select or_product, or_amount, or_date, or_customer from orderproduct
where or_customer='apple' and or_amount>=15;

select cus_name, age, grade, credit from customer
where cus_name like '김%';  -- where 속성 like 'A%' : 해당 속성에 A가 들어있는 값을 조회 (문자열만 가능, 숫자는 불가)
-- A%: A로 시작, %A: A로 끝남, %A%: 중간에 A가 있음

select cus_name, grade, age from customer
order by age desc; -- order by 속성 내림차순(desc)/오름차순(asc) : 오름차순/내림차순으로 정렬

select or_customer, or_product, or_amount, or_date from orderproduct
where or_amount >=10 order by or_product asc, or_amount desc;

select avg(price) as average, sum(price) as total	 from product	-- avg(속성): 속성의 평균값, sum(속성): 속성의 합계
where company ='한빛제과';		

select count(id) as 'total customer', count(age) as 'total customer2', count(*) as 'total customer3' 
from customer;		-- select count(속성) as '' : 속성의 개수를 '새로운속성'으로 조회

select count(distinct company) as 'total company' from product;	

select or_product, sum(or_amount) as 'total amount' from orderproduct 
group by or_product; -- or_product를 기준으로 묶어서 sum(or_amoumt)을 출력alter

select company, count(*) as 'total product', max(price) as 'maximum' from product
group by company having count(*)>=3;
-- 3개 이상인 company를 기준으로 count와 price의 최대값을 조회

select grade, count(*) as 'number', avg(credit) as 'average of credit' from customer
group by grade having avg(credit)>=1000;	

select or_product, or_customer, sum(or_amount) as 'total amount' from orderproduct
group by or_product, or_customer order by or_product asc;

-- 적립금 평균이 1000이상인 등급을 대상으로 등급별 적립금 평균 및 고객 수를 출력
select grade, count(*), avg(credit) from customer
group by grade having avg(credit)>=1000;		 

select company, count(*) as 'num', sum(amount), max(amount) from product
group by company having max(amount) >=3000;	

select * from product as p, orderproduct as o
where o.or_customer='banana' and p.pro_num=o.or_product;

select p.pro_num, c.cus_name, c.id	
from customer as c, product as p, orderproduct as o
where c.cus_name = '고명석' and c.id = o.or_customer and p.pro_num = o.or_product;	

