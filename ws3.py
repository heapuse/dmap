"""Consider the  following data (in increasing order) for the attribute age:
 13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70. 
Use smoothing by bin means to smooth these data, using a bin depth of 3. 
Use smoothing by bin median to smooth these data, using a bin depth of 3. 
Use smoothing by bin boundaries to smooth these data, using a bin depth of 3. 
"""
def bin_mean(x):
    temp=[]
    inc=0
    
    for i in range(len(x)//b):
        s=0
        for j in range(b):
            s+=x[j+inc]
        inc+=b
        for j in range(b):
            temp.append(s/b)
    print(temp)
            
            
def bin_med(x):
    temp=[]
    inc=1

    for i in range(len(x)//b):
        for j in range(b):
            temp.append(x[inc])
        inc+=b
    print(temp)
    
def bin_boundry(x):
    temp=[]
    inc=0
    
    for i in range(len(x)//b):
        for j in range(b):
            if(j==1):
                if(x[inc+j]-x[inc+j-1]>x[inc+j+1]-x[inc+j]):
                    temp.append(x[inc+j+1])
                else:
                    temp.append(x[inc+j-1])
            else:
                temp.append(x[inc+j])
        inc+=b
                
    print(temp)
    
x=[13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70]

b=3

bin_boundry(x)
bin_mean(x)
bin_med(x)
