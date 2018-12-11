
# coding: utf-8

# In[55]:
#QUESTION1

import numpy as np
m=int(input("no of students"))
n=int(input("no of sub"))
mark=np.zeros((m,n),dtype=int)
y=np.zeros(m,dtype=int)
c=0
k=0
sum=0
for i in range(m):
    for j in range(n):
        a=int(input("marks ofstudent"))
        if a>=0 and a<=100:
            mark[i,j]=a
        else:
            a=int(input("enter correct marks of above "))
            mark[i,j]=a
for i in range(m):
    sum=0
    for j in range(n):
        sum+=mark[i,j] #sum  of marks
        y[k]=sum  #array of sum of marks of eac student
    k+=1
    print("averge of student",i,":",sum/n)
x=np.sort(y) #sort the sum
z=np.copy(x[::-1]) #reverse to get decreasing order
#find the rank of student
for k in range(len(y)):
    for j in range(len(x)):
        if z[k]==y[j]:
            print("student",j+1,"is at positon",(k+1))
            break
k=0
for i in range(m):
    sum=0
    for j in range(n):
        sum+=mark[j,i] #sum of marks in each sub of all student
        y[k]=sum       #array of sum
    k+=1
#check which sub is hard or easy
for i in range(len(y)):
    if y[i]==max(y):
        print("subject",i+1,"is easy")
    if y[i]==min(y):
        print("sub",i+1,"is hard")
print(y,x,z)
for i in (m)

    #print("averge ofsub",i,":",sum/n)
          


# In[35]:

#QUES 2
import numpy as np
a=np.zeros((3,3),dtype=int)
for i in range(3):
    for j in range(3):
        a[i,j]=int(input())
b=a.flatten() #flatten array
c=np.sort(b) #sort flattened array
print(c.reshape(3,3)) #reshape to get output
print(np.sort(a))


# In[57]:
#QUES3

import numpy as np
m=int(input("no of students")) #no of students
n=int(input("no of sub"))
s_c=int(input("no of sub to choose")) #no of sub to choose
m_q=int(input("totalmarks to qualify")) #marks to qualify
mark=np.zeros((m,n),dtype=int)
#array 
b=np.zeros((m,2),dtype=int)
for i in range(m):
    for j in range(n):
        a=int(input("marks ofstudent"))
        if a>=0 and a<=100:
            mark[i,j]=a
        else:
            a=int(input("enter correct marks of above "))
            mark[i,j]=a
z=np.sort(mark)
print(mark,z)
print(z[:,len(z)-2:len(z)])
for i in range(len(z)):
    if np.sum(z[i:i+1,len(z)-(s_c):len(z)+1])>m_q: #to find who qualifies
        print(i+1,"student is pass")
    else :
        print(i+1,"student not pass")

