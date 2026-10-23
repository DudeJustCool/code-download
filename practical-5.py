def sjf_scheduling(processes, burst_times):
    n = len(processes)
    process_info = sorted(zip(processes, burst_times), key=lambda x: x[1])
    waiting_time = [0] * n
    turnaround_time = [0] * n
    

    for i in range(1, n):
        # Waiting time is sum of burst times of all previous processes
        waiting_time[i] = waiting_time[i-1] + process_info[i-1][1]


    for i in range(n):
        turnaround_time[i] = waiting_time[i] + process_info[i][1]


    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n


    print("Process\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"{process_info[i][0]}\t{process_info[i][1]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

    print(f"\nAverage Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")



processes = [1, 2, 3, 4]
burst_times = [6, 8, 7, 3]

sjf_scheduling(processes, burst_times)