#!/usr/bin/env python
# coding: utf-8

# In[28]:


import numpy as np
import cmath as cm
from collections import Counter
import json

w = float(input("Enter the wavelength: "))
NSID = int(input("Enter the number of dipoles along the major axes: "))
NLSID = int(input("Enter the number of fine structure devisions per dipole cell side: "))
RAD = float(input("Enter the particle symmetry semi-axes (z-axes radius): "))
alpha = float(input("Enter the incident theta (in degrees): "))
beta = float(input("Enter the value for phi (in degrees): "))
gamma = float(input("Enter the value for gamma (in degrees): "))
psi = float(input("Enter the polarization angle (in degrees): "))
MR = float(input("Enter the real part of the the index of refraction: "))
MIstring = (input("Enter the imaginary part of the index of refraction: "))
MI = float(MIstring)
ARstring = (input("Enter the aspect ratio (major axis/minor axis): ")) 
AR = float(ARstring)
COMMENTS = input("Enter the file comments: ")
OUTFILE = input("Enter the output filename: ")

def SD(W,MI):
    if MI == 0:
        return SD == 0
    else:
        return SD == (W/(2*np.pi*MI))
    return SD

Max = max(RAD, (RAD/AR))

TD = ((2*Max)/NSID)

if MI < 0:
    MI = -MI
M = complex(MR,MI)

DRF = 0.5*(NSID - 1)

LD = TD/NLSID

FRAC = 1/(NLSID**3)

NUSE = 0

INCNT = 0 

temp = 0

R = np.empty([0,3])
D = np.empty([0,1])

for i in range (1, NSID):
    for h in range (1, NSID):
        for g in range (1, NSID):
            x = (i - DRF)*TD
            y = (h - DRF)*TD
            z = (g - DRF)*TD
   
            
            for IX in range (1, NLSID):
                for IY in range (1, NLSID):
                    for IZ in range (1, NLSID):
                        RF1 = x + LD*(0.5*(1.0 - NLSID) + IX)      
                        RF2 = y + LD*(0.5*(1.0 - NLSID) + IY)
                        RF3 = z + LD*(0.5*(1.0 - NLSID) + IZ)
                
                        INSIDE = np.sqrt(abs((RF1/(RAD**2/AR**2))) + np.sqrt(abs((RF2/(RAD**2/AR**2))) + np.sqrt(abs((RF2/RAD**2)))))
                        if INSIDE < 1:
                            INCNT = INCNT + 1
                        IZ += 1
                    IY += 1
                IX += 1
                        
                        
                        
            if INCNT > 0:
                R = np.append(R, np.array([[x,y,z]]), axis = 0) 
                D = np.append(D, [[NUSE]], axis = 0)
                NUSE = NUSE + 1
            if (NUSE%100) == 0:
                print (f'NUSE = {NUSE}')
            
            g += 1
        h += 1
    i += 1
    INCNT = 0        
print(type(R))
print(R)
print("Nuse values:", D)

            
#print (COMMENTS)
#print (NUSE)
#print (w, alpha, beta, gamma, psi, RAD)
EPS = complex(M*M)
ER = EPS.real
EI = EPS.imag
#print (EPS,ER, EI, TD)


data={
    'Comments': COMMENTS, 
    'Counter': NUSE,
    'Wavelength': w, 
    'Incident theta angle': alpha, 
    'Value for phi': beta,
    'Value for gamma': gamma, 
    'Polarization angle': psi, 
    'Particle symmetry semi-axes': RAD,
    'EPS': str(EPS), 
    'ER': str(ER), 
    'EI': str(EI), 
    'TD': str(TD),
    'R-vector': str(R),
    'D-vector': str(D),
    #temp = temp + D(i)**3
    'Number of dipoles along major axes': NSID,
    'Number of fine structure devisions per dipole cell side': NLSID,
    'Real part of index of refraction': MR, 
    'Imaginary part of index of refraction': MI
}


with open('/Users/madisonderosier/Desktop/Research/' + OUTFILE + '.txt', 'w') as fp:
    variable=json.dumps(data, indent=4)
    fp.write(variable)
    


# In[ ]:





# In[ ]:




