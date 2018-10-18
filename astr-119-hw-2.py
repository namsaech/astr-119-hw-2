
# coding: utf-8

# In[ ]:


#Natalie Saechao, 
#October 18, 2018
#HW 2
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 2*np.pi, 0.00628) #(2*pi)/1000 is 0.00628
y = 5.5*np.cos(2*x) + 5.5
v = 0.02*np.exp(x)
w = 0.25*x**2 + 0.1*np.sin(10*x)
plt.plot(x, y, 'y')  
plt.plot(x, v, 'v') 
plt.plot(x, w, 'w', color="red")


plt.ylim([-1,10])
#plt.plot(x,y)
plt.xlabel('Time in Astr-119')
plt.ylabel('Measure of Awesomeness')
plt.show()

