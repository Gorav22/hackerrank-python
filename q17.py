def swap_case(s):
    return s.swapcase() if(0<len(s)<=1000) else None

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
