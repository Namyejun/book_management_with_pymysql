# book_management_with_pymysql
## mysql을 사용해 도서를 관리하는 프로그램<br>

1. model -> 각 클래스를 모아놓은 디렉토리<br>
   1. Book.py -> 책의 정보를 담고있는 객체를 만들 클래스<br>
   2. Borrow.py -> 대여정보를 담고있는 객체를 만들 클래스<br>
2. mem_fun.py -> 고객이 실행할 수 있는 기능을 모아놓은 파일<br>
3. work_fun -> 직원이 실행할 수 있는 기능을 모아놓은 파일<br>
4. main.py -> 프로그램이 실제 돌아가는 장소<br>
5. conn_for_other -> DB와 세션을 만들어주는 파일 <br>
6. Management_program.exe -> 프로그램 실행파일
   1. 실행이 안될 시 /dist/main/main.exe 실행