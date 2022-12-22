#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

data = pd.read_csv(r'E:\Files\ads.csv')


# In[2]:


data


# In[6]:


max(data['Age'])


# In[15]:


data['Age_cat']=pd.cut(data['Age'],bins=[17,30,45,60],labels=['Youth','Mid-age','Adult'])


# In[18]:


data_filtered = data.drop('Age',axis=1)


# In[19]:


data_filtered


# In[20]:


data_filtered['Age_cat'] = data_filtered['Age_cat'].astype('category') 


# In[21]:


data_filtered['Age_cat'].cat.codes


# In[29]:


df_1 = pd.get_dummies(data_filtered['Age_cat'], drop_first=True)


# In[35]:


df = pd.concat([data_filtered,df_1],axis=1)


# In[39]:


import numpy as np
df_new = pd.pivot_table(df,columns='Age_cat',values='EstimatedSalary',
              index='Purchased',aggfunc = (np.mean))


# In[41]:


df_new.T.plot(kind='bar')


# In[ ]:




