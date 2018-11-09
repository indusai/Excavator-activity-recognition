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


#print(act_total_time)
Digging = {'Digging': [1,1]}
Swing = {'Swing': [1,1]}
Loading = {'Loading': [1,1]}

Digging['Digging'][1] = 3

#print(Digging)

num_cyc = 1
num_dig = 0
Dig = []
for n in range(len(new_acti_class)-1):
    a = new_acti_class[n]
    b = acti_class[n+1]
    if a == b:
        num_cyc = num_cyc
    else:
        num_cyc = 1+num_cyc

print(num_cyc)
cyc = int(num_cyc/4)
print(cyc)


#        Dig[1] = num_cyc

