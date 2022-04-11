"""
For the following vectors x and y, calculate the indicated similarity or distance measures.
x=(1, 1, 1, 1) , y= (2, 2, 2, 2) cosine, correlation, Euclidean
x=(0, 1, 0, 1) , y= (1, 0, 1, 0) cosine, correlation, Euclidean, Jaccard
x=(0, -1, 0, 1) , y= (1, 0, -1, 0) cosine, correlation, Euclidean
x=(1, 1, 0, 1, 0, 1) , y= (1, 1, 1, 0, 0, 1) cosine, correlation, Jaccard
x=(2, -1, 0, 2, 0, -3) , y= (-1, 1, -1, 0, 0, -1) cosine, correlation
"""
import math

def cosine(x,y):
    ytemp=0
    xtemp=0
    num=0
    for i,j in zip(x,y):
        num+=(i*j)
        xtemp+=i*i
        ytemp+=j*j
    print(num/math.sqrt((xtemp*ytemp)))
    
def jaccard(x,y):
    q=0
    r=0
    s=0
    for i,j in zip(x,y):
        if(i==1 and j==1):
            q+=1
        if(i==0 and j==1):
            s+=1
        if(i==1 and j==0):
            r+=1
    jaccard=0
    jaccard=q/(q+r+s)
    print(jaccard)
    
def euc(x,y):
    temp=0
    for i,j in zip(x,y):
        temp+=(i-j)*(i-j)
    print(math.sqrt(temp))
    

x=list(map(int,input("Enter X value: ").split(" ")))
y=list(map(int,input("Enter Y value: ").split(" ")))

cosine(x,y)
jaccard(x,y)
euc(x,y)

"""
This exercise compares and contrasts some similarity and distance measures.
For binary data, the Hamming distance is the number of bits that are different between two binary vectors. 
The Jaccard similarity is a measure of the similarity between two binary vectors. Compute the Hamming distance and the J
accard similarity between the following two binary vectors. 

X=0101010001
Y=0100011000
"""
x=list(map(int,input("Enter X value: ").split(" ")))
y=list(map(int,input("Enter Y value: ").split(" ")))

q=0
r=0
s=0
hamming=0

for i,j in zip(x,y):
    if(i==1 and j==1):
        q+=1
    if(i==1 and j==0):
        r+=1
        hamming+=1
    if(i==0 and j==1):
        s+=1
        hamming+=1

jaccard=0
jaccard=q/(q+r+s)

print(jaccard)
print(hamming)
        