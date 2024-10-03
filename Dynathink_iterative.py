import json
import math
import pickle as pkl

data_path=''

with open(data_path,'r') as f:
    SC_output = json.load(f)

generate_times_from_ori_data=10 # all the data for both slow set and fast set, we put them together
end_for_fast=5 # the generate times for seperation of fast set and slow set
regenerate=10 # dealing the slow set data(including previous cost in seperation part)

left_correct=0
cost=0
new_t=0
new=0
wrong=[]

for i in range(0,(int)(len(SC_output)/generate_times_from_ori_data)):
    wrong.append(i)


for end in range(2,end_for_fast):
    wrong1=[]
    new1=0
    for i in wrong:
        
        step_cal={}
        
        for j in range(0,end):
            if SC_output[i*generate_times_from_ori_data+j]['predicted_result']!=None:
                if SC_output[i*generate_times_from_ori_data+j]['predicted_result'] not in step_cal:
                    step_cal[SC_output[i*generate_times_from_ori_data+j]['predicted_result']]=len(SC_output[i*generate_times_from_ori_data+j]['steps'])
                else:
                    if step_cal[SC_output[i*generate_times_from_ori_data+j]['predicted_result']]>len(SC_output[i*generate_times_from_ori_data+j]['steps']):
                        step_cal[SC_output[i*generate_times_from_ori_data+j]['predicted_result']]=len(SC_output[i*generate_times_from_ori_data+j]['steps'])

        res = {}
        for j in range(0,end):
            if SC_output[i*generate_times_from_ori_data+j]['predicted_result']!=None:
                if SC_output[i*generate_times_from_ori_data+j]['predicted_result'] not in res:
                    res[SC_output[i*generate_times_from_ori_data+j]['predicted_result']]=1
                else:
                    res[SC_output[i*generate_times_from_ori_data+j]['predicted_result']]+=1
        it = iter(res) 
        max=0
        ans=''
        for x in it:
            if res[x]>max:
                max=res[x]
                ans=x
        min=100.0
        for x in step_cal:
            if min>=step_cal[x]:
                min=step_cal[x]
        if ans!='' and res[ans]>=int(end/2)+1:
            if step_cal[ans]<=min:
                new+=1
                new1=1
                if ans==SC_output[i*generate_times_from_ori_data]['correct']:
                    new_t+=1
        else:
            wrong1.append(i)
    cost+=new1*end
    if new==0:
        break
    wrong.clear()
    wrong=wrong1.copy()

for i in wrong:

    step_cal={}
    res = {}
    for j in range(0,regenerate):
        if SC_output[i*generate_times_from_ori_data+j]['predicted_result']!=None:
            if SC_output[i*generate_times_from_ori_data+j]['predicted_result'] not in res:
                res[SC_output[i*generate_times_from_ori_data+j]['predicted_result']]=1
            else:
                res[SC_output[i*generate_times_from_ori_data+j]['predicted_result']]+=1    
    it = iter(res) 
    max=0
    ans=''
    for x in it:
        if res[x]>max:
            max=res[x]
            ans=x

    if ans==SC_output[i*generate_times_from_ori_data]['correct']:
        left_correct+=1


cost+=regenerate*len(wrong)


print('accuracy:'+str(float((left_correct+new_t)/(int)(len(SC_output)/generate_times_from_ori_data))))
print('cost:'+cost)