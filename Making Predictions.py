#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import pickle


# In[3]:


clf = pickle.load(open('Model','rb'))


# In[6]:


# Predicting if a user gets the job 
# per1 ssc_p=68,hsc_p=66,degree_p=90,mba_p=85,work_ex=0,etest_p=79


# In[7]:


# Creating a list to store the values
# Remember to create a 2D list because model doesn't accepts 1D array
per_1 = [[68,66,90,85,0,79]]
per_2 = [[68,70,85,96,1,67]]


# In[14]:


per_1_pred = clf.predict(per_1)
if per_1_pred:
    print('User 1 got the job')
else:
    print("User 1 didn't got the job")


# In[15]:


per_2_pred= clf.predict(per_2)
if per_2_pred:
    print('User 2 got the job')
else:
    print("User 2 didn't got the job")


# In[ ]:




