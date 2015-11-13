# coding: utf-8
import numpy as np
data = np.loadtxt('STO-110.xyz',skiprows=2, usecols=(1,2,3))
trans = np.array([[0.707, -0.707, 0],[.707, .707, 0], [0, 0, 1]])
data = np.dot(data,trans)
data
np.savetxt('testout.txt', data, fmt='%1.6f')
elem = np.loadtxt('STO-110.xyz',skiprows=2, usecols=(0,),dtype='S2')
elem
data
np.savetxt('elemout2.txt', (elem,data), fmt='%s %1.6f')
elem[0]import numpy as np
data = np.loadtxt('STO-110.xyz',skiprows=2, usecols=(1,2,3))
trans = np.array([[0.707, -0.707, 0],[.707, .707, 0], [0, 0, 1]])
data = np.dot(data,trans)
data
np.savetxt('testout.txt', data, fmt='%1.6f')
elem = np.loadtxt('STO-110.xyz',skiprows=2, usecols=(0,),dtype='S2')
elem
data
np.savetxt('elemout2.txt', (elem,data), fmt='%s %1.6f')
elem[0]
data
elem
elem.shape
data.shape
a = elem + data
np.rowstack()
np.colstack()
np.column_stack()
np.row_stack()
np.row_stack(elem,data)
np.row_stack((elem,data))
np.v_stack((elem,data))
np.row_stack((elem,data))
np.row_stack((data,elem))
data.shape
data.T
np.row_stack(elem,data.T)
np.row_stack((data,elem))
np.row_stack((elem,data.T))
_.shape
testj = np.row_stack((elem,data.T))
np.savetxt('test.txt', testj, fmt='%s %1.6f %1.6f %1.6f')
np.savetxt('test.txt', testj, fmt='%s')
get_ipython().system('cat test.txt')
np.savetxt('test.txt', (elem, data), fmt='%s')
np.savetxt('test.txt', (elem, data.T), fmt='%s')
get_ipython().system('cat test.txt')
np.savetxt('test.txt', (elem, data.T), fmt='%s %f')
np.savetxt('test.txt', (elem, data.T), fmt='%s %f %f %f')
np.savetxt('test.txt', (elem.T, data), fmt='%s %f %f %f')
np.savetxt('test.txt', (elem, data.T), fmt='%s %f %f %f')
np.savetxt('test.txt', (elem, data.T))
(elem, data)
(elem, data.T)
data
np.invert(trans)
trans
np.linalg.inv(trans)
itrans = np.linalg.inv(trans)
np.dot(data,trans)
elem,data
f = np.zeros((38,4),dtype=('|S2,float64'))
f
f = np.zeros((38,),dtype=('|S2,float64, float64, float64'))
f
f[0]
f[,0]
f[:,0]
f[:,]
f[,:]
f.shape
np.vstack(data, elem)
np.vstack((data, elem))
np.vstack((data, elem.T))
np.vstack((data.T, elem))
_.T
np.vstack((data, elem.T))
