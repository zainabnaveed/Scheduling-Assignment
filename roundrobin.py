print('Round Robin')

quantum=input('Enter quantum time:')
type(quantum)

processes=[0]*10
index=0
i=0
j=0
k=0
time=0

processes[0]=dictt={}
processes[1]=dictt={}
processes[2]=dictt={}

processes[0]['Process_id']='p1'
processes[1]['Process_id']='p2'
processes[2]['Process_id']='p3'

processes[0]['arr_time']=0
processes[1]['arr_time']=5
processes[2]['arr_time']=2

processes[0]['burst_time']=9
processes[1]['burst_time']=3
processes[2]['burst_time']=5

for i in range(3):
	for j in range(2-i):
		if processes[j]['arr_time']>processes[j+1]['arr_time']:
			temp={}
			temp=processes[j]
			processes[j]=processes[j+1]
			processes[j+1]=temp

check='true'

for i in range(3):
	processes[i]['rem_burst']=processes[i]['burst_time']

for j in range(3):
	check='true'
	if processes[j]['rem_burst']>0:
		check='false'
		if processes[j]['rem_burst']>quantum:
			time= time+ quantum
			processes[j]['rem_burst'] = processes[j]['rem_burst']-quantum
	else:
		time= time+ processes[j]['rem_burst']
		processes[j]['wait_time']= time-processes[j]['arr_time']-processes[j]['burst_time']
		processes[j]['rem_burst']=0

	if check=='true':
		break

for k in range(3):
	processes[k]['turnaround_time']=time-processes[k]['arr_time']

avgturntime=0
k=0

for k in range(3):
	print processes[k]
	avgturntime=avgturntime+processes[k]['turnaround_time']

avgturntime=avgturntime/3
print 'Average Turnaround Time'
print(avgturntime)
















