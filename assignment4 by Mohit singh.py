
# coding: utf-8

# In[1]:


print("welcome BADAss BABUA")


# In[4]:


a=10
b=20
print(a&b,a|b,a^b,~(~a),a<<2,b>>2)


# In[ ]:


a=0b0010011
c=0
while(a):
    a<<1
    if(a):
        c+=1
print(c)
    


# In[ ]:


print(c)


# In[ ]:


a=10
if(a):
    a-=1
    print(a)


# In[3]:


x="hello"
print("h" in x)
print("hello" is x)


# In[14]:


import math as m
a=5.766
b=8.09
print(a+b,a-b,m.ceil(a+b),m.floor(a+b),m.fabs(a-b),m.factorial(int(b+a)),m.sqrt(a+b),m.fmod(a,b),m.trunc(a),m.log1p(a),m.log2(b),m.log10(b))


# In[18]:


mark=int(input("enter marks"))
if mark>=40:
    print("pass")
elif mark >=38:
    print("pass by grace marks")
else:
    print("fail")


# In[19]:


#ODD EVEN
a=int(input("enter teh value"))
if a%2==0:
    print(a ,"is even")
else:
    print(a,"is odd")


# In[24]:


a=int(input("value"))
for i in range(2,a-1):
    if int((a%i))==0:
        print("prime")
    


# In[26]:


a=int(input("enter number"))
if a>=0 and a<=10:
    print(a,"lies between1 to 10")
else:
    print(a,"doesnot lies between 1 to 10")


# In[29]:


a=input("enter password ")
passwrd="heropanti"
if a==passwrd:
    print("u r welcome")
else:
    print("wrong password ")


# In[34]:


#nested if-else loop
a=int(input("person1 marks"))
b=int(input("2nd person marks"))
c=int(input("3rd person marks"))
if a>b:
    if b>c:
        print("person1 has highes marks , 2nd has 2nd highest and 3rd at 3rd highest")
    else:
        print("person1 has highes marks , 3rd has 2nd highest and 2nd at 3rd highest")
elif b>c:
    if a>c:
        print("person2 has highes marks , 1s has 2nd highest and 3rd at 3rd highest")
    else:
        print("person2 has highes marks , 3rd has 2nd highest and 1st at 3rd highest")
else:
    if a>b:
        print("person3 has highes marks , 1st has 2nd highest and 2nd at 3rd highest")
    else:
        print("perso3 has highes marks , 2nd has 2nd highest and 1 at 3rd highest")
        
        
        
        


# In[37]:


a=89
b=45
c=34
if(a>b and b>c):
    print("person1 has highes marks , 2nd has 2nd highest and 3rd at 3rd highest")


# In[ ]:


a=True
if a==True:
    print("yes")


# In[3]:


x=0
while x<=10:
    print(x,sep="\n")
    x=x+1


# In[4]:


a="hello"
for i in range(len(a)):
    print(a[i])
    


# In[2]:


a="hello"
b=len(a)
print(b)
for i in range(len(a)):
    print(a[i],sep=" ")


# In[8]:


a=0
max_m=20
for i in range(5):
    a+=int(input())
    
m=(a/(5*max_m))*100
print(m,"%")


# In[26]:


for i in range(8):
    for j in range(i+1):
        print("*",end=" ")
    print()


# In[28]:


get_ipython().run_line_magic('pinfo', 'print')


# In[ ]:


while(1):
    a=int(input())
    if a%2!=0 and a%3==0:
        a=a+4
        print(a)
    elif a%2==0:
        print("please enter odd no")
    else:
        print(a)
    


# In[ ]:


while(1):
    a=int(input())
    if a%4==0 and a%100!=0:
        print("leap year")
    else:
        print("not leap year")
             


# In[18]:


#QUES 3
import math as m
a=int(input())
for i in range(2,a):
    if a%i==0:
        print("not prime")
        break
    else:
        print("prime")
        


# In[16]:


while(1):
    a=int(input("les than 42"))
    assert a>42
    print(a)


# In[3]:


#ques 5
n=int(input())
b=1
c=0
d=0
for i in range(n+1):
    if i==0:
        b=1
    else:
        b=b*i
print(b)
while b>0:
    d=b%10
    b=b//10
    if d%2!=0:
        c+=1
print(c)


# In[2]:


#ques 4
a=int(input())
while(a!=42):
    print(a)
    a=int(input())


# # binary palindrome

# In[8]:


a=int(input())
b=str(bin(a))
b=b[2:]
c=b[-1::-1]
if b==c:
    print("binary palindrome",b,c)
else:
    print("not a binary palindrome",b,c)
    


# # Array 

# In[15]:


from array import *
a=array("u",['a','b','c'])
b=array(a.typecode,[c for c in a])
if(a==b):
    print("same")
else:
    print("diff")
print(a)


# In[29]:


a=array("i",[-1,2,3,4])
for i in range(len(a)):
    print(a[i],end=" ")
    print(float(a[i]),end=" ")


# In[25]:


a=array('i',[1,2,3,4,5,6,7,8])
b=int(input())
if b<=len(a):
    print(a[b])
else:
    print("error")


# In[31]:


print(a[len(a):1:-1])


# In[39]:


print(a[::-1])
print(a.reverse())


# In[56]:


a=input().split(' ') # splits lets u  to enter multiple input with space as array
m=[int(i) for i in a ]
sum=0
print(m)
for i in m:
    sum+=i
print("total ",sum,"%age",(sum/(15*len(a)))*100)


# In[ ]:


from array import *
import mohit.py
a=array("i",[1,2,3,4,5])
a.append(6)
a.extend([1,2,3])
b=a.count(2)
a.pop()
a.remove(3)
c=a.index(4)
#a.fromfile(mohit.py,2)
print(a,b,c)


# In[2]:


print("hey you  welcome back ")

