-- primary key/foreign key ������, constraint(��������)�ʿ�.
-- constraint pk_keyname primary key (keyname)
-- constraint fk_keyname foreign key(keyname) reference ����table(���� PK name)
-- commit; insert, update, delete ��� ���� �Ŀ� �ݵ�� �����ؾ� �����.

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

INSERT INTO customer VALUES ('apple', '����ȭ', 20, 'gold', '�л�', 1000);
INSERT INTO customer VALUES ('banana', '�輱��', 25, 'vip', '��ȣ��', 2500);
INSERT INTO customer VALUES ('carrot', '���', 28, 'gold', '����', 4500);
INSERT INTO customer VALUES ('orange', '����', 22, 'silver', '�л�', 0);
INSERT INTO customer VALUES ('melon', '������', 35, 'gold', 'ȸ���', 5000);
INSERT INTO customer VALUES ('peach', '������', NULL, 'silver', '�ǻ�', 300);
INSERT INTO customer VALUES ('pear', 'ä����', 31, 'silver', 'ȸ���', 500);

INSERT INTO product VALUES ('p01', '�׳ɸ���', 5000, 4500, '���ѽ�ǰ');
INSERT INTO product VALUES ('p02', '�ſ��̸�', 2500, 5500, '�α�Ǫ��');
INSERT INTO product VALUES ('p03', '��������', 3600, 2600, '�Ѻ�����');
INSERT INTO product VALUES ('p04', '�������ݸ�', 1250, 2500, '�Ѻ�����');
INSERT INTO product VALUES ('p05', '��ū���', 2200, 1200, '���ѽ�ǰ');
INSERT INTO product VALUES ('p06', '����쵿', 1000, 1550, '�α�Ǫ��');
INSERT INTO product VALUES ('p07', '���޺�Ŷ', 1650, 1500, '�Ѻ�����');

INSERT INTO tblorder VALUES ('o01', 'apple', 'p03', 10, '����� ������', '19/01/01');
INSERT INTO tblorder VALUES ('o02', 'melon', 'p01', 5, '��õ�� ��籸', '19/01/10');
INSERT INTO tblorder VALUES ('o03', 'banana', 'p06', 45, '��⵵ ��õ��', '19/01/11');
INSERT INTO tblorder VALUES ('o04', 'carrot', 'p02', 8, '�λ�� ������', '19/02/01');
INSERT INTO tblorder VALUES ('o05', 'melon', 'p06', 36, '��⵵ ���ν�', '19/02/20');
INSERT INTO tblorder VALUES ('o06', 'banana', 'p01', 19, '��û�ϵ� ������', '19/03/02');
INSERT INTO tblorder VALUES ('o07', 'apple', 'p03', 22, '����� ��������', '19/03/15');
INSERT INTO tblorder VALUES ('o08', 'pear', 'p02', 50, '������ ��õ��', '19/04/10');
INSERT INTO tblorder VALUES ('o09', 'banana', 'p04', 15, '���󳲵� ������', '19/04/11');
INSERT INTO tblorder VALUES ('o10', 'carrot', 'p03', 20, '��⵵ �Ⱦ��', '19/05/22');


select * from customer;
select * from product;
select * from tblorder;


-- id, ��ǰ��, �ܰ�, ����, �ݾ� ��ȸ
select c.c_id, p.p_name, p.p_price, o.o_amount, o.o_amount*p.p_price total 
from customer c, product p, tblorder o
where c.c_id=o.c_id and p.p_num=o.p_num
order by c.c_id asc;

-- ��ǰ���̺��� ��մܰ� �̻��� ��ǰ�� ������ ���� ���̵�, ����
select c_id, c_name from customer 
    where c_id in (select c_id from tblorder 
        where p_num in (select p_num from product 
            where p_price >= (select avg(p_price) from product)));





