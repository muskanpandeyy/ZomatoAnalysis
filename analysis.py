#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().system('pip install matplotlib')
get_ipython().system('pip install pandas plotly')



# In[7]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[10]:


dataframe = pd.read_csv("C:\\zomato\\Zomato-data-.csv")

print(dataframe.head())


# In[6]:


get_ipython().system('pip install seaborn')


# In[11]:


def handleRate(value):
    value=str(value).split('/')
    value=value[0];
    return float(value)

dataframe['rate']=dataframe['rate'].apply(handleRate)
print(dataframe.head())


# In[12]:


dataframe.info()


# In[22]:


sns.countplot(x=dataframe['listed_in(type)'], palette="Set2")
plt.xlabel("Type of restaurant")
plt.title("Restaurant Types Count")


# In[14]:


grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes': grouped_data})
plt.plot(result, c='green', marker='o')
plt.xlabel('Type of restaurant', c='red', size=20)
plt.ylabel('Votes', c='red', size=20)


# In[16]:


max_votes = dataframe['votes'].max()
restaurant_with_max_votes = dataframe.loc[dataframe['votes'] == max_votes, 'name']

print('Restaurant(s) with the maximum votes:')
print(restaurant_with_max_votes)


# In[24]:


sns.countplot(x=dataframe['online_order'], palette="Set1")
plt.xlabel("Online Order Availability")
plt.title("Count of Restaurants with Online Order Availability")


# In[26]:


plt.hist(dataframe['rate'], bins=5, color='yellow', edgecolor='black', histtype='bar', rwidth=0.8)
plt.title('Ratings Distribution')
plt.show()


# In[19]:


couple_data=dataframe['approx_cost(for two people)']
sns.countplot(x=couple_data)


# In[28]:


plt.figure(figsize = (6,6))
sns.boxplot(x = 'online_order', y = 'rate', data = dataframe,color='purple')


# In[21]:


pivot_table = dataframe.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)
sns.heatmap(pivot_table, annot=True, cmap='YlGnBu', fmt='d')
plt.title('Heatmap')
plt.xlabel('Online Order')
plt.ylabel('Listed In (Type)')
plt.show()


# In[ ]:




