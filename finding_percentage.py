if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for keys in student_marks.keys():
            if(keys==query_name):
                x=student_marks[query_name]
    sum=0
    count=0
    for i in x:
        sum=sum+i
        count=count+1
    avr="{:.2f}".format(sum/count) 
    print(avr)              