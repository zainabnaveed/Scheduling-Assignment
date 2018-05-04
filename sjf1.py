print('Shortest Job first')
process=['p1', 'p2', 'p3']
arr_time = [0, 1, 3]
burst_time = [4, 5, 3]
wait_time = [0]*3
start_time = 0
finish_time = 0
turnaround_time = [0]*3
minn=0
i=0
j=0
avg=0.0

for i in range(3):
	for j in range(2-i):
		if arr_time[j]>minn and burst_time[j]>burst_time[j+1]:
			temp=burst_time[j]
			burst_time[j]=burst_time[j+1]
			burst_time[j+1]=temp
			tem=arr_time[j]
			arr_time[j]=arr_time[j+1]
			arr_time[j+1]=tem
			t=process[j]
			process[j]=process[j+1]
			process[j+1]=t
	minn=burst_time[i]+minn

for index in range(3):
	print(process[index])
	
	finish_time = finish_time + burst_time[index]
	wait_time[index] = start_time - arr_time[index]
	print'Waiting Time:', wait_time[index]

        turnaround_time[index] = finish_time-arr_time[index]
	print'Turnaround Time:', turnaround_time[index]
	start_time= start_time+burst_time[index]

print 'Average Turnaround Time'
for k in range(3):
	avg=avg+turnaround_time[k]

avg=avg/3
print(avg)















