
# coding: utf-8

# In[2]:


print("welcome BADASS BABUA")


# In[11]:


""" prog to fing hike 
 prog1"""
p=float(input("year1price")) #year 1 price
p2=float(input("year2 price")) #year2 price
if(p>p2): #compare price
    print("year 1 price was greater by:",(p-p2)) 
else:
    print("year2 price is greater by:",(p2-p))


# In[8]:


#ques2
a=int(input("value1"))
b=int(input("value2"))
z=((a*a)+(b*b)) #calculating z
print(z,z/(2*a*b)) #print thge values


# In[9]:


#ques 3
a=complex(input("enter complex no"))
b=complex(input("enter complex no 2"))
print(a,b)
#swap using 3rd var
c=a
a=b
b=c
print(a,b)
a=a+b
b=a-b
a=a-b
print(a,b)
if((a+b)==(b+a)):
    print("+ is commutative")
else:
    print("+ is not commutative ")
if((a-b)==(b-a)):
    print("- is commutative")
else:
    print("- is not commutative ")
if((a*b)==(b*a)):
    print("* is commutative")
else:
    print("* is not commutative ")
if((a/b)==(b/a)):
    print("/is commutative")
else:
    print("/ is not commutative ")


# In[12]:


#ques4
name=input("enter ur name")
dob=input("enter dob")
fname=input("father name")
college=input("college")
class=name #assign name to class
continue=dob #assign dob to continue


# In[16]:


#ques5
a=int(input("enter number"))
if(a%10==0):
    print("multiple of 10")
else:
    print("substract ",a-int(a/10)*10,"to make its multiple of 10")


# In[4]:


#ques6
a=45
b=0
while(a>22):
    a=a-6
    if(a==33):
        a=++a
    if(a==22):
        a=a-2
        break;
    b=b+1
print("he has to play",b ,"times to reach both conditions")
    
    

