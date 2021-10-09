# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 23:17:00 2021

@author: Owner
"""

import pandas as pd
import math
import matplotlib.pyplot as plt
df = pd.read_csv(r'bigstones (copy).csv')
ll = []
[ll.append(math.log10(int(i))) for i in df['6469.1'].tolist()]
plt.scatter(df['0'].tolist(), ll, s=0.8, alpha=0.5,marker='o', color='blue')
#plt.yscale('log')
plt.xlabel('iteration')
plt.ylabel('log10(n)')
plt.title('sampling of A348074 hailstone seq. seeded by 6469')