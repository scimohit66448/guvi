
# coding: utf-8

# In[1]:


print('badass babua')


# In[12]:


a=42.0
b=43.9
c=43.9
d=67.0
print(int(a),int(b),int(c),int(d)) #convert to int from float\
print(bin(int(a)),bin(int(b)),bin(int(c)),bin(int(d))) #binary coversion
marks_list=[a,b,c,d]
print(marks_list)
tuple_marks=tuple(marks_list)
print(tuple_marks)
print(set(marks_list))
a=set(marks_list)
a[4]={56}
a[5]={65}
print(a)


# In[27]:


a="welcome to the computer science and engineering department MNIT allahabad "
print(a[:])
print(a[72:63:-1])
print(3*a[:])
a=["welcome","to allahabad"]
b=None
for i in a[0:len(a)]:
    b=b+a[i]   
    print(b)


# In[3]:


a={1,2,3,4} 
a= set add(5)
print(a)


# In[6]:


a=list(a)+[5,6]
print(set(a))
a=set(a)


# In[7]:


a.add(7)
print(a)

