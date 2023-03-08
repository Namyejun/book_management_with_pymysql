from model.Book import Book
from model.Member import Member

def mem_UI():
    return input(
"""
#########################
1. 회원 가입
2. 도서 전체 조회
3. 도서 이름 및 저자로 조회
4. 도서 장르로 조회
5. 도서 대여
6. 도서 반납
7. 회원 탈퇴
0. 종료
#########################
입력> """)

def fun1(cur): # add_member
    print("##### 회원 가입 시작 #####")
    s = []
    for i in Member.field[1:]:
        s.append(input(i + ": "))
    try:
        cur.execute(f"insert into `lib_member`(`name`, `phone_num`, `addr`) values ('{s[0]}', '{s[1]}', '{s[2]}');")
        cur.execute(f"select `id` from `lib_member` where `name` = '{s[0]}' and `phone_num` = '{s[1]}' and `addr` = '{s[2]}';")
        id = cur.fetchone()
        print(f"사용자의 아이디는 {id[0]}입니다.")
    except Exception as e:
        print("가입에 실패했습니다.")
        print("#########################")
        print(e)
        return False
    else:
        print("##### 회원 가입 완료 #####")
        return True

def fun2(cur): # select all books
    print("##### 도서 조회 시작 #####")
    cur.execute(f"select * from `books`;")
    data = cur.fetchall()
    try:
        for i in data:
            print(Book(*i))
    except Exception as e:
        print("도서 조회에 실패했습니다.")
        print("#########################")
        print(e)
        return False
    print("##### 도서 조회 완료 #####")
    return True

def fun3(cur): # select books by name or author
    s = input("찾으시는 책의 제목이나 작가 이름을 입력해주세요. : ")
    print("##### 도서 조회 시작 #####")
    cur.execute(f"select * from `books` where `name` like '%{s}%' or `author` like '%{s}%';")
    data = cur.fetchall()
    try:
        for i in data:
            print(Book(*i))
    except Exception as e:
        print("도서 조회에 실패했습니다.")
        print("#########################")
        print(e)
        return False
    else:
        print("##### 도서 조회 완료 #####")
        return True

def fun4(cur): # select books by genre
    print("##### 도서 조회 시작 #####")
    s = input("찾으시는 책의 장르를 입력해주세요. : ")
    cur.execute(f"select * from `books` where `genre` like '%{s}%';")
    data = cur.fetchall()
    try:
        for i in data:
            print(Book(*i))
    except Exception as e:
        print("도서 조회에 실패했습니다.")
        print("#########################")
        print(e)
        return False
    print("##### 도서 조회 완료 #####")
    return True

def fun5(cur): # borrow book
    print("##### 도서 대여 시작 #####")
    s = input("대여하시려는 책의 제목이나 작가 이름을 입력해주세요. : ")
    cur.execute(f"select `books`.`ISBN`, `books`.`name`, `books`.`author`, `books`.`genre`, `books`.`price`\
                from `books` natural left join `borrow`\
                where\
                (`books`.`name` like '%{s}%' or `books`.`author` like '%{s}%')\
                and\
                (`books`.`ISBN` not in (select `borrow`.`ISBN` from `borrow`) or (`borrow`.`is_returned` = 1));")
    data = cur.fetchall()
    print("##### 대여 가능 도서 #####")
    try:
        for i, book in enumerate(data):
            print("번호 :", i, "|" , Book(*book))
    except Exception as e:
        print("도서 조회에 실패했습니다.")
        print("#########################")
        print(e)
        return False
    else:
        print("#########################")
        try:
            id = int(input("본인의 id를 입력해주세요. "))
            num = int(input("대여 하시려는 번호를 입력해주세요. "))
            cur.execute(f"insert into `borrow`(`ISBN`, `borrower_id`)\
                        values\
                        ('{data[num][0]}', {id});")
        except Exception as e:
            print("대여에 실패했습니다.")
            print("#########################")
            print(e)
            return False
        else:
            print("##### 도서 대여 완료 #####")
            return True
        
def fun6(cur): # return book
    print("##### 도서 반납 시작 #####")
    id = int(input("본인의 id를 입력해주세요. "))
    cur.execute(f"select `borrow`.`borrower_id`, `borrow`.`ISBN`, `books`.`name`\
                from `borrow` natural join `books`\
                where `borrow`.`borrower_id` = {id} and `borrow`.`is_returned` = 0;")
    data = cur.fetchall()
    print("##### 현재 대여 도서 #####")
    try:
        for i, t in enumerate(data):
            print("번호 :", i, "|" , t[0], "\t", t[1], "\t", t[2])
    except Exception as e:
        print("도서 반납에 실패했습니다.")
        print("#########################")
        print(e)
        return False
    else:
        print("#########################")
        while True:
            try:
                num = int(input("반납 하시려는 번호를 입력해주세요. "))
                cur.execute(f"update `borrow`\
                            set `is_returned` = 1\
                            where `borrower_id` = {id} and `ISBN` = '{data[num][1]}';")
            except Exception as e:
                print("반납에 실패했습니다.")
                print("#########################")
                print(e)
                return False
            else:
                print("##### 도서 반납 완료 #####")
                choice = input("더 반납하시겠습니까? (y, n) : ")
                if choice == "y":
                    continue
                else:
                    return True

def fun7(cur): # remove member
    print("##### 회원 탈퇴 시작 #####")
    id = int(input("본인의 id를 입력해주세요. "))
    name = input("정말 삭제하시겠다면 본인의 이름을 입력하세요. ")
    try:
        cur.execute(f"delete from `lib_member` where `id` = {id} and `name` = '{name}';")
    except Exception as e:
        print("회원 탈퇴에 실패했습니다.")
        print("#########################")
        print(e)
        return False
    else:
        print("##### 회원 탈퇴 완료 #####")
        return True

def quit(a): #quit
    print("#########################")
    print("프로그램을 종료합니다.")
    print("#########################")
    exit()

mem_menu = [quit, fun1, fun2, fun3, fun4, fun5, fun6, fun7]