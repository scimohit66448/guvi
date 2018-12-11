
# coding: utf-8

# In[31]:


from array import *
a=[]
b=0
c=0
a_grade=0
c1=0
a_grade1=0
m_count=0
mean=0
sum=0
a_grade2=None
for i in range(10):
    b=int(input())
    if b>=0 and b<= 100:
        a.append(b)
    else:
        print("wrong input")
        
print(a)
min_m=a[0] 
max_m=a[0]
for i in a:
    if i%2!=0: #part a
        c+=1
    if i>=75: #part b
        a_grade+=1
    if i==84 or i==74 or i==64 or i== 54 or i==44 or i==29: #part c
        ind=a.index(i)
        a[ind]=i+1
        #part d
    if i%2!=0:
        c1+=1
    if i>=75:
        a_grade1+=1
        #f part
    if a.count(i)>=a.count(m_count): 
        m_count=i
    sum=sum+i
    if i>max_m:
        max_m=i
    if i<min_m:
        min_m=i
mean=sum/len(a)
    #e part
i=int(len(a)/2)
j=int(len(a)/2+1)
b=a[i-1:j+1]
#g part
if m_count>84:
    a_grade2="a+"
elif m_count>74:
    a_grade2="a"
elif m_count>64:
    a_grade2="b+"
elif m_count>54:
    a_grade2="b"
elif m_count>44:
    a_grade2="c"
elif m_count>30:
    a_grade2="d"
else:
    a_grade2="fail"

        #h part
"""min_a=min(a)
max_a=max(a)"""
    



print(c,a_grade,a,c1,a_grade1,min_m,max_m,m_count,mean,a_grade2,b) #all results


        
    


# # ques 2 assignment 5

# In[45]:


str=[]
a="MNNIT ALLAHBAD"
for i in a:
    str.append(i)
print(str)
for i in str:
     if i== 'i' or i=='e' or i=='a'or i=='o' or i=='u' or i== 'I' or i=='E' or i=='A'or i=='O' or i=='U': #part a
        print("index of",i,"is",str.index(i))
print(set(a)) #part b
b=set(a) # part c
for i in b:
    print("f of ",i,"is",a.count(i))
    


# In[47]:





# In[44]:


from numpy import *
import copy as c
a=array([1,2,3,4,])
print(a)
b=zeros(10,dtype=int)
for i in range(10):
    a=int(input())
    b[i]=a
print(b)
d=c.copy(b)


print(d)


# In[31]:


import numpy as np
import math as m
a=np.zeros(5,dtype=int)
b=np.ones(5,dtype=int)
"""for i in range(5):
    j=int(input("value if 1st array"))
    a[i]=j
for i in range(5):
    j=int(input("value if 2nd array"))
    b[i]=j
for i in range(5):
    a[i]=a[i]+5
    b[i]=b[i]+7"""
    

print(a,b,a+b,a-b,a/b,np.log(a+b),abs(a+b),np.mean(a),np.median(a),np.sort(a+b),np.cov(a+b),np.std(a+b),np.sqrt(b),np.cos(a),np.sin(a),np.max(a)) #part a and b





# In[28]:


#ques 4
import numpy
a=numpy.array([[4,7,-6],[3,0,8],[2,0,-4]])
e=0
f=0
sum=0
print(a)
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j]==numpy.max(a):
            e=i
            f=j
            
        if i==j:
            sum+=a[i][j]
        print(a[i][j])
c=a[1][1]
a[1][1]=numpy.max(a)
a[e][f]=c
b=a.flatten()
print(numpy.max(a),a,e,f,b,sum)   
y=numpy.rot90(x,k=3)
print(y)
       


# In[68]:


import numpy as np
from array import *
a=np.array(["vns","ald","mum","del","kol"])
a[0]="ahm"
a=np.append(a,["chen"])
print(a[0],a[len(a)-1],a)


# In[78]:


import numpy as n
a=n.arange(1,10,1)
print(a)


# In[17]:


import numpy as np
n1=int(input("size of arrays"))
a=np.zeros(n1,dtype=int)
b=np.ones(n1,dtype=int)
for i in range(n1):
    j=int(input("value if 1st array"))
    a[i]=j
for i in range(n1):
    j=int(input("value if 2nd array"))
    b[i]=j
if all(a>b):
        print("a>b")
elif(any(a>b)):
        print("atleast 1 is greater in a")
else:
    print("b>a")
if np.logical_and(a.all()>5,a.all()<10):
    print("true")
else:
    print("false")
c=np.where(a>=5,True,False)
print(a==b,a>b,a<b,a>=b,a<=b,c)


# In[35]:


import numpy as np
a=np.arange(1,10)
b=a.view()
c=a.copy()
c[0]=109
b[0]=99
print(a[::-1],b,c,a.ndim,a.shape,a.size,a.dtype,a.reshape(3,3),a.reshape(3,3).flatten())


# In[22]:


import numpy as np
n1=int(input("size"))
a=np.zeros((n1,n1),dtype=int)
for i in range(n1):
    for k in range(n1):
        j=int(input("value if 1st array"))
        a[i][k]=j
"""for i in range(n1):
    j=int(input("value if 2nd array"))
    b[i]=j"""
print("row wise")
for i in range(len(a)):
    print("row:",i)
    for j in range(len(a[i])):
        print(a[i,j],end=" ")
    print()
print("column wise")
for i in range(len(a)):
    print("column:",i)
    for j in range(len(a[i])):
        print(a[j,i])
    print(end=" ")
print(a.flatten(),a,a[1:3,0:2].reshape(1,4),sep="\n")


# In[24]:


import numpy as np
n1=int(input("size"))
a=np.zeros((n1,n1),dtype=int)
for i in range(n1):
    for k in range(n1):
        j=int(input("value if 1st array"))
        a[i][k]=j
"""for i in range(n1):
    j=int(input("value if 2nd array"))
    b[i]=j"""
print("row wise")
for i in range(len(a)):
    print("row:",i)
    for j in range(len(a[i])):
        print(a[i,j],end=" ")
    print()
print("column wise")
for i in range(len(a)):
    print("column:",i)
    for j in range(len(a[i])):
        print(a[j,i])
    print(end=" ")
print(a.flatten(),a,a[:,:],"transpose:",np.transpose(a),"daigonal:",np.diagonal(a),sep="\n")

