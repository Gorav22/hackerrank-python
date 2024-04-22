if __name__ == '__main__':
    students_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students_list.append([name, score])
    
    student_dict = dict(students_list)
    values = student_dict.values()
    min_val = min(values) # finding minimum value
    second_dict = {k: v for k, v in student_dict.items() if v != min_val}    
    lst = sorted([k for k,v in second_dict.items() if v == min(second_dict.values())]) 
    
    for i in lst:
        print(i)
