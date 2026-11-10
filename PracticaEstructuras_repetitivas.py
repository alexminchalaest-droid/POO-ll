for i in range(5):
    print(i)
for i in range(10):
    print(i)
for i in range(2,10,2):
    print(i)
for i in range(2,10,3):
    print(i)
for i in range(10,0,-1):
    print(i)
#Si el numero es par o impar del 1 al 100
for i in range(1,101):
    if i % 2 == 0:
        print(f"{i} es par")
    else:
        print(f"{i} es impar")

notas=[6,8,9,10,3]
for elemento in notas:
    print(elemento)