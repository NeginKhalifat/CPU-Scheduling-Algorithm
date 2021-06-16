import csv

arr = []
i = 0
context_switch=int(input('please enter context switch time:\n'))
tq=int(input("please enter time quantum:"))
with open('test.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = -1
    for row in csv_reader:
        if line_count == -1:
            line_count += 1
        else:
            arr.append( [int(row[1]),int( row[2]),int( row[3])])
            line_count += 1


    print(len(arr))
