#Mock Hackathon
#Level 1
import json

def findSlots(restDist,dMat):
    catered=[]
    while(True):
        qtySent=0
        currentVertex=-1
        while(qtySent<capacity):
            slot=[]
            if(currentVertex==-1):
                ratio=[qty[i]/restDist[i] if restDist[i]!=0 else 9999999999 for i in range(n)]
                minRatio=min(ratio)
                index=[i for i,j in enumerate(ratio) if j==minRatio]
                restDist.pop(index[0])
            else:
                ratio=[qty[i]/dMat[currentVertex][i] if dMat[currentVertex][i]!=0 else 9999999999 for i in range(n)]
                minRatio=min(ratio)
                index=[i for i,j in enumerate(ratio) if j==minRatio]
                restDist.pop(index[0])
            if(qtySent+qty[index[0]]<capacity):
                qtySent+=qty[index[0]]
                slot.append(currentVertex)
                currentVertex=index[0]
            else:
                catered.append(slot)
    return catered
        

f1=open("C:/Users/TEMP/Desktop/Input data/level1a.json")
ip1=json.load(f1)

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

print(findSlots(restDist,dMat))



