if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    sor=sorted(set(arr))
    print(sor[-2])
