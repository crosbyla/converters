# coding: utf-8
get_ipython().system('ls -F --color ')
import xyz2cifnp as xyz
xyz.convert2cif('STO-110-Surf-O.xyz')
import numpy as np
date = np.load('STO-110.xyz',skiprows=2)
date = np.load('STO-110.xyz')
date = np.loadtxt('STO-110.xyz')
date = np.loadtxt('STO-110.xyz',skiprows=2)
date = np.loadtxt('STO-110.xyz',skiprows=3)
data = np.loadtxt('STO-110.xyz',skiprows=3)
data = np.loadtxt('STO-110.xyz',skiprows=3)
data = np.loadtxt('STO-110.xyz')
get_ipython().system('cat STO-110.xyz')
data = np.loadtxt('STO-110.xyz',skiprows=2)
data = np.loadtxt('STO-110.xyz',skiprows=2, usecols=(1,))
data
data = np.loadtxt('STO-110.xyz',skiprows=2, usecols=(1,2,3))
data
data1 = np.loadtxt('STO-110.xyz',skiprows=2, dtype={'s1, f6, f6, f6'})
data1 = np.loadtxt('STO-110.xyz',skiprows=2, dtype='s1, f6, f6, f6')
data1 = np.loadtxt('STO-110.xyz',skiprows=2, dtype=['s2', float, float, float])
data1 = np.loadtxt('STO-110.xyz',skiprows=2, dtype==[('atom','s2'),('x', float),('y', float),('z', float)])
data1 = np.loadtxt('STO-110.xyz',skiprows=2, dtype=[('atom','s2'),('x', float),('y', float),('z', float)])
data1 = np.loadtxt('STO-110.xyz',skiprows=2, dtype=[('atom','S2'),('x', float),('y', float),('z', float)])
data1
data
data1[1:]
data1[:,1:]
data1[:,1]
data1.shape
data.shape
data.T
data.T[0]
data.T[0]*0.707
trans = array([0.707, -0.707, 0],[.707, .707, 0], [0, 0, 1])
trans = np.array([0.707, -0.707, 0],[.707, .707, 0], [0, 0, 1])
np.array([[1]])
np.array([[1,2]])
trans = np.array([[0.707, -0.707, 0],[.707, .707, 0], [0, 0, 1]])
trans
data * trans
np.dot(array,trans)
np.dot(data,trans)
data
data[0]
data[:][0]
data[0][0]
:ref:`sort-words-solution`
data[0][:]
data[0,:]
data[0,1]
data[:,1]
data[:,0]
max(data[:,0])
range(data[:,0])
np.range(data[:,0])
np.xrange(data[:,0])
np.max(data[:,0])
np.max(data[:,0]) - np.min(data[:,0])
x = data[:,0]
y = data[:,1]
z = data[:,2]
xlim = np.max(x) - np.min(x)
ylim = np.max(y) - np.min(y)
zlim = np.max(z) - np.min(z)
xlim
ylim
zlim
x /= xlim
z
x
y /= ylim
z /= zlim
data
data = np.dot(data,trans)
data
np.savetxt('testout.txt', data, fmt='%1.6f')
get_ipython().system('ls -F --color ')
get_ipython().system('cat testout.txt')
elem = np.loadtxt('STO-110.xyz',skiprows=2, usecols=(0))
elem = np.loadtxt('STO-110.xyz',skiprows=2, usecols=(0,))
elem = np.loadtxt('STO-110.xyz',skiprows=2, usecols=(0,),dtype='S2')
elem
data
np.savetxt('elemout2.txt', (elem,data), fmt=%s '%1.6f')
np.savetxt('elemout2.txt', (elem,data), fmt='%s %1.6f')
elem[,0]
elem[:,0]
elem[:]
elem[0]
