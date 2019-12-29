def part1():
    group = {'Ivanov' : [74,45,56], 'Petrov' : [67,75,56], 'Shov' : [77,63,34], 'Cuckov' : [93,80,76], 'Sidorov' : [34,45,30]}
    for i in group:
        count = 0
        s=0
        for k in group[i]:
            count+=1
            s+=k
        mean= float(s/count)
        print(f'{i:<10}{mean:>10.0f}')

def part2():
    group = {'Ivanov' : [5,4,5], 'Petrov' : [3,2,3], 'Shov' : [5,3,3], 'Cuckov' : [3,2,5], 'Sidorov' : [4,3,5]}
    score =[0,0,0]
    for i in group:
        count = 0
        s=0
        for k in group[i]:
            score[count]+=k
            count+=1
            s+=k
        mean= float(s/count)
        print(f'{i:<10}{mean:>10.1f}')
    print()
    for i in range(len(score)):
        score[i]/=len(group)
    k=str(score)
    k = k[1:-1:1]
    print(k.replace(',',' '))

def part3():
    def maxmin(arr, mini, maxi):
      #  a = min(mas, key= lambda x: x>mini )
      # b = max(mas, key= lambda x: x<maxi)
        lst = arr.split()
        l = []
        for i in lst:
            i = int(i.strip())
            if i >= mini and i <= maxi:
                l.append(i)
                minz = min(l)
                maxz = max(l)
        return minz, maxz

    arr = (input('Введите данные: '))
    mini = int(input('Введите минимальную границу поиска: '))
    maxi = int(input('Введите минимальную границу поиска: '))
    a,b= maxmin(arr, mini, maxi )
    print(f'Минимальное значение в заданных границах: {a}')
    print(f'Максимальное значение в заданных границах: {b}')
part3()
                

