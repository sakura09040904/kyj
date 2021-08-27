-- ���θ� Data Base
-- insert into table(columns) select columns(����) from table(����) (where ����)
-- �ٸ� table�κ��� value�� ������ �� ����.
-- group by�� ����� ��� �ߺ��Ǵ� �����ʹ� ��ȸ�� �� ���� (sum �� count�� ��ȸ)

select* from tblmember;
select* from tblgoods;
select* from tblaccount;
select* from tblsale;

create table tblmember(
m_id varchar(20) not null,
m_name varchar(20) not null,
constraint pk_m_id primary key(m_id)
);

create table tblgoods(
g_code int not null,
g_name varchar(100) not null,
g_price int not null,
constraint pk_g_code primary key (g_code)
);

create table tblaccount(
a_code int not null,
m_id varchar(20) not null,
a_date date,
constraint pk_a_code primary key (a_code),
constraint fk_m_id foreign key(m_id) references tblmember(m_id)
);

create table tblsale(
s_code int not null,
a_code int not null,
g_code int not null,
s_cnt int not null,
constraint pk_s_code primary key (s_code),
constraint fk_a_code foreign key(a_code) references tblaccount(a_code),
constraint fk_g_code foreign key(g_code) references tblgoods(g_code)
);

create sequence seq_g_code;
create sequence seq_a_code;
create sequence seq_s_code;

-- insert into tblmember(m_id, m_name) select c_id, c_name from customer
insert into tblmember(m_id, m_name) values('apple', '����ȭ');
insert into tblmember(m_id, m_name) values('banana', '�輱��');
insert into tblmember(m_id, m_name) values('carrot', '���');
insert into tblmember(m_id, m_name) values('orange', '����');
insert into tblmember(m_id, m_name) values('melon', '������');
insert into tblmember(m_id, m_name) values('peach', '������');
insert into tblmember(m_id, m_name) values('pear', 'ä����');

-- insert into tblgoods(g_code, g_name, g_price) values(seq_g_code.nextval) select 
insert into tblgoods(g_code, g_name, g_price) 
values(seq_g_code.nextval, '��Ż����BMT', 5000);
insert into tblgoods(g_code, g_name, g_price) 
values(seq_g_code.nextval, '�������Ŭ��', 6000);
insert into tblgoods(g_code, g_name, g_price) 
values(seq_g_code.nextval, '���׸���', 4800);
insert into tblgoods(g_code, g_name, g_price) 
values(seq_g_code.nextval, 'BLT', 5500);
insert into tblgoods(g_code, g_name, g_price) 
values(seq_g_code.nextval, 'K�ٺ�ť', 5800);
insert into tblgoods(g_code, g_name, g_price) 
values(seq_g_code.nextval, '��Ű', 5800);
insert into tblgoods(g_code, g_name, g_price) 
values(seq_g_code.nextval, '�����ͺ�', 5800);
insert into tblgoods(g_code, g_name, g_price) 
values(seq_g_code.nextval, select p_name from product, select p_price from product);

insert into tblaccount(a_code, m_id, a_date)
values(seq_a_code.nextval, 'apple', '2021-07-30');
insert into tblaccount(a_code, m_id, a_date)
values(seq_a_code.nextval, 'banana', '2021-07-23');
insert into tblaccount(a_code, m_id, a_date)
values(seq_a_code.nextval, 'carrot', '2021-06-30');
insert into tblaccount(a_code, m_id, a_date)
values(seq_a_code.nextval, 'orange', '2021-05-18');
insert into tblaccount(a_code, m_id, a_date)
values(seq_a_code.nextval, 'melon', '2021-08-13');
insert into tblaccount(a_code, m_id, a_date)
values(seq_a_code.nextval, 'peach', '2021-07-13');
insert into tblaccount(a_code, m_id, a_date)
values(seq_a_code.nextval, 'pear', '2021-06-11');
insert into tblaccount(a_code, m_id, a_date)
values(seq_a_code.nextval, 'apple', '2021-04-12');
insert into tblaccount(a_code, m_id, a_date)
values(seq_a_code.nextval, 'banana', '2021-03-19');
insert into tblaccount(a_code, m_id, a_date)
values(seq_a_code.nextval, 'carrot', '2021-08-01');
insert into tblaccount(a_code, m_id, a_date)
values(seq_a_code.nextval, 'apple', '2021-08-05');

