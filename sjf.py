#SJF with arrival time 0
print('Shortest Job first')
arr_time = [0, 0, 0]
burst_time = [4, 3, 5]
wait_time = [0]*3
start_time = 0
finish_time = 0
turnaround_time = [0]*3
minn=burst_time[0]
i=0
j=0

for i in range(3):
	for j in range(2-i):
		if burst_time[j]>burst_time[j+1]:
			temp=burst_time[j]
			burst_time[j]=burst_time[j+1]
			burst_time[j+1]=temp

for index in range(3):
	
	finish_time = finish_time + burst_time[index]
	wait_time[index] = start_time - arr_time[index]
	print'Waiting Time:', wait_time[index]

        turnaround_time[index] = finish_time-arr_time[index]
	print'Turnaround Time:', turnaround_time[index]
	start_time= start_time+burst_time[index]















