create database `book_management`;
use `book_management`;

create table `books` (
	`ISBN` varchar(20) not null,
    `name` varchar(50) not null,
    `author` varchar(20) not null,
    `genre` varchar(10) not null,
    `price` int not null,
    primary key(`ISBN`)
) ENGINE=InnoDB CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

create table `lib_member` (
	`id` int not null auto_increment,
    `name` varchar(20) not null,
    `phone_num` varchar(20) default null,
    `addr` varchar(50) default null,
    primary key(`id`)
) ENGINE=InnoDB CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

create table `borrow` (
	`id` int not null auto_increment,
	`ISBN` varchar(20) not null,
    `borrower_id` int not null,
    `borrow_date` datetime not null default current_timestamp,
    `return_date` datetime default (current_timestamp + interval 7 day),
    `is_returned` bool not null default false,
    primary key (`id`),
    foreign key (`ISBN`) references `books`(`ISBN`) on update cascade on delete cascade,
    foreign key (`borrower_id`) references `lib_member`(`id`) on update cascade on delete cascade
) ENGINE=InnoDB CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

insert into `book_management`.`books`(`ISBN`, `name`, `author`, `genre`, `price`)
values
("979-11-90014-69-4", "SQL로 맛보는 데이터 전처리 분석", "노수영", "교육", 24000),
("979-11-5839-152-2", "데이터 분석을 위한 파이썬 철저 입문", "최은석", "교육", 28000),
("979-11-5644-488-0", "누구나 파이썬 통계분석", "타니아이 히로키", "교육", 26000);

INSERT INTO `book_management`.`lib_member` (`id`, `name`, `phone_num`, `addr`) VALUES ('1', '남예준', '01042151148', '~');
INSERT INTO `book_management`.`lib_member` (`id`, `name`, `phone_num`, `addr`) VALUES ('2', '남예훈', '01042161148', '~');
