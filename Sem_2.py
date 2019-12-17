#Вриант 6
import string 
import random
def app1():
    a1 = int (input("hey "))
    s= a1
    s2 = 0+abs(a1**2)
    while s!=0:
        a1 = int(input())
        s = s + a1
        s2 = s2+abs(a1)**2
        if s==0:
            break
    print(s2)

def app2():
    A = [float(i) for i in input('Введите значения цен через пробел ').split()]
    for i in range(len(A)):
        print(f'{A[i]:>10}') 
    
def app3():
    s = input("Введите строку: ")
    m = int(input("m: "))
    n = int(input("n: "))
    if s[m:n] == '666':
        print("True")
    else:
        print("False")

def app4():
    A = [random.randint(12, 14) for i in range(20)]
    B = []
    print(A, "\n")
    i = 0
    while i < len(A):
	    if A[i] != 13:
		    B.append(A[i])
		    del A[i]
	    else:
		    i += 1
    print(B)

app2()

