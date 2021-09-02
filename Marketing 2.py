#!/usr/bin/env python
# coding: utf-8

# # Answers of the test file, sheet 2

# <font color="blue">Importing necessary library for analysis

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# <font color="blue">Reading the test file

# In[2]:


df=pd.read_excel(r'C:\Users\Carnival\Downloads\Data_Specialist_Test (9).xlsx', header=14, sheet_name="Performance Report")


# <font color='blue'>Wrangling the data

# In[3]:


df.head(8)


# <font color="blue">Clean the file by removal the unnamed column

# In[4]:


del df["Unnamed: 0"]


# <font color='blue'>Checking the type of data in the file

# In[5]:


df.dtypes


# <font color="blue">Visualizing the data for better insights

# In[6]:


df.groupby("Ad Source")["Revenue"].sum().plot(kind='bar');
plt.ylabel("Total revenue");
plt.title("Total revenues for both networks");


# In[7]:


df.groupby("Ad Source")["Impressions"].sum().plot(kind='bar')
plt.ylabel("Total impressions")
plt.yscale("log")
plt.title("Total impressions for both networks");


# In[8]:


df.groupby("Ad Source")["eCPM"].sum().plot(kind='bar')
plt.ylabel("Total eCPM");
plt.title("Total eCPM for both networks");


# **1.a) Which ad source network is performing the best? Based on which criteria are you making such conclusions? Revenue / eCPM / Impr, etc.?**
# ><font color="red">*Without unreserved doubt I choose Netwrok 1 as the best performing Network. Although Network 2 got more revenues and impressions than Network 1, Network 1 has a remarkable eCPM. Besides, Network1 has a low revenue because the impressions are low. Neverthless, Network 1 is more effective than Network 2. Bear in mind  that I am in the stakeholder's shoes.*

# <font color="blue">Summarizing the data for better insights

# In[9]:


App_Name=df.groupby("App Name").sum()


# <font color='blue'> Displaying the summarized data

# In[10]:


App_Name


# **1.b) Which app is performing the best? Based on which criteria are you making such conclusions? Revenue / eCPM / Impr, etc.?**
# ><font color="red">*I would choose App 1 because it has the highest revenue*

# **1.c)  How would you suggest to optimise these networks or what changes would you recommend? Which app would you allocate more resources to?**
# 
# ><font color="red">*To optimise the Netwroks, I would recommend getting more impressions for Network 1. Obviousuly, from the chart the more impressions it gets, the more revenue it achieves. On the other hand, Network 2 have better number in impressions and revenue, but it is not as effecient as Network 1 so the eCPM needs to be improved.*
#     
# ><font color="red">*In my opinion, more resources should be allocated to App 3 because it has the highest eCPM and second highest revenue and impressoins*

# **2. What other conclusion can you make from the data?**
# ><font color='red'>*The effectiveness / efficiency of the Network 2 might be affected by the zeros in revenues in both App 2 & App 4. If these zeroes are incorrect, obviously, this would lead to different conclusions.*
#     
# ><font color='red'>*App 1 in both Networks has the highest numbers in revenues and impressions*
#     
# ><font color='red'>*App 3 revenue's and impressions almost tripled in Network 2 in comparison to Network 1*

# **3. Make a simple graph based on the data and indicate what you want to highlight in its title.**
# ><font color='red'>*The figure below.*

# In[11]:


plt.figure(figsize=(14,6));
e_CPM= df[df.eCPM>0]
sns.barplot(x="App Name", y="eCPM", data=df, hue="Ad Source", ci=None, dodge=True);
plt.title("The best performing applications", fontsize=15);


# **4. What question would you ask your manager about this data set or this task?**
# ><font color='red'>*Are the data sources trustworthy?*
# 
# ><font color='red'>*What exactly do you want to find out?*
#     
# ><font color='red'>*Who are the end users of the analysis results?*
#     
# ><font color='red'>*How long these Networks are running? Are they equal in duration?*
