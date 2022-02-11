#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
from numpy import append
import cmath as cm
from math import pi 
from collections import Counter
import json


NTH = int(input("Enter the number of angles theta: "))
NPH = int(input("Enter the number of angles phi: "))
FNAME = input("Enter the file name: ")
COMMENTS = input("Enter the comments here: ")

count = 1 

knmax = 5000

delTh = pi/(NTH+1)
delPh = 2*pi/NPH
kth = np.zeros(knmax)
kph = np.zeros(knmax)
Kth = []
Kph = []
kth[count] = 0.0
kph[count] = 0.0
countList = [0]
lastLine = [99999, 99999, 1, 1]

for i in range (1, NTH + 1):
    th = (i * delTh)

    
    for j in range (1, NPH + 1):
        ph = j * delPh
        kth[count] = th
        kph[count] = ph
        countList.append(count)
        count = count + 1
        
        

kth[count]= pi
kph[count]= 0.0


for i in range (0, count + 1):
    Kth.append(kth[i])
    Kph.append(kph[i])
    #print(Kth,Kph)
    
    data = {'Comments': COMMENTS, 'Count': countList[-1], 'Theta angle': Kth, 'Phi angle': Kph, 'Last Line': lastLine}


with open('/Users/madisonderosier/Desktop/Research/' + FNAME + '.txt', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)


# In[ ]:




