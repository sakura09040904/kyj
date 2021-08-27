-- 자동증가 옵션 
-- sequence 생성 필요. 각 테이블마다 생성. insert into 전에 해야함
-- create sequence seq_name;
-- insert into table(columns) value(seq_name.nextval, ......);

create table tblboard(
b_num int not null,
b_subject varchar(100) not null,
b_contants varchar(2000),
b_writer varchar(20),
b_date date,
constraint pk_b_num primary key(b_num)
);

create sequence seq_b_num;

insert into tblboard(b_num, b_subject, b_contants, b_writer, b_date) 
	values(seq_b_num.nextval, 'title1', 'contents1', 'writer1', '2021-07-30');
    insert into tblboard(b_num, b_subject, b_contants, b_writer, b_date) 
	values(seq_b_num.nextval, 'title2', 'contents2', 'writer2', '2021-07-30');
    insert into tblboard(b_num, b_subject, b_contants, b_writer, b_date) 
	values(seq_b_num.nextval, 'title3', 'contents3', 'writer3', '2021-07-30');
    insert into tblboard(b_num, b_subject, b_contants, b_writer, b_date) 
	values(seq_b_num.nextval, 'title4', 'contents4', 'writer4', '2021-07-30');
    
delete from tblboard where b_num >= 2;   

drop table tblboard;
drop sequence seq_b_num;

select * from tblboard;