#!/usr/bin/env python
# coding: utf-8

# ## Surfacr Plots |Data visualisation
# Surface plots are used to
# - Visualise loss function in Machine learning and deep learning
# - visualise state or state value function in reinforcement learning

# In[20]:


import matplotlib.pyplot as plt
import numpy as np


# In[33]:


# a = np.array([1,2,3])
# b = np.array([4,5,6,7])
a = np.arange(-1,1,0.02)
b=a
a,b = np.meshgrid(a,b)
print(a)
print(b)


# In[34]:


from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
axes = fig.gca(projection='3d')
axes.plot_surface(a,b,a**2+b**2,cmap="rainbow")# color difference depicts high and low value 
plt.show()


# ## contour plot

# In[35]:


fig = plt.figure()
axes = fig.gca(projection='3d')
axes.contour(a,b,a**2+b**2,cmap = 'rainbow')
plt.title("contour plot")
plt.show()


# In[ ]:




