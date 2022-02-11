#!/usr/bin/env python
# coding: utf-8

# In[27]:


from math import pi
import numpy as np
import cmath as cm
from collections import Counter
import json

DEG = pi/180.0
CI = (0.0,1.0)
nmax = 20000
knmax = 150
dsum = 0

VGFIN = input("Enter vgfin input file name: ")
VGFKV = input("Enter vgfkv input file name: ")
OUTFILE = input("Enter output file name: ")

with open("/Users/madisonderosier/Desktop/Research/" + VGFIN + ".txt",'r')as fp:    # Read in VGFIN file
    variable=fp.read()
    vgfin=json.loads(variable)


with open("/Users/madisonderosier/Desktop/Research/" + VGFKV + ".txt",'r')as fp:   # Read in VGFKV
    variable=fp.read()
    vgfkv=json.loads(variable)

wave = int(vgfin["Wavelength"])                    # This just reads in each individual variable and
alpha = int(vgfin["Incident theta angle"])         #     asigns them the variable that will be used
beta = int(vgfin["Value for phi"])                 #     to call them in the functions in this code
gama = int(vgfin["Value for gamma"])
psi = int(vgfin["Polarization angle"])
RAD = int(vgfin["Particle symmetry semi-axes"])
eps = complex(vgfin["EPS"])
er = float(vgfin["ER"])
ei = float(vgfin["EI"])
td = float(vgfin["TD"])
R = np.array(vgfin["R-vector"])
D = np.array(vgfin["D-vector"])
nsid = int(vgfin["Number of dipoles along major axes"])
nlsid = int(vgfin["Number of fine structure devisions per dipole cell side"])
mr = float(vgfin["Real part of index of refraction"])
mi = float(vgfin["Imaginary part of index of refraction"])
NUSE = int(vgfin["Counter"])

theta = np.array(vgfkv["Theta angle"])
phi = np.array(vgfkv["Phi angle"])
lastLine = np.array(vgfkv["Last Line"])

EPS = complex(er,ei)
mm = np.sqrt(EPS)
x = (EPS - 1.0)/(4.0* pi)
           
#for i in range(0,NUSE+1):       # This is supposed to be the loop that calls in each 
    #r = R(i)                    #     set of (x,y, and z) components of R and D in order
    #d = D(i)                    #     to calculate the total volume of the particle 
    #dsum = dsum + d**3          # Its currently commented out because it was returning an 
    #i+= 1                       #     error saying there were too many values in the R array?
                                 #     so I was very confused but wanted to make sure the rest of the code worked.
#print(dsum)

k = (2.0 * pi)/ wave            # Defines k
alpha = alpha*DEG               # The following makes the following variables in terms of radians
beta = beta*DEG
gamma = gamma*DEG
psi = psi*DEG

rot = Rot(alpha,beta,gamma)     # This is where Class ROT is called in and RRR can be 
RRR = rot.ROT()                 # Successfully executed!

print(RRR)

           


# In[13]:


from numpy.linalg import norm
from numpy import arange,array,pi,cos,sin,copy,sqrt
from matplotlib import pyplot as plt

class Rot:                                    # Class that will make array RRR to be
                                              # called into the main section of vgffmc
    def __init__(self,alpha,beta,gamma):      # The variables that must be called in are 
        self.alpha = alpha                    #   alpha, beta, and gamma
        self.beta = beta
        self.gamma = gamma
        
    def ROT(self):
        RRR = np.array(
          [[ cos(self.alpha)*cos(self.beta)*cos(self.gamma)-sin(self.alpha)*sin(self.gamma),
             sin(self.alpha)*cos(self.beta)*cos(self.gamma)+cos(self.alpha)*sin(self.gamma),
            -sin(self.beta)*cos(self.gamma)],
           [-cos(self.alpha)*cos(self.beta)*sin(self.gamma)-sin(self.alpha)*cos(self.gamma),
            -sin(self.alpha)*cos(self.beta)*sin(self.gamma)+cos(self.alpha)*cos(self.gamma),
             sin(self.beta)*sin(self.gamma)],
           [ cos(self.alpha)*sin(self.beta),
             sin(self.alpha)*sin(self.beta),
             cos(self.beta)]])
        return RRR                              # This is the array and returns it 
                                                #    with the name RRR so that we can 
alpha = 3                                       #    call it in
beta = 4
gamma = 2            

rot = Rot(alpha,beta,gamma)                      # This was just a test to see if it worked
RRR = rot.ROT()                                  #   p.s. it does! woohoo!


    


# In[ ]:




