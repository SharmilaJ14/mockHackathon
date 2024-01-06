#KLA Hackathon!
#Level 0: Travelling salesman problem
import json

#Importing the data
f0=open("C:/Users/TEMP/Desktop/Input data/level0.json")
ip0=json.load(f0)

#Constructing a distance graph using given inputs - preprocessing of data
dGraph={}
n=ip0['n_neighbourhoods']
dGraph['r0']=ip0['restaurants']['r0']['neighbourhood_distance']
for i in ip0['neighbourhoods']:
    dGraph[i]=ip0['neighbourhoods'][i]['distances']

#Converting dictionary to adjustancy matrix
dMat=[[0 for i in range(n+1)]for j in range(n+1)]
k=0
for i in dGraph:
    dMat[k][0]=dGraph['r0'][k-1] if k>0 else 0
    for j in range(1,len(dGraph[i])+1):
        dMat[k][j]=dGraph[i][j-1]
    k+=1

#Fixing 'r0' vertex to be the first and last vertes and then solving travelling salesman problem
