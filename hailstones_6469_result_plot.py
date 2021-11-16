# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 23:17:00 2021

@author: Owner
"""

import pandas as pd
import math
import matplotlib.pyplot as plt
#df = pd.read_csv(r'bigstones (copy).csv')
df = pd.read_csv(r'C:\Users\Owner\Desktop\bigstones.csv')
ll = []
[ll.append(math.log10(int(i))) for i in df['12851.1'].tolist()]
plt.scatter(df['0'].tolist(), ll, s=0.8, alpha=0.5,marker='o', color='blue')
#plt.yscale('log')
plt.xlabel('iteration')
plt.ylabel('log10(n)')
plt.title('sampling of A348074 hailstone seq. seeded by 12851')


import math
def A158824(n, k): 
    if k==1:
        return math.comb(n+2, 3)  
    else: return (k-1)*math.comb(n-k+2, 2)

import math
# alternative crazy function
def A158824(n, k): 
    if k==1:
        return math.comb(bitflip(n), 3)  
    else: return (k-1)*math.comb(3*(n-k+2)+1, 2)


N = 50
ll = []
for i in range(1, N):
    for j in range(i):
        ll.append(A158824(i,j))
        
plt.scatter(range(len(ll)), ll, s=0.8, alpha=0.5,marker='o', color='black')
