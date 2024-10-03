import json
import math
import pickle as pkl

data_path=''

with open(data_path,'r') as f:
    SC_output = json.load(f)

# The following algorithm presents one iteration of Dynathink

cnt1=0
tot1=0
cnt_sc=0
tot2=0

# Hyperparameters

# start and end location of one iteration
start=0
end=10       

left_end=8 # extra queries of 'slow' questions

SC_end=10  # total number of queries of one question

total_score_min=0.0
total_score_max=0.0

for i in range(0,(int)(len(SC_output)),SC_end):
    list_min=[]
    list_max=[]
    for j in range(0,SC_end):
        
        if j%SC_end==0:
            list_min.append(SC_output[i+j])
    
        else:
            if len(list_min[0]['steps'])>len(SC_output[i+j]['steps']):
                list_min.clear()
                list_min.append(SC_output[i+j])
            elif len(list_min[0]['steps'])==len(SC_output[i+j]['steps']):
                list_min.append(SC_output[i+j])
        
        if j%SC_end==0:
            list_max.append(SC_output[i+j])
    
        else:
            if len(list_max[0]['steps'])<len(SC_output[i+j]['steps']):
                list_max.clear()
                list_max.append(SC_output[i+j])
            elif len(list_max[0]['steps'])==len(SC_output[i+j]['steps']):
                list_max.append(SC_output[i+j])

    score_min=0.0
    for t in range(0,len(list_min)):
        if list_min[t]['predicted_result']==list_min[t]['correct']:
            score_min+=1
    score_min=(float)(score_min/len(list_min))
    total_score_min+=score_min

    score_max=0.0
    for t in range(0,len(list_max)):
        if list_max[t]['predicted_result']==list_max[t]['correct']:
            score_max+=1
    score_max=(float)(score_max/len(list_max))
    total_score_max+=score_max

print('total score min:'+str(total_score_min/(len(SC_output)/10)))
print('total score max:'+str(total_score_max/(len(SC_output)/10)))      