def priority_scheduling(processes):

    processes.sort(key=lambda x: x[2])

    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n


    for i in range(1, n):
        waiting_time[i] = waiting_time[i-1] + processes[i-1][1]


    for i in range(n):
        turnaround_time[i] = waiting_time[i] + processes[i][1]


    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n


    print("Process\tBurst Time\tPriority\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"P{processes[i][0]}\t{processes[i][1]}\t\t{processes[i][2]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    print(f"\nAverage Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")

process_list = [
    (1, 10, 3),
    (2, 1, 1),
    (3, 2, 4),
    (4, 5, 2)
]
priority_scheduling(process_list)