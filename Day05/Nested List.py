if __name__ == '__main__':
    students = []
    # Collect input
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    # 1. Get all unique scores and sort them
    grades = sorted(list(set([x[1] for x in students])))
    
    # 2. Identify the second lowest grade
    second_lowest_grade = grades[1]
    
    # 3. Collect names of students with that grade
    result_names = [x[0] for x in students if x[1] == second_lowest_grade]
    
    # 4. Sort names alphabetically and print
    result_names.sort()
    for name in result_names:
        print(name)
