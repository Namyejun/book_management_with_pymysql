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
with con_db_for_other() as conn:
    with conn.cursor() as cur:
        while True:
            c = UI()
            if c == '1':
                while True:
                    try:
                        choice = int(mem_fun.mem_UI())
                        if choice < 0 or choice > 8:
                            raise Exception
                    except Exception as e:
                        print("다시 선택하세요.")
                        continue
                    else:
                        mem_fun.mem_menu[choice](cur)
                        if choice == 8: break
                        conn.commit()

            elif c == '2':
                while True:
                    try:
                        choice = int(work_fun.work_UI())
                        if choice < 0 or choice > 7:
                            raise Exception
                    except Exception as e:
                        print("다시 선택하세요.")
                        continue
                    else:
                        work_fun.work_menu[choice](cur)
                        if choice == 7: break
                        conn.commit()

