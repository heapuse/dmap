"""Consider the above data and perform the following operations
 Roll-up on location (from cities to countries)
Drill-down on time (from quarters to months)
Dice for (location=’Toronto’ or ‘Vancouver’ and (time=’Q1’ or ‘Q2’) and (item=’home entertainment’ or ‘computer’)
Slice for time = ‘Q1’
"""
def down(x):
    y=[]
    for i in x:
        temp=[]
        for j in i:
            temp.append(j/3)
        y.append(temp)
    print( y)
    
chicago=[[854,882,89,623],[943,890,64,698],[1032,924,59,789],[1129,992,63,870]]
new=[[1087,968,38,872],[1130,1024,41,925],[1034,1048,45,1002],[1142,1091,54,984]]
toronto=[[818,746,43,591],[894,769,52,682],[940,795,58,728],[978,864,59,784]]
van=[[605,825,14,400],[680,952,31,512],[812,1023,30,501],[927,1038,38,580]]

#roll up
us=[]
canada=[]

for x,y in zip(chicago,new):
    temp=[]
    for i,j in zip(x,y):
        temp.append(i+j)
    us.append(temp)
        
for x,y in zip(toronto,van):
    temp=[]
    for i,j in zip(x,y):
        temp.append(i+j)
    canada.append(temp)  

print(us)
print(canada)

#drill down 
down(chicago)
down(new)
down(toronto)
down(van)


#dice

temp1=[]
temp2=[]

temp1.append(toronto[0][0:2])
temp1.append(toronto[1][0:2])

temp2.append(van[0][0:2])
temp2.append(van[1][0:2])

print(temp1)
print(temp2)

#slice

print(chicago[0])
print(new[0])
print(toronto[0])
print(van[0])