#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))


# ### Avg. Time Spend on Social Media Analysis (EDA)

# In[4]:


df=pd.read_csv('D:\\ML project\\Average Time Spent By A User On Social Media\dummy_data.csv')
df


# In[5]:


df.describe()


# In[6]:


df.isnull().sum()


# In[7]:


df['demographics'].value_counts()


# In[8]:


df['location'].value_counts()


# In[9]:


df['platform'].value_counts()


# In[10]:


df['profession'].value_counts()


# In[11]:


import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# In[12]:


df.sample(5)


# In[13]:


def myfunc(age):
    if age<2:
        return 'baby'
    elif age>2 and age<=10:
        return 'children'
    elif age>10 and age<=16:
        return 'teenage'
    elif age>16 and age<=30:
        return 'Young Adults'
    elif age>30 and age <=50:
        return 'middel aged Adults'
    elif age>50 and age<=70:
        return 'aged'
    else:
        return 'old'


# In[14]:


df['Age Category']=df['age'].apply(myfunc)
df.sample(5)


# In[15]:


avg_time_on_social_media=df.groupby(by=['platform']).agg({'time_spent':'mean'}).reset_index()
avg_time_on_social_media


# In[16]:


fig=px.bar(avg_time_on_social_media,x='platform',y='time_spent',color='time_spent',title='Avg. Time spent on Social media platforms')
fig.show(render='iframe')


# In[17]:


avg_time_genderwise=df.groupby(by=['gender']).agg({'time_spent':'mean'}).reset_index()
avg_time_genderwise


# In[18]:


fig=px.bar(avg_time_genderwise,x='gender',y='time_spent',color='time_spent',title='Time Spent on Social Media by Gender')
fig.show(render='iframe')


# In[19]:


avg_time_professionwise=df.groupby(by=['profession']).agg({'time_spent':'mean'}).reset_index()
avg_time_professionwise


# In[20]:


fig=px.bar(avg_time_professionwise,x='profession',y='time_spent',color='time_spent',title='Time Spent on Social Media by Profession')
fig.show(render='iframe')


# In[21]:


profession_SocialMedia_avgTime=df.groupby(by=['profession','platform']).agg({'time_spent':'mean'}).reset_index()
profession_SocialMedia_avgTime


# In[22]:


fig=px.bar(profession_SocialMedia_avgTime,x='profession',y='time_spent',color='platform',barmode='group',title='Average Time Spent on Social Media Platforms by Profession')
fig.show(render='iframe')


# In[23]:


df.groupby(by=['demographics']).agg({'time_spent':'mean'}).reset_index()


# In[24]:


fig=px.bar(df.groupby(by=['demographics']).agg({'time_spent':'mean'}).reset_index(),x='demographics',y='time_spent',title='Average Time Spent on Social Media by Demographics')
fig.show(render='iframe')


# In[25]:


df.groupby(by=['location']).agg({'time_spent':'mean'}).reset_index()


# In[26]:


fig=px.bar(df.groupby(by=['location']).agg({'time_spent':'mean'}).reset_index(),x='location',y='time_spent',title="Average Time Spent on Social Media by Location")
fig.show(render='iframe')


# In[27]:


df.groupby(by=['location','platform']).agg({'time_spent':'mean'}).reset_index()


# In[28]:


fig=px.bar(df.groupby(by=['location','platform']).agg({'time_spent':'mean'}).reset_index(),
           x='location',y='time_spent',color='platform',barmode='group',
           title="Average Time Spent on Social Media Platforms by Location")
fig.show(render='iframe')


# In[29]:


df.groupby(by=['Age Category','gender']).agg({'time_spent':'mean'}).reset_index()


# In[30]:


fig=px.bar(df.groupby(by=['Age Category','gender']).agg({'time_spent':'mean'}).reset_index(),
           x='Age Category',y='time_spent',color='gender',barmode='group',
          title="Average Time Spent on Social Media by Age Category and Gender")
fig.show(render='iframe')


# In[31]:


df.groupby(by=['Age Category']).agg({'time_spent':'mean'}).reset_index()


# In[32]:


fig=px.bar(df.groupby(by=['Age Category']).agg({'time_spent':'mean'}).reset_index(),
           x='Age Category',y='time_spent',barmode='group',
          title="Average Time Spent on Social Media by Age Category")
fig.show(render='iframe')


# In[33]:


df['time_spent'].mean()


# In[34]:


df[df['time_spent']>7]['gender'].value_counts().reset_index()


# In[35]:


fig=px.bar(df[df['time_spent']>7]['gender'].value_counts().reset_index(),
           x='gender',y='count',title="Count of Addicted Individuals by Gender")
fig.show(render='iframe')


# In[36]:


df[df['time_spent']>7]['Age Category'].value_counts().reset_index()


# In[37]:


fig=px.bar(df[df['time_spent']>7]['Age Category'].value_counts().reset_index(),
           x='Age Category',y='count',title="Count of Addicted Individuals by Age Category ")
fig.show(render='iframe')


# In[38]:


df[df['time_spent']>7]['profession'].value_counts().reset_index()


# In[39]:


fig=px.bar(df[df['time_spent']>7]['profession'].value_counts().reset_index(),
           x='profession',y='count',title="Count of Addicted Individuals by Profession")
fig.show(render='iframe')


# In[40]:


df[df['time_spent']>7]['demographics'].value_counts().reset_index()


# In[41]:


fig=px.bar(df[df['time_spent']>7]['demographics'].value_counts().reset_index(),
           x='demographics',y='count',title="Count of Addicted Individuals by demographics")
fig.show(render='iframe')


# In[42]:


df[df['time_spent']>7]['location'].value_counts().reset_index()


# In[43]:


fig=px.bar(df[df['time_spent']>7]['location'].value_counts().reset_index(),
           x='location',y='count',title="Count of Addicted Individuals by location")
fig.show(render='iframe')


# In[44]:


df[df['time_spent']>7]['platform'].value_counts().reset_index()


# In[45]:


fig=px.bar(df[df['time_spent']>7]['platform'].value_counts().reset_index(),
           x='platform',y='count',title="Most Addicted Platforms")
fig.show(render='iframe')

