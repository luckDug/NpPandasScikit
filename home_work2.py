#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# задание 1

import numpy as np
from matplotlib import pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7]
y = [3.5, 3.8, 4.2, 4.5, 5, 5.5, 7.]

plt.plot(x, y)
plt.show()


# In[3]:


plt.scatter(x, y)
plt.show()


# In[10]:


# задание 2

t = np.linspace(0, 10, num=51)
f = np.cos(t)

plt.title('График f(t)')
plt.xlabel('Значения t')
plt.ylabel('Значения f')
plt.plot(t, f, color='g')
plt.axis([0.5, 9.5, -2.5, 2.5])
plt.show()


# In[32]:


# задание 3
from pylab import rcParams

rcParams["figure.figsize"] = 8, 6

x = np.linspace(-3, 3, num=51)
y1 = x**2
y2 = 2 * x + 0.5 
y3 = -3 * x - 1.5 
y4 = np.sin(x)

fig, ax = plt.subplots(nrows=2, ncols=2)
fig.subplots_adjust(wspace=0.3, hspace=0.3)
ax1, ax2, ax3, ax4 = ax.flatten()


ax1.set_title('График y1')
ax2.set_title('График y2')
ax3.set_title('График y3')
ax4.set_title('График y4')

ax1.set_xlim([-5, 5])

ax1.plot(x, y1)
ax2.plot(x, y2)
ax3.plot(x, y3)
ax4.plot(x, y4)

plt.show()


# In[42]:


# задание 4

import pandas as pd

creditcard = pd.read_csv("creditcard.csv")
plt.style.use('fivethirtyeight')

class_count = creditcard['Class'].value_counts()
class_count.plot(kind="bar")


class_count = creditcard['Class'].value_counts()
class_count.plot(kind="bar", logy=True)


fig, ax = plt.subplots()
ax.hist(creditcard.loc[creditcard['Class'] == 1, 'V1'], bins=20, density = True, alpha=0.5, color="red")
ax.hist(creditcard.loc[creditcard['Class'] == 0, 'V1'], bins=20, density = True, alpha=0.5, color="lightgrey")
ax.set_xlabel('V1')

plt.legend(labels=["class 1", "class 0"])
plt.show()
