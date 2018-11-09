import os
import sys
import json
import subprocess
import numpy as np

num_loa = 0
num_swi = 0
num_dig = 0

new_acti_class = ['Digging', 'Digging', 'Digging', 'Digging', 'Digging', 'Digging',
              'Digging', 'Digging', 'Swing', 'Swing', 'Swing', 'Swing', 'Swing',
              'Swing', 'Swing', 'Swing', 'Swing', 'Loading', 'Loading', 'Loading',
              'Loading', 'Loading', 'Loading', 'Loading', 'Loading', 'Swing', 'Swing',
              'Swing', 'Swing', 'Swing', 'Swing', 'Swing', 'Swing','Digging', 'Digging', 'Digging', 'Digging', 'Digging', 'Digging']


list_swi = []
for i in range(len(new_acti_class)):

#    print(new_acti_class[i])
#    activity_dic = {'Digging':'a', 'Swing':'b', 'Loading':'c'}
    if new_acti_class[i] == 'Digging':
        num_dig = 1+num_dig
    else:
        if new_acti_class[i] == 'Swing':
            num_swi = 1+num_swi
        else:
            num_loa = 1+num_loa
            list_num = [i]

    print(num_swi)

    list_swi.append(num_swi)
print(list_swi)




'''   act_total_time = []
    act_total_time.append(num_dig*0.04)
    act_total_time.append(num_swi*0.04)
    act_total_time.append(num_loa*0.04)




num_cyc = 1

Dig = []
for n in range(len(new_acti_class)-1):
    a = new_acti_class[n]
    b = new_acti_class[n+1]
    if a == b:
        num_cyc = num_cyc
    else:
        num_cyc = 1+num_cyc

#print(num_cyc)
cyc = int(num_cyc/4)
print(cyc)
print(act_total_time)

print('total cycle: '+str(cyc))
print('Activity time: '+ 'Digging-'+str(act_total_time[0])+'s '+'Loading-'+str(act_total_time[1])+'s '
      +'Swing-'+str(act_total_time[2])+'s')'''

