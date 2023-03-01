#!/usr/bin/env python
# coding: utf-8

# # Welcome to numpy

# In[1]:


import numpy as np


# In[2]:


myarr = np.array([[3,6,7,8]], np.int64) # I'm going to use 8bit integer


# In[3]:


myarr


# In[4]:


myarr[0,1]


# In[5]:


myarr.shape


# In[6]:


myarr.dtype


# In[7]:


myarr[0,1] = 32


# In[8]:


myarr


# # Array creation from conversion from other structure

# In[12]:


listarry = np.array([[1,4,7],[2,5,7],[3,6,8] ])


# In[13]:


listarry


# In[14]:


listarry.dtype


# In[15]:


listarry.shape


# In[16]:


listarry.size


# In[17]:


zeros = np.zeros((2,5))


# In[18]:


zeros


# In[20]:


rng = np.arange(15)


# In[21]:


rng


# In[22]:


lspace = np.linspace(1, 5, 12)


# In[23]:


lspace


# In[24]:


emp = np.empty((4,6))


# In[25]:


emp


# In[28]:


empty_like = np.empty_like(lspace)


# In[29]:


empty_like


# In[30]:


ide = np.identity(45)


# In[31]:


ide


# In[32]:


arr = np.arange(99)


# In[33]:


arr


# In[35]:


arr = arr.reshape(3,33)


# In[36]:


arr


# In[37]:


arr.ravel()


# # Numpy Axis

# In[39]:


x = [[1,2,3], [4,5,6], [7,1,0]]


# In[42]:


ar = np.array(x)


# In[43]:


ar


# In[44]:


ar.sum(axis=0)


# # Numpy attributes and methods

# In[45]:


ar.T # Transforms rows into columns


# In[46]:


ar.flat


# In[47]:


for item in ar.flat:
    print(item)


# In[49]:


ar.ndim


# In[50]:


ar.size


# In[51]:


ar.nbytes


# # Array Methods

# In[58]:


one = np.array([1,3,4,5,6])


# In[59]:


one


# In[60]:


one.argmax()


# In[61]:


one.argmin()


# In[62]:


one.argsort()


# In[63]:


ar


# In[64]:


ar.argmax()


# In[65]:


ar.argmin()


# In[66]:


ar.argmax(axis=0)


# In[67]:


ar.argmax(axis=1)


# In[68]:


ar.ravel()


# # Mathematical Operation provide by the Numpy

# In[69]:


ar2 = np.array([[1, 4, 3],
       [4, 0, 6],
       [8, 1, 0]])


# In[70]:


ar + ar2


# In[71]:


ar * ar2


# In[72]:


np.sqrt(ar)


# In[74]:


ar.sum()


# In[75]:


ar.max()


# In[76]:


ar.min()


# In[77]:


ar


# In[78]:


np.where(ar>5)


# In[79]:


type(np.where(ar>5))


# In[80]:


np.count_nonzero(ar)


# In[81]:


np.nonzero(ar)


# In[82]:


ar[1,2] = 0


# In[83]:


np.nonzero(ar)


# # Numpy occupy less space

# In[84]:


import sys


# In[85]:


ch_ar = [0, 4, 55, 2]


# In[88]:


np_ar = np.array(ch_ar)


# In[90]:


sys.getsizeof(1) * len(ch_ar)


# In[92]:


np_ar.itemsize * np_ar.size


# In[ ]:




