from main import arr, context_switch

gantt_chart = []
length = len(arr)
io_time = []
io_chart = []
index = 0
now = 0


def find_cpu(arr, p):
    for i in range(length):
        if (arr[i][0] == p):
            return arr[i]


while True:
    if (index >= length):
        if len(io_time) == 0: break
        if (now >= io_time[0][2]):
            if len(gantt_chart) != 0 and gantt_chart[-1][0] != io_time[0][0] and context_switch != 0:
                gantt_chart.append(['context', now, now + context_switch])
                now = gantt_chart[-1][2]
            gantt_chart.append([io_time[0][0], now, now + arr[int(io_time[0][0]) - 1][2]])
            now = gantt_chart[-1][2]
            io_time.pop(0)
        else:
            gantt_chart.append(['idle', now, io_time[0][2]])
            now = gantt_chart[-1][2]


    else:
        if arr[index][0] != 0:
            if (len(io_time) == 0):
                if len(gantt_chart) != 0 and gantt_chart[-1][0] != str(index + 1) and context_switch != 0:
                    gantt_chart.append(['context', now, now + context_switch])
                    now = gantt_chart[-1][2]

                gantt_chart.append([str(index + 1), now, now + arr[index][0]])
                if (arr[index][1] == 0):
                    gantt_chart.pop()
                    io_chart.append([str(index + 1), now, now + arr[index][1]])
                    if len(gantt_chart) != 0 and gantt_chart[-1][0] != str(index + 1) and context_switch != 0:
                        gantt_chart.append(['context', now, now + context_switch])
                        now = gantt_chart[-1][2]
                    gantt_chart.append([str(index + 1), now, now + arr[index][0] + arr[index][2]])
                    arr[index][2] = 0
                    now = gantt_chart[-1][2]
                else:
                    now = gantt_chart[-1][2]
                    io_chart.append([str(index + 1), now, now + arr[index][1]])
                    io_time.append([str(index + 1), now, now + arr[index][1]])
                    io_time.sort(key=lambda x: x[2])
                index = index + 1
            else:
                if (now > io_time[0][2]):
                    if len(gantt_chart) != 0 and gantt_chart[-1][0] != io_time[0][0] and context_switch != 0:
                        gantt_chart.append(['context', now, now + context_switch])
                        now = gantt_chart[-1][2]
                    gantt_chart.append([io_time[0][0], now, now + arr[int(io_time[0][0]) - 1][2]])
                    now = gantt_chart[-1][2]
                    io_time.pop(0)
                else:
                    if len(gantt_chart) != 0 and gantt_chart[-1][0] != str(index + 1) and context_switch != 0:
                        gantt_chart.append(['context', now, now + context_switch])
                        now = gantt_chart[-1][2]
                    gantt_chart.append([str(index + 1), now, now + arr[index][0]])
                    if (arr[index][1] == 0):
                        gantt_chart.pop()
                        if len(gantt_chart) != 0 and gantt_chart[-1][0] != str(index + 1) and context_switch != 0:
                            gantt_chart.append(['context', now, now + context_switch])
                            now = gantt_chart[-1][2]
                        gantt_chart.append([str(index + 1), now, now + arr[index][0] + arr[index][2]])
                        arr[index][2] = 0
                        now = gantt_chart[-1][2]
                    else:
                        now = gantt_chart[-1][2]
                        io_chart.append([str(index + 1), now, now + arr[index][1]])
                        io_time.append([str(index + 1), now, now + arr[index][1]])
                        io_time.sort(key=lambda x: x[2])
                    index = index + 1
        else:
            if arr[index][1] == 0:
                if len(gantt_chart) != 0 and gantt_chart[-1][0] != str(index + 1) and context_switch != 0:
                    gantt_chart.append(['context', now, now + context_switch])
                    now = gantt_chart[-1][2]
                gantt_chart.append([str(index + 1), now, now + arr[index][2]])
                now = gantt_chart[-1][2]
            else:
                io_chart.append([str(index + 1), 0, arr[index][1]])
                io_time.append([str(index + 1), 0, arr[index][1]])
                io_time.sort(key=lambda x: x[2])
            index += 1

print(gantt_chart)
print(io_chart)
