print('First come Fisrt serve')
arr_time = [0, 2, 4]
burst_time = [4, 3, 5]
wait_time = [0]*3
start_time = 0
finish_time = 0
turnaround_time = [0]*3


for index in range(3):
	print 'Process', index
	
	finish_time = finish_time + burst_time[index]
	wait_time[index] = start_time - arr_time[index]
	print'Waiting Time:', wait_time[index]

        turnaround_time[index] = finish_time-arr_time[index]
	print'Turnaround Time:', turnaround_time[index]
	start_time= start_time+burst_time[index]
