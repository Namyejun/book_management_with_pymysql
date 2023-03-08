from model.Book import Book
from model.Member import Member

def work_UI():
    return input(
"""
#########################
1. 도서 추가 입력
2. 대여 중 책 목록 출력
3. 반납 기한 지난 목록 출력
4. 도서 전체 조회
5. 도서 이름 및 저자로 조회
6. 도서 장르로 조회
0. 종료
#########################
입력> """)

def fun1(cur): # add_book
    print("##### 도서 추가 시작 #####")
    s = []
    for i in Book.field:
        s.append(input(i + ": "))
    try:
        cur.execute(f"insert into `books`(`ISBN`, `name`, `author`, `genre`, `price`) values ('{s[0]}', '{s[1]}', '{s[2]}', '{s[3]}', {int(s[4])});")
    except Exception as e:
        print("입력에 실패했습니다.")
        print("#########################")
        print(e)
        return False
    print("##### 도서 추가 완료 #####")
    return True

def fun2(cur): # select all borrow list
    print("##### 목록 조회 시작 #####")
    cur.execute(f"select * from `borrow` where `is_returned` = 0;")
    data = cur.fetchall()
    try:
        for i in data:
            print(*i[1:-1])
    except Exception as e:
        print("목록 조회에 실패했습니다.")
        print("#########################")
        print(e)
        return False
    print("##### 목록 조회 완료 #####")
    return True

def fun3(cur): # select return date over  
    print("##### 목록 조회 시작 #####")
    cur.execute(f"select * from `borrow` where `return_date` < current_timestamp() and `is_returned` = 0;")
    data = cur.fetchall()
    try:
        for i in data:
            print(*i[1:-1])
    except Exception as e:
        print("목록 조회에 실패했습니다.")
        print("#########################")
        print(e)
        return False
    print("##### 목록 조회 완료 #####")
    return True

def fun4(cur): # select all books
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

def fun5(cur): # select books by name or author
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

def fun6(cur): # select books by genre
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
def quit(a): #quit
    print("#########################")
    print("프로그램을 종료합니다.")
    print("#########################")
    exit()

work_menu = [quit, fun1, fun2, fun3, fun4, fun5, fun6]