insert into tblsale(s_code, a_code, g_code, s_cnt)
values(seq_s_code.nextval, 1,7,1);
insert into tblsale(s_code, a_code, g_code, s_cnt)
values(seq_s_code.nextval, 2,6,2);
insert into tblsale(s_code, a_code, g_code, s_cnt)
values(seq_s_code.nextval, 3,1,3);
insert into tblsale(s_code, a_code, g_code, s_cnt)
values(seq_s_code.nextval, 4,7,4);
insert into tblsale(s_code, a_code, g_code, s_cnt)
values(seq_s_code.nextval, 5,6,5);
insert into tblsale(s_code, a_code, g_code, s_cnt)
values(seq_s_code.nextval, 6,5,1);
insert into tblsale(s_code, a_code, g_code, s_cnt)
values(seq_s_code.nextval, 7,4,2);
insert into tblsale(s_code, a_code, g_code, s_cnt)
values(seq_s_code.nextval, 8,3,3);
insert into tblsale(s_code, a_code, g_code, s_cnt)
values(seq_s_code.nextval, 9,2,4);
insert into tblsale(s_code, a_code, g_code, s_cnt)
values(seq_s_code.nextval, 10,1,5);
insert into tblsale(s_code, a_code, g_code, s_cnt)
values(seq_s_code.nextval, 1,2,4);
insert into tblsale(s_code, a_code, g_code, s_cnt)
values(seq_s_code.nextval, 2,3,3);
insert into tblsale(s_code, a_code, g_code, s_cnt)
values(seq_s_code.nextval, 3,7,2);
insert into tblsale(s_code, a_code, g_code, s_cnt)
values(seq_s_code.nextval, 4,6,1);
insert into tblsale(s_code, a_code, g_code, s_cnt)
values(seq_s_code.nextval, 5,5,2);
insert into tblsale(s_code, a_code, g_code, s_cnt)
values(seq_s_code.nextval, 6,4,3);
insert into tblsale(s_code, a_code, g_code, s_cnt)
values(seq_s_code.nextval, 7,3,2);
insert into tblsale(s_code, a_code, g_code, s_cnt)
values(seq_s_code.nextval, 8,6,1);
insert into tblsale(s_code, a_code, g_code, s_cnt)
values(seq_s_code.nextval, 9,7,3);
insert into tblsale(s_code, a_code, g_code, s_cnt)
values(seq_s_code.nextval, 10,5,5);
insert into tblsale(s_code, a_code, g_code, s_cnt)
values(seq_s_code.nextval, 1,4,3);
insert into tblsale(s_code, a_code, g_code, s_cnt)
values(seq_s_code.nextval, 2,2,2);
insert into tblsale(s_code, a_code, g_code, s_cnt)
values(seq_s_code.nextval, 3,5,4);
insert into tblsale(s_code, a_code, g_code, s_cnt)
values(seq_s_code.nextval, 4,5,3);
insert into tblsale(s_code, a_code, g_code, s_cnt)
values(seq_s_code.nextval, 5,3,2);
insert into tblsale(s_code, a_code, g_code, s_cnt)
values(seq_s_code.nextval, 6,2,1);
insert into tblsale(s_code, a_code, g_code, s_cnt)
values(seq_s_code.nextval, 10,7,2);
insert into tblsale(s_code, a_code, g_code, s_cnt)
values(seq_s_code.nextval, 21,5,3);
insert into tblsale(s_code, a_code, g_code, s_cnt)
values(seq_s_code.nextval, 21,3,3);

-- ���� �������� �ֹ��� ����(�ֹ��ڵ�, �ֹ���ID, ��ǰ��, ����, �ݾ�, ��¥)
select a.a_code, a.m_id, g.g_name, s.s_cnt, g.g_price, s.s_cnt*g.g_price as total, a.a_date 
from tblsale s, tblaccount a, tblgoods g
where s.g_code=g.g_code and s.a_code=a.a_code and a.a_code
in(select max(a_code) from tblaccount);

-- ���� �������� �ֹ��� �ֹ��� ����
select m_id, m_name
from tblmember 
where m_id = (select m_id from tblaccount where a_code
=(select max(a_code) from tblaccount));

-- �������� �ֹ��� �ѱݾ�
select sum(s.s_cnt*g.g_price) total 
from tblsale s, tblgoods g
where s.g_code=g.g_code and a_code
in(select max(a_code) from tblaccount);

-- apple ���� �ֹ��� ��� �ֹ��ݾװ� ��¥
select a.a_code, sum(s.s_cnt*g.g_price), a.a_date from tblsale s, tblgoods g, tblaccount a
where s.g_code=g.g_code and a.a_code=s.a_code and s.a_code in 
(select a_code from tblaccount where m_id='apple')
group by a.a_code, a.a_date;

-- apple ���� �ֹ��� ��ǰ�� ������ ������(ǰ��, �ܰ�) ��ȸ
 select g_name,g_price from tblgoods where g_code in 
 (select g_code from tblsale where a_code in 
 (select a_code from tblaccount where m_id='apple'));

-- apple ���� �ѹ��� �ֹ����� �ʾҴ� ��ǰ ��ȸ
 select * from tblgoods where g_code not in 
 (select g_code from tblsale where a_code in 
 (select a_code from tblaccount where m_id = 'apple'));

commit;






