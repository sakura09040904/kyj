use big_data;	

-- 자동 증가 옵션 : table 생성시, auto_increment 추가 (PK설정 필수) 
-- value를 입력하지 않을경우, 1부터 순차적 입력
-- 기존 data를 삭제 후 입력하여도, 삭제된 숫자 이후부터 증가 됨. (reset은 table drop필요) 

create table tblboard(
b_num int not null auto_increment,
b_subject varchar(100) not null,
b_contants varchar(2000),
b_writer varchar(20),
b_date date,
primary key(b_num)  
);

insert into tblboard(b_subject, b_contants, b_writer, b_date) 
	values('title2', 'contents2', 'writer2', '2021-07-30');
    insert into tblboard(b_subject, b_contants, b_writer, b_date) 
	values('title3', 'contents3', 'writer3', '2021-07-30');
    insert into tblboard(b_subject, b_contants, b_writer, b_date) 
	values('title4', 'contents4', 'writer4', '2021-07-30');
    
select* from tblboard;    