from main import arr, context_switch, tq

gantt_chart = []
length = len(arr)
queue = []
arr2 = []
for i in range(length):
    arr2.append([str(i + 1), arr[i][0], arr[i][1], arr[i][2]])

for i in range(length):
    if arr2[i][2] == 0:
        arr2[i][0] += arr2[i][3]
        arr2[i][3] = 0
arr2.sort(key=lambda x: x[1])
print(arr2)
io_time = []
io_chart = []
index = 0
now = 0


def find_cpu2(arr, p):
    for i in range(length):
        if (arr[i][0] == p):
            return arr[i]


def get_io_time(io_time, p):
    for i in range(len(io_time)):
        if io_time[i][0] == p:
            return io_time[i]


while True:
    if arr2[index][1] == 0:
        io_time.append([arr2[index][0], 0, arr2[index][2]])
        io_chart.append([arr2[index][0], 0, arr2[index][2]])
        io_time.sort(key=lambda x: x[2])
        index += 1
    else:
        if len(io_time) == 0:

            if len(gantt_chart) != 0 and gantt_chart[-1][0] != arr2[index][0] and context_switch != 0:
                gantt_chart.append(['context', now, now + context_switch])
                now = gantt_chart[-1][2]
            gantt_chart.append([arr2[index][0], now, now + arr2[index][1]])
            now = gantt_chart[-1][2]
            io_chart.append([arr2[index][0], now, now + arr2[index][2]])
            io_time.append([arr2[index][0], now, now + arr2[index][2]])
            io_time.sort(key=lambda x: x[2])
            index += 1
        else:
            list = []
            for i in range(len(io_time)):
                if io_time[i][2] == io_time[0][2]:
                    list.append(find_cpu2(arr2, io_time[i][0]))

            list.sort(key=lambda x: x[3])
            if (now < io_time[0][2]):

                if len(gantt_chart) != 0 and gantt_chart[-1][0] != arr2[index][0] and context_switch != 0:
                    gantt_chart.append(['context', now, now + context_switch])
                    now = gantt_chart[-1][2]
                if (now + arr2[index][1]) <= io_time[0][2]:
                    gantt_chart.append([arr2[index][0], now, now + arr2[index][1]])
                    now = gantt_chart[-1][2]
                    io_chart.append([arr2[index][0], now, now + arr2[index][2]])
                    io_time.append([arr2[index][0], now, now + arr2[index][2]])
                    io_time.sort(key=lambda x: x[2])
                if now + arr2[index][1] > io_time[0][2]:

                    gantt_chart.append([list[0][0], now, io_time[0][2]])
                    arr2[index][1] -= io_time[0][2] - now
                    #io_time.remove(get_io_time(io_time, list[0][0]))
                    now = gantt_chart[-1][2]
