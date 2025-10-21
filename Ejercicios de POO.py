"""
Ejercicios de POO
"""

#!/usr/bin/env python
# coding: utf-8

# In[4]:


import sys
print(sys.version)


# In[6]:


import datetime
dir(datetime)
#help(datetime)


# In[7]:


class product():
    def __init__(self):
        pass
producto=product()
dir(producto)


# In[10]:


def stock_info(company, country, price):
    pass
dir(stock_info.__code__.co_varnames)


# In[12]:


help(sum)


# In[13]:


def stick(dato1, dato2):
    print(str(dato1)+str(dato2))

stick(1,2)


# In[30]:


def display_info(company, **kwargs):
    print(company)
    if "price" in kwargs:
        print (kwargs)
    pass

display_info(company="juana", price=100)


# In[31]:


class Vehicle():
    pass


# In[32]:


class phone():
    pass
print(type(phone))


# In[34]:


class vehicle():
    """this is a  vehicle class"""
print(vehicle.__name__)


# In[37]:


class Container():
    """ this is a container class"""

print(Container.__dict__.keys())


# In[39]:


class Container():
    """ this is a container class"""

print(Container.__module__)


# In[ ]:




