if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    list1 = list(student_marks[query_name])
    addition = sum(list1)
    result = addition/len(list1)
    print(format(result, '.2f'))
