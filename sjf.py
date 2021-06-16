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
    if (index >= length):
        if (len(io_time) == 0):
            break
        else:
            list = []
            for j in range(len(io_time)):
                if now >= io_time[j][2] and find_cpu2(arr2, io_time[j][0])[3] != 0:
                    list.append(find_cpu2(arr2, io_time[j][0]))
            list.sort(key=lambda x: x[3])
            if len(gantt_chart) != 0 and gantt_chart[-1][0] != list[0][0] and context_switch != 0:
                gantt_chart.append(['context', now, now + context_switch])
                now = gantt_chart[-1][2]
            if list:
                # if
                if find_cpu2(arr2, list[0][0])[3] != 0:
                    gantt_chart.append([list[0][0], now, now + find_cpu2(arr2, list[0][0])[3]])  # todo
                    now = gantt_chart[-1][2]

                io_time.remove(get_io_time(io_time, list[0][0]))
                io_time.sort(key=lambda x: x[2])

            else:
                gantt_chart.append(['idle', now, io_time[0][2]])  # todo
                now = gantt_chart[-1][2]
                # gantt_chart.append([io_time[0][0], now, now + find_cpu2(arr2, io_time[0][0])[3]])  # todo

            # io_time.pop(0)

    else:

        if arr2[index][1] != 0:
            if (len(io_time) == 0):
                if len(gantt_chart) != 0 and gantt_chart[-1][0] != arr2[index][0] and context_switch != 0:
                    gantt_chart.append(['context', now, now + context_switch])
                    now = gantt_chart[-1][2]

                gantt_chart.append([arr2[index][0], now, now + arr2[index][1]])
                now = gantt_chart[-1][2]
                io_chart.append([arr2[index][0], now, now + arr2[index][2]])
                io_time.append([arr2[index][0], now, now + arr2[index][2]])
                if (find_cpu2(arr2, arr2[index][0])[3] == 0):
                    io_time.remove(get_io_time(io_time, arr2[index][0]))
                io_time.sort(key=lambda x: x[2])
                index += 1
            else:
                list = []
                for j in range(len(io_time)):
                    if now >= io_time[j][2] and find_cpu2(arr2, io_time[j][0])[3] != 0:
                        list.append(find_cpu2(arr2, io_time[j][0]))
                list.sort(key=lambda x: x[3])
                if (len(list) == 0 or list[0][3] > arr2[index][1]):

                    if len(gantt_chart) != 0 and gantt_chart[-1][0] != arr2[index][0] and context_switch != 0:
                        gantt_chart.append(['context', now, now + context_switch])
                        now = gantt_chart[-1][2]
                    gantt_chart.append([arr2[index][0], now, now + arr2[index][1]])
                    now = gantt_chart[-1][2]
                    io_chart.append([arr2[index][0], now, now + arr2[index][2]])
                    io_time.append([arr2[index][0], now, now + arr2[index][2]])
                    if (find_cpu2(arr2, arr2[index][0])[3] == 0):
                        io_time.remove(get_io_time(io_time, arr2[index][0]))
                    io_time.sort(key=lambda x: x[2])
                    index += 1
                else:

                    if len(gantt_chart) != 0 and gantt_chart[-1][0] != list[0][0] and context_switch != 0:
                        gantt_chart.append(['context', now, now + context_switch])
                        now = gantt_chart[-1][2]
                    gantt_chart.append([list[0][0], now, now + list[0][3]])
                    remove_item = get_io_time(io_time, list[0][0])

                    io_time.remove(remove_item)
                    io_time.sort(key=lambda x: x[2])
                    now = gantt_chart[-1][2]
        else:
            io_chart.append([arr2[index][0], now, now + arr2[index][2]])
            io_time.append([arr2[index][0], now, now + arr2[index][2]])
            if (find_cpu2(arr2, arr2[index][0])[3] == 0):
                io_time.remove(get_io_time(io_time, arr2[index][0]))
            io_time.sort(key=lambda x: x[2])
            index += 1

print(gantt_chart)
print(io_chart)
