if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    zero= str().zfill(1)
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for i in student_marks:
        if i==f"{query_name}":
            string =""
            percentage= str(sum(student_marks[i])/3)+zero
            for j in range(len(percentage)):
                if j <= 4:
                    string+=percentage[j]
                else:
                    break
            print(string)