#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import numpy as np
import pandas as pd


# In[2]:


df_online=pd.read_csv("https://raw.githubusercontent.com/fivethirtyeight/data/master/media-mentions-2020/online_weekly.csv")
df_online.head()


# In[3]:


dfO= df_online[['name','matched_stories']]

dfO= dfO.groupby("name")["matched_stories"].sum()
dfO = pd.DataFrame(dfO)

dfToShow= dfO.sort_values("matched_stories", ascending=False)
dfToShow.head()


# In[4]:


import streamlit as st
st.bar_chart(dfToShow)
st.title("ARando")
st.selectbox("Select Dataset",("A"))


# In[ ]:


'''
# Creating Web Apps with JN and Streamlit
## Christian F. Jung
christianfjung.com

**About this Project** 

This project uses live poll data from 538 so the website will be update constantly!

'''



# In[ ]:




