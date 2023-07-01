import numpy as np
rotangle=int(input("rotangle >"))
rhotest = [[3.5,0.5,0],[0.5,3.5,0],[0,0,10]]
print(rhotest)
rot = np.array([[np.cos(rotangle*np.pi/180),np.sin(rotangle*np.pi/180),0],[-np.sin(rotangle*np.pi/180),np.cos(rotangle*np.pi/180),0],[0,0,1]])
resultmat=np.dot(rot,np.dot(rhotest,rot.T))
print(resultmat)
