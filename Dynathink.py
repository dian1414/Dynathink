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
end=5       

left_end=8 # extra queries of 'slow' questions

SC_end=10  # total number of queries of one question


for i in range(0,(int)(len(SC_output)),SC_end):
    # our method
    res = {}
    step_cal={}
    min=1000
    for j in range(start,end):
        if len(SC_output[i+j]['steps'])<min:
            min=len(SC_output[i+j]['steps'])
        if SC_output[i+j]['predicted_result']!=None:
            if SC_output[i+j]['predicted_result'] not in res:
                res[SC_output[i+j]['predicted_result']]=1
            else:
                res[SC_output[i+j]['predicted_result']]+=1
            if SC_output[i+j]['predicted_result'] not in step_cal:
                step_cal[SC_output[i+j]['predicted_result']]=len(SC_output[i+j]['steps'])
            else:
                if step_cal[SC_output[i+j]['predicted_result']]>len(SC_output[i+j]['steps']):
                    step_cal[SC_output[i+j]['predicted_result']]=len(SC_output[i+j]['steps'])
    ans_t=''
    step_t=0
    max=0
    for x in res:
        if res[x]>max:
            ans_t=x
            step_t=step_cal[x]
            max=res[x]
    ans=''
    if max>=int(end/2)+1:
        if min==step_t:
            tot1+=1
            ans=ans_t


        else:   
            tot2+=1   
            res_left = {}
            for j in range(start,left_end):
                if SC_output[i+j]['predicted_result']!=None:
                    if SC_output[i+j]['predicted_result'] not in res_left:
                        res_left[SC_output[i+j]['predicted_result']]=1
                    else:
                        res_left[SC_output[i+j]['predicted_result']]+=1
            ans=''
            max=0
            for x in res_left:
                if res_left[x]>max:
                    ans=x
                    max=res_left[x]
            if ans==SC_output[i]['correct']:
                cnt1+=1
        if ans==SC_output[i]['correct']:
            cnt1+=1

    else:      
        tot2+=1
        res_left = {}
        for j in range(start,left_end):
            if SC_output[i+j]['predicted_result']!=None:
                if SC_output[i+j]['predicted_result'] not in res_left:
                    res_left[SC_output[i+j]['predicted_result']]=1
                else:
                    res_left[SC_output[i+j]['predicted_result']]+=1
        ans=''
        max=0
        for x in res_left:
            if res_left[x]>max:
                ans=x
                max=res_left[x]
        if ans==SC_output[i]['correct']:
            cnt1+=1

    # SC
    res_SC = {}
    for j in range(start,SC_end):
        if SC_output[i+j]['predicted_result']!=None:
            if SC_output[i+j]['predicted_result'] not in res_SC:
                res_SC[SC_output[i+j]['predicted_result']]=1
            else:
                res_SC[SC_output[i+j]['predicted_result']]+=1
    ans=''
    max=0
    for x in res_SC:
        if res_SC[x]>max:
            ans=x
            max=res_SC[x]
    if ans==SC_output[i]['correct']:
        cnt_sc+=1


print('our cost:'+str(tot1*end+tot2*left_end))
print('our acc:'+str(float(cnt1/(int)(len(SC_output)/10))))
print('----------------------------------------------------')
print('SC cost:'+str((int)(len(SC_output)/10)*SC_end))
print('SC acc:'+str(float(cnt_sc/(int)(len(SC_output)/10))))
