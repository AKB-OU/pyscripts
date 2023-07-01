import numpy as np
import csv

string_var=input("var (phi or theta)? > ")
int_start=int(input("start? > "))
int_end=int(input("end? > "))
int_interv=int(input("interv? > "))

with open("dhva_angle.out", "w", encoding="utf-8") as output:
    output.write("#angular dependence of dhva \n")
    output.write("#Var [deg], Freq [T], SdevFreq [T], M [m_e], SdevM [m_e], X [0...1], SdevX, Y, SdevY, Z, SdevZ, Number of copies \n")

if string_var == "phi":
    string_filepath=input("filepath > ")
    int_nksc=int(input("nksc > "))
    int_nsc=int(input("nsc > "))
    int_theta=int(input("theta > "))
    float_maxkdiff=float(input("maxkdiff > "))
    float_maxfreqdiff=float(input("maxfreqdiff > "))
    int_minimumfreq=int(input("minimumfreq > "))
    int_ip=int(input("ip > "))

    for int_phi in range(int_start, int_end+int_interv, int_interv):
        inputfilename=string_filepath+"."+str(int_nksc)+"_"+str(int_nsc)+"_"+str('{:.1f}'.format(int_phi))+"_"+str('{:.1f}'.format(int_theta))+"_"+str('{:.3f}'.format(float_maxkdiff))+"_"+str('{:.3f}'.format(float_maxfreqdiff))+"_"+str(int_minimumfreq)+"_"+str(int_ip)+".out"

        result=np.loadtxt(inputfilename, comments="#")
        if len(result) > 0:
            print(result)
            with open("dhva_angle.out", "a", encoding="utf-8") as output:
                if result.ndim > 1:
                    csv.writer(output, delimiter="\t").writerows(np.insert(result, 0, int_phi, axis=1))
                else:
                    csv.writer(output, delimiter="\t").writerow(np.insert(result, 0, int_phi))

elif string_var == "theta":
    string_filepath=input("filepath > ")
    int_nksc=int(input("nksc > "))
    int_nsc=int(input("nsc > "))
    int_phi=int(input("phi > "))
    float_maxkdiff=float(input("maxkdiff > "))
    float_maxfreqdiff=float(input("maxfreqdiff > "))
    int_minimumfreq=int(input("minimumfreq > "))
    int_ip=int(input("ip > "))

    for int_theta in range(int_start, int_end+int_interv, int_interv):
        inputfilename=string_filepath+"."+str(int_nksc)+"_"+str(int_nsc)+"_"+str('{:.1f}'.format(int_phi))+"_"+str('{:.1f}'.format(int_theta))+"_"+str('{:.3f}'.format(float_maxkdiff))+"_"+str('{:.3f}'.format(float_maxfreqdiff))+"_"+str(int_minimumfreq)+"_"+str(int_ip)+".out"

        result=np.loadtxt(inputfilename, comments="#")
        if len(result) > 0:
            print(result)
            with open("dhva_angle.out", "a", encoding="utf-8") as output:
                if result.ndim > 1:
                    csv.writer(output, delimiter="\t").writerows(np.insert(result, 0, int_theta, axis=1))
                else:
                    csv.writer(output, delimiter="\t").writerow(np.insert(result, 0, int_theta))


    
        
