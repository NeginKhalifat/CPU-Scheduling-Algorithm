import matplotlib.pyplot as plt
from fcfs import gantt_chart

# line 1 points
i = 0
j = 1
length = len(gantt_chart)
while True:
    if (i >= length):
        break
    x1 = []
    y1 = []
    x1 = [gantt_chart[i][1], gantt_chart[i][2]]
    y1 = [j, j]
    j = j + 1
    # plotting the line 1 points
    if (gantt_chart[i][0] == "context" or gantt_chart[i][0] == "idle"):
        plt.plot(x1, y1, label=gantt_chart[i][0])

    else:
        plt.plot(x1, y1, label="P" + gantt_chart[i][0],linewidth=8.0)

    i = i + 1

# line 2 points


# naming the y axis
plt.ylabel('y - axis')
# giving a title to my graph
plt.title('Two lines on same graph!')

# show a legend on the plot
plt.legend()

# function to show the plot
plt.show()
