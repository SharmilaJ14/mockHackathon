#Hackathon!
#Level 0: Travelling salesman problem
from typing import DefaultDict
import json

#Using Heuristics to solve it - Nearest Neighbour Heuristic
def travellingSalesman(G):
    visited=[False for i in range(len(G))]
    currentVertex=0
    path=[0]
    count=0
    while any(not i for i in visited):
        temp=G[currentVertex]
        print(path,count,temp)
        while(visited[currentVertex]==False):
            temp.remove(min(temp))
            minDist=min(temp)
            ind=[i for i,j in enumerate(G[currentVertex]) if j==minDist]
            if(len(ind)==1):
                if(visited[ind[0]]==False):
                    visited[currentVertex]=True
                    currentVertex=ind[0]
                    path.append(currentVertex)
                    count+=minDist
                else:
                    temp.pop(ind[0])
            else:
                for i in ind:
                    if(visited[i]==False):
                        visited[currentVertex]=True
                        currentVertex=i
                        path.append(currentVertex)
                        count+=minDist
                        break
                    else:
                        temp.pop(ind[0])
    return path,count

#Greedy Approach - finding the shortest path starting from vertex 0
def findMinRoute(tsp):
    sum = 0
    counter = 0
    j = 0
    i = 0
    min = 100000000
    visitedRouteList = DefaultDict(int)
    visitedRouteList[0] = 1
    path=[]
    route = [0] * len(tsp)
    while i < len(tsp) and j < len(tsp[i]):
        if counter >= len(tsp[i]) - 1:
            break
        if j != i and (visitedRouteList[j] == 0):
            if tsp[i][j] < min:
                min = tsp[i][j]
                route[counter] = j + 1
        j += 1
        if j == len(tsp[i]):
            sum += min
            min = 100000000
            visitedRouteList[route[counter] - 1] = 1
            path.append(route[counter]-1)
            j = 0
            i = route[counter] - 1
            counter += 1
    i = route[counter - 1] - 1
    for j in range(len(tsp)):
        if (i != j) and tsp[i][j] < min:
            min = tsp[i][j]
            route[counter] = j + 1
    sum += min
    return sum,path

#Using Nearest Neighbour Heuristic
cost=0
def tsp(c):
    global cost
    adj_vertex = 99999999
    min_val = 99999999
    visited[c] = 1
    print((c + 1), end=" ")
    for k in range(n):
        if (dMat[c][k] != 0) and (visited[k] == 0):
            if dMat[c][k] < min_val:
                min_val = dMat[c][k]
                adj_vertex = k
    if min_val != 99999999:
        cost = cost + min_val
    if adj_vertex == 99999999:
        adj_vertex = 0
        print((adj_vertex + 1), end=" ")
        cost = cost + dMat[c][adj_vertex]
        return
    tsp(adj_vertex)

#Using Twice around the tree
def findMST(G):
    mst=[]
    v=[i for i in range(len(G))]

def TwiceAroundTree(G):
    mst=findMST(G)

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
cost,route=findMinRoute(dMat)
visited=[0 for i in range(n+1)]
#print(tsp(0), cost)
op0={}
path=[]
for i in route:
    path.append(f"n{i-1}")
op0['v0']={"path":path}
print(op0)

#Output as file 
f=open("C:/Users/TEMP/Desktop/Input data/level0_output.json",'w')
json.dump(op0,f)

