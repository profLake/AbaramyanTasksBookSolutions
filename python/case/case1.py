#case1. Дано целое число в диапазоне 1-7. Вывести
#строку - названия дня недели, соответствующее
#данному числу (1 - "понедельник", 2 - "вторник"
#и т.д.)

import m_case as m

DAYS_OF_WEEK = ["понедельник" ,"вторник" ,"среда" ,"четверг",
                "пятница" ,"суббота" ,"воскресенье"]
def main():
    n = int(input("n: "))
    print(DAYS_OF_WEEK[n - 1].title())

try:
    main()
except:
    print("\nНеизвестная ошибка.")
    
m._exit()


