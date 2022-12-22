#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data = pd.read_csv(r'E:\Files\ads.csv')


# In[2]:


data.head()


# In[5]:


x = data['Age']
data['Norm_age'] = (x - min(x))/(max(x) - min(x))


# In[7]:


data['std_age'] = (x-x.mean())/(x.std())


# In[12]:


data


# In[ ]:





# In[ ]:





# In[ ]:




