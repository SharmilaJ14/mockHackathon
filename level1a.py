#Mock Hackathon
#Level 1
import json
def findSlots(qty):  
    slots=[]
    while(True):
        if(len(qty)==0):
            return slots
        if(len(qty)==1):
            slots.append([qty[0]])
            return slots
        dp=[[0 for i in range(capacity+1)] for j in range(len(qty)+1)]
        for i in range(len(qty)+1):
            dp[i][0]=0
            dp[0][i]=0
        for i in range(1,len(qty)+1):
            for j in range(1,capacity+1):
                if(j>qty[i-1]):
                    dp[i][j]=max(dp[i-1][j],dp[i-1][j-qty[i-1]]+qty[i-1])
                else:
                    dp[i][j]=dp[i-1][j]
        path=[]
        i=len(qty)
        j=capacity
        while(i>0 and j>0):
            if(dp[i-1][j]==dp[i][j]):
                i=i-1
            else:
                path.append(qty[i])
                if(j-qty[i-1]>0):
                    j=j-qty[i-1]
                    i-=1
                else:
                    break
        slots.append(path)
        temp=[qty[i] for i in range(len(qty)) if qty[i] not in path]
        qty=temp
    return slots

"""def findSlots(restDist,dMat):
    catered=[]
    while(True):
        qtySent=0
        currentVertex=-1
        while(qtySent<capacity):
            slot=[]
            if(currentVertex==-1):
                ratio=[qty[i]/restDist[i] if restDist[i]!=0 else 9999999999 for i in range(n)]
                maxRatio=max(ratio)
                index=[i for i,j in enumerate(ratio) if j==maxRatio]
                restDist.pop(index[0])
            else:
                ratio=[qty[i]/dMat[currentVertex][i] if dMat[currentVertex][i]!=0 else 9999999999 for i in range(n)]
                maxRatio=max(ratio)
                index=[i for i,j in enumerate(ratio) if j==maxRatio]
                restDist.pop(index[0])
            if(qtySent+qty[index[0]]<capacity):
                qtySent+=qty[index[0]]
                slot.append(currentVertex)
                currentVertex=index[0]
            else:
                catered.append(slot)
    return catered"""
        

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

print(findSlots(qty)) 

"""capacity=70
qty=[30,20,40,10,50]
dMat=[[0,2,3,3,6],
      [2,0,2,7,7],
      [3,2,0,6,8],
      [3,7,6,0,4],
      [6,7,2,4,0]]
rDist=[2,3,5,1,4]
slots=[]"""

#Approach1: Finding slots through 0/1 Knapsack then TSP for each Slot is performed to find path. 

"""def findSlots(qty,capacity):
    slots=[]
    while(True):
        path=[]
        c=0
        while(c<capacity):
            print(c,qty,slots,path)
            if(len(qty)==0):
                return slots
            index=[i for i,j in enumerate(qty) if j==max(qty)]
            path.append(index[0])
            temp=[qty[i] for i in range(len(qty)) if i!=index[0]]
            qty=temp
        slots.append(path)"""

slots=findSlots(qty)
print(slots)

