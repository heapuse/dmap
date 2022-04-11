"""It is important to define or select measures in data analysis/ However there is comonly/..."""
import math

def man(x,y):
    temp=0
    for i,j in zip(x,y):
        temp+=abs(i-j)
    print(temp)

def cos(x,y):
    num=0
    xval=0
    yval=0
    for i,j in zip(x,y):
        num+=(i*j)
        xval+=i*i
        yval+=j*j
    print(num/(math.sqrt(xval*yval)))

def ecu(x,y):
    temp=0
    for i,j in zip(x,y):
        temp+=(i-j)*(i-j)
    print(math.sqrt(temp))
    
def supremum(x,y):
    m=[]
    temp=0
    for i,j in zip(x,y):
        temp=abs(i-j)
        m.append(temp)
    print(max(m))
    
x=[1.5,2,1.6,1.2,1.5]
y=[1.7,1.9,1.8,1.5,1.0]

for i,j in zip(x,y):    
    x1=[i,j]
    y1=[1.4,1.6]
    man(x1,y1)
    cos(x1,y1)
    ecu(x1,y1)
    supremum(x1, y1)
    print("#################################3")


"""Consider the following Term-Frequency vector. 

Find Cosine similarity matrix of the given documents.
Also, find dissimilarity matrix by using 
Euclidean distance
Manhattan distance
Minkowski distance (h=3)
Supremum distance 
"""
import math

def man(x,y):
    temp=0
    for i,j in zip(x,y):
        temp+=abs(i-j)
    return (temp)

def cos(x,y):
    num=0
    xval=0
    yval=0
    for i,j in zip(x,y):
        num+=(i*j)
        xval+=i*i
        yval+=j*j
    return (num/(math.sqrt(xval*yval)))

def ecu(x,y):
    temp=0
    for i,j in zip(x,y):
        temp+=(i-j)*(i-j)
    return (math.sqrt(temp))

def h_3(x,y):
    temp=0
    for i,j in zip(x,y):
        temp+=(abs(i-j))**3
    return ((temp)**(1/3))
    
def supremum(x,y):
    m=[]
    temp=0
    for i,j in zip(x,y):
        temp=abs(i-j)
        m.append(temp)
    return (max(m))
    

d=[[5,0,3,0,2,0,0,2,0,0],[3,0,2,0,1,1,0,1,0,1],[0,7,0,2,1,0,0,3,0,0],[0,1,0,0,1,2,2,0,3,0]]


s=[]
d1=[]
d2=[]
d3=[]
d4=[]


for i in range(0,4):
    temp=[]
    for j in range(0,4):
        temp.append(man(d[i],d[j]))
    d1.append(temp)

for i in range(0,4):
    temp=[]
    for j in range(0,4):
        temp.append(ecu(d[i],d[j]))
    d2.append(temp)

for i in range(0,4):
    temp=[]
    for j in range(0,4):
        temp.append(supremum(d[i],d[j]))
    d3.append(temp)
    
for i in range(0,4):
    temp=[]
    for j in range(0,4):
        temp.append(h_3(d[i],d[j]))
    d4.append(temp)

for i in range(0,4):
    temp=[]
    for j in range(0,4):
        temp.append(cos(d[i],d[j]))
    s.append(temp)

print(d1)
print(d2)
print(d3)
print(d4)
print(s)
        

"""Dissimilarity between binary attributes:
Find the distance between objects (patients) by considering only on asymmetric attributes. (Gender is symmetric attribute.)

For the given data, find d(Jack, Jim), d(Jack, Mary), d(Jim, Mary).

Also, ensure that your program should work correctly for any other possible size of data.
"""
def bin_d(x,y):
    p=7
    m=0
    for i,j in zip(x,y):
        if(i==j):
            m=m+1
    print ((p-m)/p)
jack=['m','y','n','p','n','n','n']
jim=['m','y','y','n','n','n','n']
marry=['f','y','n','p','n','p','n']


bin_d(jack,jim)
bin_d(jack, marry)
bin_d(jim,marry)