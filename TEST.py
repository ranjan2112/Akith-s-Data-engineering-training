#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Python Request Module
import requests
url= 'https://en.wikipedia.org/wiki/Cricket_World_Cup'
data= requests.get(url)


# In[2]:


data


# In[3]:


dir(data)


# In[4]:


data.status_code


# In[5]:


data.content


# In[6]:


url= 'https://api.github.com/user/repos'#need authentication
token='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'
user='ranjan2112'
data= requests.get(url, auth=(user, token))


# In[7]:


data.json


# In[8]:


data.content


# In[9]:


data.json()


# In[10]:


len(data.json())


# In[11]:


#webscrapping using pandas
import pandas as pd


# In[12]:


url= 'https://en.wikipedia.org/wiki/Cricket_World_Cup'
data= pd.read_html(url)


# In[13]:


data


# In[14]:


type(data)


# In[15]:


data[0]


# In[ ]:


df1=pd.DataFrame(data[0])


# In[ ]:


df1


# In[16]:


data[2]


# In[ ]:


list=[5,10,15,20]

