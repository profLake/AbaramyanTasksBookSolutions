#if21. Даны целочисленные координаты точки на плоскости.
#Если точка совпадает с началом координат, то вывести 0.
#Если точка не совпадает с началом координат, но лежит на
#оси OX или OY, то вывести соответственно 1 или 2. Если
#точка не лежит на координатных осях, то вывести 3.

import m_if

coor = m_if.get_coor()

if coor == [0, 0]:
    print(0)
elif coor[1] == 0 :
    print(1)
elif coor[0] == 0:
    print(2)
else:
    print(3)

input("Для продолжения нажмите enter.")