# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

number = int(input('Enter number from 1 to 4 = '))
if (number == 1):
    print('x>0 and y>0')
elif (number == 2):
    print('x<0 and y>0')
elif (number == 3):
    print('x<0 and y<0')
else:
    print('x>0 and y<0')