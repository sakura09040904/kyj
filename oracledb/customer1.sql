-- primary key/foreign key 설정시, constraint(제약조건)필요.
-- constraint pk_keyname primary key (keyname)
-- constraint fk_keyname foreign key(keyname) reference 참조table(참조 PK name)
-- commit; insert, update, delete 명령 실행 후에 반드시 실행해야 저장됨.

CREATE TABLE customer(
c_id VARCHAR(20)	NOT NULL,
c_name VARCHAR(10) NOT NULL,
c_age int,
c_grade varchar(10) not null,
c_job varchar(20),
c_credit int default 0,
constraint pk_c_id primary key (c_id)
);

create table product(
p_num char(3) not null,
p_name varchar(20),
p_stock int,
p_price int,
p_company varchar(20),
constraint pk_p_num primary key(p_num)
);

create table tblorder(
o_num char(3) not null,
c_id varchar(20) not null,
p_num char(3) not null,
o_amount int,
o_address varchar(30),
o_date date,
constraint pk_o_num primary key(o_num),
constraint fk_c_id foreign key(c_id) references customer(c_id),
constraint fk_p_num foreign key(p_num) references product(p_num)
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

INSERT INTO tblorder VALUES ('o01', 'apple', 'p03', 10, '서울시 마포구', '19/01/01');
INSERT INTO tblorder VALUES ('o02', 'melon', 'p01', 5, '인천시 계양구', '19/01/10');
INSERT INTO tblorder VALUES ('o03', 'banana', 'p06', 45, '경기도 부천시', '19/01/11');
INSERT INTO tblorder VALUES ('o04', 'carrot', 'p02', 8, '부산시 금정구', '19/02/01');
INSERT INTO tblorder VALUES ('o05', 'melon', 'p06', 36, '경기도 용인시', '19/02/20');
INSERT INTO tblorder VALUES ('o06', 'banana', 'p01', 19, '충청북도 보은군', '19/03/02');
INSERT INTO tblorder VALUES ('o07', 'apple', 'p03', 22, '서울시 영등포구', '19/03/15');
INSERT INTO tblorder VALUES ('o08', 'pear', 'p02', 50, '강원도 춘천시', '19/04/10');
INSERT INTO tblorder VALUES ('o09', 'banana', 'p04', 15, '전라남도 목포시', '19/04/11');
INSERT INTO tblorder VALUES ('o10', 'carrot', 'p03', 20, '경기도 안양시', '19/05/22');


select * from customer;
select * from product;
select * from tblorder;


-- id, 제품명, 단가, 수량, 금액 조회
select c.c_id, p.p_name, p.p_price, o.o_amount, o.o_amount*p.p_price total 
from customer c, product p, tblorder o
where c.c_id=o.c_id and p.p_num=o.p_num
order by c.c_id asc;

-- 제품테이블의 평균단가 이상인 제품을 구매한 고객의 아이디, 고객명
select c_id, c_name from customer 
    where c_id in (select c_id from tblorder 
        where p_num in (select p_num from product 
            where p_price >= (select avg(p_price) from product)));





