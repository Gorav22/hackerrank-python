if __name__ == '__main__':
    N = int(input())
    lst = []
    for i in range(N):
        command = input()
        if "insert" in command:
            *rest, val1, val2 = command.split(" ")
            lst.insert(int(val1), int(val2))
        if "print" in command:
            print(lst)
        if "remove" in command:
            *rest, val = command.split(" ")
            lst.remove(int(val))
        if "append" in command:
            *rest, val = command.split(" ")
            lst.append(int(val))
        if "sort" in command:
            lst.sort()
        if "pop" in command:
            lst.pop()
        if "reverse" in command:
            lst.reverse()
