#!/usr/bin/env python
# coding: utf-8

# In[1]:


def diff21(n):
    n = abs(21 - abs(n))
    return n


# In[3]:


assert(diff21(19) == 2), "The return value of diff21 is incorrect for this assertion"
assert(diff21(10) == 11 ), "The return value of diff21 is incorrect for this assertion"
assert(diff21(21) == 0), "The return value of diff21 is incorrect for this assertion"


# In[4]:


def sum_double(a,b):
    if a==b:
        return (a+b)*2
    else:
        return (a+b)
    return 0


# In[6]:


assert(sum_double(1,2) == 3), "The return value of sum_double is incorrect for this assertion"
assert(sum_double(2,2) == 8), "The return value of sum_double is incorrect for this assertion"


# In[20]:


def count_even(arr):
    out = len([x for x in arr if x%2 == 0])
    return out


# In[21]:


count_even([2,1,3,4])


# In[22]:


assert(count_even([2, 1, 2, 3, 4])) == 3

