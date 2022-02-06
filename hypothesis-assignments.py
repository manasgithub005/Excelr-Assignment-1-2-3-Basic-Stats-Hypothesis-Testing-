#!/usr/bin/env python
# coding: utf-8

# # Hypothesis Testing -Assignments

# In[39]:


import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import norm
from scipy.stats import chi2_contingency
from scipy.stats import chi2


# ###### 1.A F&B manager wants to determine whether there is any significant difference in the diameter of the cutlet between two units. A randomly selected sample of cutlets was collected from both units and measured? Analyze the data and draw inferences at 5% significance level. Please state the assumptions and tests that you carried out to check validity of the assumptions.
#      Minitab File : Cutlets.mtw  
# ![image.png](attachment:image.png)

# In[40]:


# Load the dataset
data=pd.read_csv('Cutlets.csv')
data.head()


# In[41]:


unitA=pd.Series(data.iloc[:,0]) #calling Series or DataFrame
unitA


# In[42]:


unitB=pd.Series(data.iloc[:,1])
unitB


# In[43]:


#Assuming Null hyposthesis as Ho: μ1 = μ2 (There is no difference in diameters of cutlets between two units).

#Thus Alternate hypothesis as Ha: μ1 ≠ μ2 (There is significant difference in diameters of cutlets between two units) 2 Sample 2 Tail test applicable


# In[44]:


# 2-sample 2-tail ttest:   stats.ttest_ind(array1,array2)     # ind -> independent samples
p_value=stats.ttest_ind(unitA,unitB)
p_value


# In[45]:


p_value[1]     # 2-tail probability 


# In[79]:


if p_value[1] <= 0.05:
	print('Dependent (reject H0)')
else:
	print('Independent (fail to reject H0)')


# ### =================================================================

# ###### 2.A hospital wants to determine whether there is any difference in the average Turn Around Time (TAT) of reports of the laboratories on their preferred list. They collected a random sample and recorded TAT for reports of 4 laboratories. TAT is defined as sample collected to report dispatch.
#    
#   Analyze the data and determine whether there is any difference in average TAT among the different laboratories at 5% significance level.
#  
# Minitab File: LabTAT.mtw
# ![image.png](attachment:image.png)

# In[47]:


# load the dataset
data=pd.read_csv('LabTAT.csv')
data.head()


# In[48]:


#Anova ftest statistics: Analysis of varaince between more than 2 samples or columns Assume Null Hypothesis Ho as No Varaince: All samples TAT population means are same

#Thus Alternate Hypothesis Ha as It has Variance: Atleast one sample TAT population mean is different


# In[49]:


# Anova ftest statistics: stats.f_oneway(column-1,column-2,column-3,column-4)
p_value=stats.f_oneway(data.iloc[:,0],data.iloc[:,1],data.iloc[:,2],data.iloc[:,3])
p_value


# In[50]:


p_value[1]  # comparing with α = 0.05


# In[51]:


# failed to reject H0


# ### ============================================================================

# ###### 3.      Sales of products in four different regions is tabulated for males and females. Find if male-female buyer rations are similar across regions.
# ![image.png](attachment:image.png)

# In[52]:


df= pd.read_csv('BuyerRatio.csv')
df.head()


# In[53]:


df_table=df.iloc[:,1:6]
df_table


# In[54]:


val=stats.chi2_contingency(df_table)
val


# In[55]:


type(val)


# In[56]:


no_of_rows=len(df_table.iloc[0:2,0])
no_of_columns=len(df_table.iloc[0,0:4])
degree_of_f=(no_of_rows-1)*(no_of_columns-1)
print('Degree of Freedom=',degree_of_f)


# In[57]:


Expected_value=val[3]
Expected_value


# In[58]:


from scipy.stats import chi2
chi_square=sum([(o-e)**2/e for o,e in zip(df_table.values,Expected_value)])
chi_square_statestic=chi_square[0]+chi_square[1]
chi_square_statestic


# In[59]:


critical_value=chi2.ppf(0.95,3)
critical_value


# In[60]:


if chi_square_statestic >= critical_value:
	print('Dependent (reject H0)')
else:
	print('Independent (fail to reject H0)')


# In[61]:


pvalue=1-chi2.cdf(chi_square_statestic,3)
pvalue


# In[62]:


if pvalue <= 0.05:
	print('Dependent (reject H0)')
else:
	print('Independent (fail to reject H0)')


# In[ ]:





# ###### 4.     TeleCall uses 4 centers around the globe to process customer order forms. They audit a certain %  of the customer order forms. Any error in order form renders it defective and has to be reworked before processing.  The manager wants to check whether the defective %  varies by centre. Please analyze the data at 5% significance level and help the manager draw appropriate inferences
# 
# Minitab File: CustomerOrderForm.mtw
#  
# ![image.png](attachment:image.png)

# In[63]:


#Assuming Null Hypothesis as Ho: Independence of categorical variables
#(customer order forms defective % does not varies by centre)
#Thus, Alternative hypothesis as Ha Dependence of categorical variables
#(customer order forms defective % varies by centre)


# In[67]:


custom = pd.read_csv('Costomer+OrderForm.csv')
custom


# In[68]:


print(custom['Phillippines'].value_counts(),custom['Indonesia'].value_counts(),custom['Malta'].value_counts(),custom['India'].value_counts())


# In[70]:


observed=([[271,267,269,280],[29,33,31,20]])
observed


# In[72]:


stat, p, dof, expected = chi2_contingency([[271,267,269,280],[29,33,31,20]])
stat


# In[73]:


p


# In[74]:


print('dof=%d' % dof)
print(expected)


# In[75]:


alpha = 0.05
prob=1-alpha
critical = chi2.ppf(prob, dof)
print('probability=%.3f, critical=%.3f, stat=%.3f' % (prob, critical, stat))
if abs(stat) >= critical:
	print('Dependent (reject H0),variables are related')
else:
	print('Independent (fail to reject H0), variables are not related')


# In[76]:


print('significance=%.3f, p=%.3f' % (alpha, p))
if p <= alpha:
	print('Dependent (reject H0)')
else:
	print('Independent (fail to reject H0)')


# In[77]:


# Inference: As (p_value = 0.2771) > (α = 0.05); Accept Null Hypthesis i.e.
#Independence of categorical variables Thus, customer order forms defective % does not varies by centre.


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




