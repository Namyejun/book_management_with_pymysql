from conn import con_db
from conn_for_other import con_db_for_other
import work_fun
import mem_fun

def UI():
    return input(
"""#########################
1. 고객용 프로그램
2. 직원용 프로그램
#########################
입력> """)
print()
with con_db() as conn:
    with conn.cursor() as cur:
        while True:
            c = UI()
            if c == '1':
                while True:
                    try:
                        choice = int(mem_fun.mem_UI())
                        mem_fun.mem_menu[choice](cur)
                    except Exception as e:
                        print("다시 선택하세요.")
                        continue
                    else:
                        if choice == 8: break
                        conn.commit()

            elif c == '2':
                while True:
                    try:
                        choice = int(work_fun.work_UI())
                        work_fun.work_menu[choice](cur)
                    except Exception as e:
                        print("다시 선택하세요.")
                        continue
                    else:
                        if choice == 7: break
                        conn.commit()

