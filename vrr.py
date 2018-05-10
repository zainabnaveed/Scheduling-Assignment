print 'Virtual Round Robin'

quantum=input('Enter quantum time:')
type(quantum)

processes=[0]*10
index=0
i=0
j=0
k=0
time=0
wait_queue=[0]*10
aux_queue=[0]*10
io_rettime=5
io_switch=2
rem_quantum=0

for index in range(10):
	processes[index]=dictt={}
	wait_queue[index]=dictt1={}
	aux_queue[index]=dictt1={}

processes[0]['Process_id']='p1'
processes[1]['Process_id']='p2'
processes[2]['Process_id']='p3'

processes[0]['arr_time']=0
processes[1]['arr_time']=5
processes[2]['arr_time']=2

processes[0]['burst_time']=9
processes[1]['burst_time']=13
processes[2]['burst_time']=5

#even process=1 and odd process=0
#even process goes for i/o
processes[0]['p_io']=0
processes[1]['p_io']=1
processes[2]['p_io']=0

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

l=0
m=0
n=0
rem_quantum=quantum

for j in range(3):
	if processes[j]['p_io']==1:
		if time>=wait_queue[m]['ret_time']:
			aux_queue[j]=wait_queue[m]		
			m=m+1
		if processes[j]['rem_burst']>0:
		check='false'
			if processes[j]['rem_burst']>io_switch:
				time=time+io_switch
				wait_queue[l]=time+io_rettime
	    			processes[j]['rem_burst'] = processes[j]['rem_burst']-io_switch
				rem_quantum=rem_quantum-io_switch
				processes[j]['rem_burst'] = processes[j]['rem_burst']-rem_quantum
				l=l+1
			else:
				time=time+processes[j]['rem_burst']
				processes[j]['wait_time']= time-processes[j]['arr_time']-processes[j]['burst_time']
				processes[j]['rem_burst']=0
				wait_queue[m]['ret_time']=0
				m=m+1
	else:
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

k=0
avgturntime=0

for k in range(3):
	print processes[k]
	avgturntime=avgturntime+processes[k]['turnaround_time']

avgturntime=avgturntime/3
print 'Average Turnaround Time'
print(avgturntime)







