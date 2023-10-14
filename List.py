#!/usr/bin/env python
# coding: utf-8

# In[1]:


## Sequence Data types


# In[2]:


todo_list=['volvo','ashok leyland','tata']
todo_list


# # appending the list

# In[4]:


todo_list.append('Mercedes')


# In[5]:


todo_list


# In[6]:


new_list=['maruti','Honda','Hyundai']


# ### Creating new List and extending the todo_list with the new_list)

# In[7]:


todo_list.extend(new_list)


# In[8]:


todo_list


# ## updating index 2 in todo_list

# In[9]:


todo_list[2]='Kia'


# In[10]:


todo_list


# In[11]:


todo_list.insert(2,'Tata')


# In[12]:


todo_list


# In[15]:


print(todo_list)

