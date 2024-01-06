#Mock Hackathon
#Level 1
import json

f1=open("C:/Users/TEMP/Desktop/Input data/level1a.json")
ip1=json.load(f1)
print(ip1)

n=ip1['n_neighbourhoods']
qty=[]
dMat=[[0 for i in range(n)]for j in range(n)]
k=0
for i in ip1['neighbourhoods']:
    qty.append(ip1['neighbourhoods'][i]['order_quantity'])
    for j in range(n):
        dMat[k][j]=ip1['neighbourhoods'][i]['distances'][j]
    k+=1

restDist=ip1['restaurants']['r0']['neighbourhood_distance']

capacity=ip1['vehicles']['v0']['capacity']
