#case7. Единицы массы пронумернованы следующим
#образом: 1 - килограмм, 2 - миллиграмм, 3 - грамм,
#5 - центнер. Дан номер единицы массы (целое число
#в диапазоне 1 - 5) и масса тела в этих единицах
#(вещественное число). Найти массу тела в килограммах.

from m_case import *

def main():
    mera = [["кг", 1], ["мг", 0.000001], ["г", 0.001], ["ц", 100]]
    n = get_n("n")
    ed = input("ed: ")
    ans = None
    
    if ed in mera:
        for m in mera:
            if ed == m[0]:
                ans = n * m[1]

    print(m, "кг")

while True:
    try:
        main()
    except:
        print_error()

_case()
    
