#!/usr/bin/env python
# coding: utf-8

# In[40]:


import numpy as np
import pandas as pd
from scipy import stats
import seaborn as sns
from statsmodels.graphics.gofplots import qqplot
import statsmodels.api as sm
import matplotlib.pyplot as plt
from scipy.stats import f_oneway
col_list = ["NEWEdImpt","Age"]
data = pd.read_csv("C:/Users/HP/Desktop/survey_results_public.csv",usecols=col_list)
print(data.shape)


# In[41]:


data.dropna(inplace=True)
print(data.shape)


# In[42]:


data['Age'].min()


# In[43]:


#histogram for normality check 
sns.distplot(data['Age'])


# In[44]:


qqplot(data['Age'], line='r')
plt.show()


# In[45]:


sns.boxplot(x=data['Age'])
#too many outliers


# In[46]:


#removing outliers
Q1 = data.quantile(0.25)
Q3 = data.quantile(0.75)
IQR = Q3 - Q1
data_out = data[~((data < (Q1 - 1.5 * IQR)) |(data > (Q3 + 1.5 * IQR))).any(axis=1)]
data_out.shape


# In[47]:


#boxplot after removing outliers
sns.boxplot(x=data_out['Age'])


# In[48]:


#Histogram after removing outliers 
sns.distplot(data_out['Age'])


# In[63]:


#Square root transformation
data_out['Age']=data_out['Age']**(.25)
sns.distplot(data_out['Age'])


# In[64]:


data_out['NEWEdImpt'].value_counts()


# In[66]:


#Groups within 

fairly_important = data_out['NEWEdImpt'].str.contains('Fairly important', na = False)
comp_fairly_important = data_out[fairly_important]['Age']

somehow_important = data_out['NEWEdImpt'].str.contains('Somehow important', na = False)
comp_somehow_important = data_out[somehow_important]['Age']

very_important = data_out['NEWEdImpt'].str.contains('Very important', na = False)
comp_very_important = data_out[very_important]['Age']

not_necessary = data_out['NEWEdImpt'].str.contains('not necessary', na = False)
comp_not_necessary = data_out[not_necessary]['Age']

critically_important = data_out['NEWEdImpt'].str.contains('critically important', na = False)
comp_critically_important = data_out[critically_important]['Age']

comp_fairly_important = comp_fairly_important[comp_fairly_important > 0]
comp_somehow_important = comp_somehow_important[comp_somehow_important > 0]
comp_very_important = comp_very_important[comp_very_important>0]
comp_not_necessary = comp_not_necessary[comp_not_necessary > 0]
comp_critically_important = comp_critically_important[comp_critically_important > 0]


# In[54]:


sns.boxplot(x = comp_fairly_important)


# In[67]:


sns.boxplot(x = comp_somehow_important)


# In[56]:


sns.boxplot(x = comp_very_important)


# In[58]:


sns.boxplot(x = comp_not_necessary)


# In[68]:


sns.boxplot(x = comp_critically_important)


# In[18]:


#ANOVA assumes that the variances of the populations that the samples come from are equal.
#The variance of job satisfaction in each group can be seen by the length of each box plot. 
#The wider the box, the higher the variance.
#box widths are almost same
#that is variances are almost same


# In[69]:


print(f_oneway(comp_fairly_important, comp_very_important, comp_not_necessary))


# In[ ]:




