from ast import Pow
from ctypes.wintypes import FLOAT
from hashlib import new
from re import I, M
from flask import g
import pandas as pd
df=pd.read_csv('main.csv')
mass=df['Mass'].tolist()
radi=df['Radius'].tolist()
New=[]
new0=[]
new1=[]
for i in range(1,50,2):
    m=float(mass[i])*1.989e+30
    New.append(m)
    R=float(radi[i])*6.957e+8
    new0.append(R)
    g=6.67*pow(10,-11)*(m/pow(R,2))
    new1.append(g)
newdf=pd.DataFrame({'mass':New,'radious':new0,'gravity':new1})
newdf.to_csv('calcutate.csv')