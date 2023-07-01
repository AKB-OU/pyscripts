import numpy as np
import csv

filenum=int(input("num. of files > "))
theta_init=int(input("theta_init > "))
theta_max=int(input("theta_max > "))
theta_del=int(input("theta_del > "))

with open("amr_r.out", "w", encoding="utf-8") as output:
    output.write("#resistivity tensor\n")
    output.write("#theta xx yx zz xx_norm yx_norm zz_norm \n")
    
with open("amr_s.out", "w", encoding="utf-8") as output:
    output.write("#conductivity tensor\n")
    output.write("#theta xx yx zz xx_norm yx_norm zz_norm \n")
    
corename=["k" for i in range(filenum)]
for i in range(filenum):
    corename[i]=input("input corename > ")

#rotation
rotangle=float(input("rotation angle around z (deg) >"))
print(rotangle)
rotmatrix=np.array([[np.cos(rotangle*np.pi/180),np.sin(rotangle*np.pi/180),0],[-np.sin(rotangle*np.pi/180),np.cos(rotangle*np.pi/180),0],[0,0,1]])
print(rotmatrix)
#rotation
    
for theta in range(theta_init, theta_max, theta_del):

    filename=["k" for i in range(filenum)]
    for i in range(filenum):
        filename[i]=corename[i]+"_"+str(theta)+"deg.dat"
    print(filename)
        
    sigmasum=np.loadtxt(filename[0], comments="#", usecols=range(2,11))
    for i in range(sigmasum.shape[0]):
        for j in range(sigmasum.shape[1]):
            sigmasum[i][j]=0
                
    for w in filename:
        #btau=np.loadtxt(w, comments="#", usecols=[0])
        #omegatau=np.loadtxt(w, comments="#", usecols=[1])
        sigma=np.loadtxt(w, comments="#", usecols=range(2,11))
        sigmasum+=sigma
        
    sigmaseg=[0]*sigmasum.shape[1]
    sigmaseg_zero=[0]*sigmasum.shape[1]
    
    #sigmaseg=sigmasum[sigmasum.shape[0]-1]
    sigmaseg=sigmasum[50]#!!!manual point set!!!
    sigmaseg_zero=sigmasum[0]
    
    sigma_3_3=sigmaseg.reshape(3,3)
    sigma_3_3_zero=sigmaseg_zero.reshape(3,3)

    #rotation
    sigma_3_3=np.dot(rotmatrix,np.dot(sigma_3_3,rotmatrix.T))
    sigma_3_3_zero=np.dot(rotmatrix,np.dot(sigma_3_3_zero,rotmatrix.T))
    #rotation
    
    sigmaseg=sigma_3_3.reshape(9)
    sigmaseg_zero=sigma_3_3_zero.reshape(9)

    result=[theta, sigmaseg[0], sigmaseg[3], sigmaseg[8], (sigmaseg[0]-sigmaseg_zero[0])/sigmaseg_zero[0], (sigmaseg[3]-sigmaseg_zero[3])/sigmaseg_zero[3], (sigmaseg[8]-sigmaseg_zero[8])/sigmaseg_zero[8]]

    with open("amr_s.out", "a", encoding="utf-8") as output:
        csv.writer(output, delimiter="\t").writerow(result)
    
    rho_3_3=np.linalg.inv(sigma_3_3)
    rho_3_3_zero=np.linalg.inv(sigma_3_3_zero)
    
    print(rho_3_3)
    
    rhoseg=rho_3_3.reshape(9)
    rhoseg_zero=rho_3_3_zero.reshape(9)
    
    #print(rhoseg)
    
    result=[theta, rhoseg[0], rhoseg[3], rhoseg[8], (rhoseg[0]-rhoseg_zero[0])/rhoseg_zero[0], (rhoseg[3]-rhoseg_zero[3])/rhoseg_zero[3], (rhoseg[8]-rhoseg_zero[8])/rhoseg_zero[8]]
    
    #print(result)
    with open("amr_r.out", "a", encoding="utf-8") as output:
        csv.writer(output, delimiter="\t").writerow(result)
