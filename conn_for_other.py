import pymysql
def con_db_for_other():
    try:
        conn = pymysql.connect(
            host = "127.0.0.1",
            port = 3306,
            user = "root",
            password = "1234",
            autocommit = True,
            database = "book_management",
            charset = "utf8mb4"
        )
    except:
        conn = pymysql.connect(
            host = "127.0.0.1",
            port = 3306,
            user = "root",
            password = "1234",
            autocommit = True,
            charset = "utf8mb4"
        )
        cur = conn.cursor()
        cur.execute("create database if not exists book_management;")
        cur.execute("use book_management")
        cur.execute("create table `books` (\
	                `ISBN` varchar(20) not null,\
                    `name` varchar(50) not null,\
                    `author` varchar(20) not null,\
                    `genre` varchar(10) not null,\
                    `price` int not null,\
                    primary key(`ISBN`)\
                    ) ENGINE=InnoDB CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;")
        
        cur.execute("create table `lib_member` (\
                    `id` int not null auto_increment,\
                    `name` varchar(20) not null,\
                    `phone_num` varchar(20) default null,\
                    `addr` varchar(50) default null,\
                    primary key(`id`)\
                    ) ENGINE=InnoDB CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;")
        
        cur.execute("create table `borrow` (\
                    `id` int not null auto_increment,\
                    `ISBN` varchar(20) not null,\
                    `borrower_id` int not null,\
                    `borrow_date` datetime not null default current_timestamp,\
                    `return_date` datetime default (current_timestamp + interval 7 day),\
                    `is_returned` bool not null default false,\
                    primary key (`id`),\
                    foreign key (`ISBN`) references `books`(`ISBN`) on update cascade on delete cascade,\
                    foreign key (`borrower_id`) references `lib_member`(`id`) on update cascade on delete cascade\
                    ) ENGINE=InnoDB CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;")
    return conn
