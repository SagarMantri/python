#!/usr/bin/env python
# coding: utf-8

# # This notebook is for demonstrating the F string 

# In[1]:


name=input("Please input the name")
age=input("please input the age")
location=input("Please input the location")
team=input('Enter the team')
profile=input("Input your profile")

print('\nBelow is the Format String example\n')
print(f""" Hi {name}, on this occassion that you are of age {age} and your address is {location}""")


# 

# In[3]:


print(f"""This is {name}, having an age of {age} and from {team} and is amazing {profile} 
from the beautiful location {location}""")

