cube = lambda x: x**3

def fibonacci(n):
    l1=[]
    for i in range(n):
        if(i==0):
            l1.append(0)
        elif(i==1):
            l1.append(1)
        else:
            l1.append(l1[i-1]+l1[i-2])
        
    return l1

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
