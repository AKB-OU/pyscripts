import numpy as np
import csv

#Misc. tool for WannierTools
#This program performs the following sequencial tasks.
#1. sums the conductivity tensor components of each band.
#2. rotate the obtained conductivity tensor around z axis.
#3. save the conductivity and resistivity tensors (inverse matrix of the conductivity tensor) to text files.
#2021.7.15 AKB

filenum=int(input("num. of files >"))
print(filenum)

filename=["k" for i in range(filenum)]
for i in range(filenum):
    filename[i]=input("file name >")
print(filename)

#rotation
rotangle=float(input("rotation angle around z (deg) >"))
print(rotangle)
rotmatrix=np.array([[np.cos(rotangle*np.pi/180),np.sin(rotangle*np.pi/180),0],[-np.sin(rotangle*np.pi/180),np.cos(rotangle*np.pi/180),0],[0,0,1]])
print(rotmatrix)
#rotation

sigmasum=np.loadtxt(filename[0], comments="#", usecols=range(2,11))
for i in range(sigmasum.shape[0]):
    for j in range(sigmasum.shape[1]):
        sigmasum[i][j]=0
print(sigmasum.shape)
#print(sigmasum)

for w in filename:
    btau=np.loadtxt(w, comments="#", usecols=[0])
    omegatau=np.loadtxt(w, comments="#", usecols=[1])
    sigma=np.loadtxt(w, comments="#", usecols=range(2,11))
    sigmasum+=sigma
#print(btau)
#print(omegatau)
#print(sigma)
#print(sigmasum)

with open("stor_r.out", "w", encoding="utf-8") as output:
    output.write("#resistivity tensor\n")
    output.write("#btau omegatau xx xy xz yx yy yz zx zy zz\n")
with open("stor_s.out", "w", encoding="utf-8") as output:
    output.write("#conductivity tensor\n")
    output.write("#btau omegatau xx xy xz yx yy yz zx zy zz\n")
sigmaseg=[0]*sigmasum.shape[1]
#print(sigmaseg)
for i in range(sigmasum.shape[0]):
    sigmaseg=sigmasum[i]
    sigma_3_3=sigmaseg.reshape(3,3)
    #print(sigma_3_3)

    #rotation
    sigma_3_3=np.dot(rotmatrix,np.dot(sigma_3_3,rotmatrix.T))
    #rotation

    sigmaseg=sigma_3_3.reshape(9)
    result=[btau[i], omegatau[i], sigmaseg[0], sigmaseg[1], sigmaseg[2], sigmaseg[3], sigmaseg[4], sigmaseg[5], sigmaseg[6], sigmaseg[7], sigmaseg[8] ]
    with open("stor_s.out", "a", encoding="utf-8") as output:
        csv.writer(output, delimiter="\t").writerow(result)
    
    rho_3_3=np.linalg.inv(sigma_3_3)
    print(rho_3_3)
    
    rhoseg=rho_3_3.reshape(9)
    #print(rhoseg)
    result=[btau[i], omegatau[i], rhoseg[0], rhoseg[1], rhoseg[2], rhoseg[3], rhoseg[4], rhoseg[5], rhoseg[6], rhoseg[7], rhoseg[8] ]
    #print(result)
    with open("stor_r.out", "a", encoding="utf-8") as output:
        csv.writer(output, delimiter="\t").writerow(result)
    
    
