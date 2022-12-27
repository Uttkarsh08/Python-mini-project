#!/usr/bin/env python
# coding: utf-8

# In[1]:


names=input('Enter the name of students: ').split(',')
marks=list(map(int,input('Enter the marks of the students: ').split(',')))
up=list(map(int,input('Enter the marks to be updated: ').split(',')))
upmarks=[x+i for x,i in zip(marks,up)]
record=dict(zip(names,marks))
uprecord=dict(zip(names,upmarks))
marks.sort(key=None,reverse=True)
sortrecord={}
for i in marks:
    for j in names:
        if record[j]==i:
            sortrecord[j]=i
            upmarks.sort(key=None,reverse=True)
            x={}
for i in upmarks:
    for j in names:
        if uprecord[j]==i:
            x[j]=i
k=list(record.keys())
v=list(record.values())
[print(f'{k[i]}\t\t{v[i]}') for i in range(len(k))]
print('Student\tMarks')
print(x)
y=list(x.keys())[0]
n=list(sortrecord).index(y)
print(f'{y} jumped {n} position(s)')


# In[ ]:




