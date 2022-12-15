# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

X = int(input())
Y = int(input())
Z = int(input())
a = not(X or Y or Z) 
b = not(X and Y and Z)
print(a==b)


