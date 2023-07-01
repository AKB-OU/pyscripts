import numpy as np
import csv

filenum=int(input("num. of files > "))
theta_max=int(input("theta_max > "))
theta_del=int(input("theta_del > "))

with open("amc.out", "w", encoding="utf-8") as output:
    output.write("#conductivity tensor\n")
    output.write("#theta xx yx zz\n")
    
corename=["k" for i in range(filenum)]
for i in range(filenum):
    corename[i]=input("input corename > ")
    
for theta in range(0, theta_max, theta_del):

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
    #sigmaseg_zero=[0]*sigmasum.shape[1]
    
    sigmaseg=sigmasum[sigmasum.shape[0]-1]
    #sigmaseg_zero=sigmasum[0]
    
    result=[theta, sigmaseg[0], sigmaseg[3], sigmaseg[8]]
    
    print(result)
    with open("amc.out", "a", encoding="utf-8") as output:
        csv.writer(output, delimiter="\t").writerow(result)
