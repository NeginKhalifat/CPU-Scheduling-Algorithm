from main import arr, context_switch, tq

gantt_chart = []
length = len(arr)
queue=[]
for i in range(length):
    if arr[i][1] == 0:
        arr[i][0] += arr[i][2]
        arr[i][2] = 0

io_time = []
io_chart = []
index = 0
now = 0
while True:
    if now>=io_time[0][2]:
        queue.append(int(io_time)-1)
    if index >=length:
        index=queue.pop(0)
        if arr[index][0] > tq:
            gantt_chart.append([str(index + 1), now, now + tq])
            queue.append(index)
            arr[index][0] -= tq
            now = gantt_chart[-1][2]
            index += 1
        else:
            gantt_chart.append([str(index + 1), now, now + arr[index][0]])
            arr[index][0] = 0
            now = gantt_chart[-1][2]
            io_chart.append([str(index + 1), now, now + arr[index][1]])
            io_time.append([str(index + 1), now, now + arr[index][1]])
            io_time.sort(key=lambda x: x[2])
            now = gantt_chart[-1][2]
            index += 1
    if arr[index][0] != 0:
        if arr[index][0] > tq:
            gantt_chart.append([str(index + 1), now, now + tq])
            queue.append(index)
            arr[index][0] -= tq
            now = gantt_chart[-1][2]
            index+=1
        else:
            gantt_chart.append([str(index + 1), now, now + arr[index][0]])
            arr[index][0] = 0
            now = gantt_chart[-1][2]
            io_chart.append([str(index + 1), now, now + arr[index][1]])
            io_time.append([str(index + 1), now, now + arr[index][1]])
            io_time.sort(key=lambda x: x[2])
            now=gantt_chart[-1][2]
            index+=1
  ##

