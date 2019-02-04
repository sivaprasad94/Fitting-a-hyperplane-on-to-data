#!/usr/bin/env python
# coding: utf-8

# In[123]:


import pandas as pd
# Importing plotly modules
import  plotly.offline  as ofl
import plotly.graph_objs as go

# Importing numpy to create data
import numpy as np

# Important to initialize notebook mode to visualize plots within notebook
ofl.init_notebook_mode()

import numpy as np
import scipy.linalg
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Import plotly package
import plotly
import plotly.graph_objs as go

# Check ploltly version
plotly.__version__

# To communicate with Plotly's server, sign in with credentials file
import plotly.plotly as py


# In[124]:


df = pd.read_csv('https://raw.githubusercontent.com/colaberry/DSin100days/master/data/Advertising.csv')


# In[125]:


df.head()


# In[141]:



trace1 = go.Scatter3d(
   x=df['Radio'],
   y=df['TV'],
   z=df['Sales'],
   mode='markers',
   marker=dict(
       color='black',
       size=6,
       symbol='circle',
       line=dict(
           color='rgb(254, 204, 204)',
           width=1
       ),
       opacity=0.9
   )
)

x1 = df['Radio'].values
y1 = df['TV'].values

X,Y = np.meshgrid(np.linspace(0, 50, 50), np.linspace(0, 300, 300))
Z = 0.18799423*X + 0.04575482*Y + 2.9210999124051398

trace2 = go.Surface(z=Z, x=X, y=Y, colorscale='RdBu', opacity=0.8)



# Defining data 
data = [trace1,trace2]

# Defining layout
layout = go.Layout(
   margin=dict(
       l=0,
       r=0,
       b=0,
       t=0
   )
)

# Creating Figure object
fig = go.Figure(data=data, layout=layout)

# Visualizing the plot
ofl.iplot(fig, filename='TV vs Radio vs Sales')

