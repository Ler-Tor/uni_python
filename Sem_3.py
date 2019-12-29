#Var 6 

def Zadanie_1():
    F = {'Russia': ['Europe', 12121212],
            'Germany': ['Europe', 12121212],
            'uwehi' : ['sasa', 21212] 
            }
    user_input = str(input())
    land = 0
    for k, val in F.items():
        if(val[0] == user_input):
            print(k)
            land = land + val[1]
    print(land)    

def Zadanie_2():
    A = {
        '1a': 20,
        '1b': 23,
        '2a': 25,
        '2b': 32
    }
    print("   Что вы хотите сделать? \n 1.Изменение учеников в классе \n 2.Определить колическтво учащихся\n")
    a = int(input())
    if(a == 1):
        print("Введите класс: \n")
        klass = str(input())
        print("Введите колличество учеников \n")
        amount = int(input())

        A[klass] = amount
        print(A)
    elif(a == 2):
        kids = 0
        print(A)
        for val in A:
            kids = kids + A[val]
        print(kids)

    else:
         print("Error")



def Zadanie_3():
    A = {}
    print("Введите данные(для окончания ввода в строке введите ‘end’):")
    while True:
        s = input()
        if(s == 'end'):
            break
        a, b = s.split()
        if(b != 'None'):
            A[a] = b   
    print(A)  
    def summ(A):
        n = 0
        amount = 0
        for val in A:
            n = n + 1
            amount = amount + int(A[val])
        sred = amount/n
        return(sred)
    print(summ(A))

Zadanie_1()


