
from scipy.io import loadmat
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

mat_dict=loadmat("98.mat")  #Thanks for CWRU Bearing Data Center
df=pd.DataFrame(mat_dict["X098_DE_time"])
plt.plot(range(0,1000),df[:1000])
plt.show(