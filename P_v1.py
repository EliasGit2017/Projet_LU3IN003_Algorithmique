""" Tâche A""" 
"""temps d'éxecution CPU"""
#t=[16.09375,6.90625,0.125,28.046875,27.09375,293.328125]
##Inst_0000012_56.adn est la première instance dont la résolution prend plus d'une minute pour la tâche A
#import matplotlib.pyplot as plt
#
#plt.plot(["10_7","10_8","10_44","12_13","12_32","12_56"],t)
#plt.xlabel("instances")
#plt.ylabel("temps d'éxecution en secondes")
#plt.title("Tâche A",color="blue")
#plt.savefig("Tâche_A_temps_exec.png",dpi=1500,bbox_inches="tight") 2066.3
#t=[1641,1819,1865,1749.8,2000.8,2025.6, 2066.3]
##Inst_0000012_56.adn est la première instance dont la résolution prend plus d'une minute pour la tâche A
#import matplotlib.pyplot as plt
#
#plt.plot(["10_7","10_8","10_44","12_13","12_32","12_56"],t)
#plt.xlabel("tailles des instances")
#plt.ylabel("Consommation mémoire en Kbits")
#plt.title("Tâche A",color="blue")
#plt.savefig("TA2.png",dpi=1500,bbox_inches="tight")

#t=[0,0,0,0,0,0,0.015625,0.03125,0.7760416666666666,3.515625,15.359375,36.70703125,108.36458333333333, 241.546875,404.65625,]
#t=[0,0,0,0,0,0,0,0.03125,0.171875,0.75,2.890625,7.6875,19.625,53.671875,78.375,184.890625,334.65625]
#
#import matplotlib.pyplot as plt
#
#plt.plot([10,12,13,14,15,20,50,100,500,1000,2000,3000,5000,8000,10000,15000,20000],t)
#plt.xlabel("tailles des instances")
#plt.ylabel("Temps d'éxecution en secondes")
#plt.title("Tâche B",color="blue")
#plt.savefig("TB.png",dpi=1500,bbox_inches="tight")
#import matplotlib.patches as mpatches
#import matplotlib.pyplot as plt
#
#blue_patch=mpatches.Patch(color='blue', label='Tâche B')
#red_patch = mpatches.Patch(color='red', label='Tâche A')
#plt.legend(handles=[red_patch,blue_patch])
#
#
#t2=[7.708333333333333,27.5703125,293.328125]
#t=[0,0,0,0,0,0,0,0.03125,0.171875,0.75,2.890625,7.6875,19.625,53.671875,78.375,184.890625,334.65625]
#plt.plot([10,12,13,14,15,20,50,100,500,1000,2000,3000,5000,8000,10000,15000,20000],t,label='Tâche B')
#plt.plot([10,12,13],t2,'r',label='Tâche A')
#plt.xlabel("tailles des instances")
#plt.ylabel("Temps d'éxecution en secondes")
#plt.title("Tâches B et A",color="blue")
#plt.savefig("TB22.png",dpi=1500,bbox_inches="tight")


import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np



green_patch=mpatches.Patch(color='red', label='Tâche A')
blue_patch=mpatches.Patch(color='blue', label='Tâche B')
red_patch = mpatches.Patch(color='green', label='Tâche C')
purple_patch=mpatches.Patch(color='purple',label='Tâche D')

plt.legend(handles=[red_patch,blue_patch,purple_patch,green_patch])
t3=[7.708333333333333,27.5703125,293.328125]
t2=[0,0,0,0,0,0,0,0.03125,0.171875,0.75,2.890625,7.6875,19.625,53.671875,78.375,184.890625]


t4=[0,0,0,0,0,0,0.015625,0.03125,1.0,4.8125,21.375,54.25,168.1875,425.703125,644.421875]
t=[0,0,0,0,0,0,0.015625,0.015625,0.515625,2.53125,10.171875,26.0625,75.34375,195.203125,305.71875,649.578125]
plt.plot([10,12,13,14,15,20,50,100,500,1000,2000,3000,5000,8000,10000],t4,'purple',label='Tâche D')
plt.plot([10,12,13,14,15,20,50,100,500,1000,2000,3000,5000,8000,10000,15000],t2,'blue',label='Tâche B')
plt.plot([10,12,13],t3,'r',label='Tâche A')
plt.plot([10,12,13,14,15,20,50,100,500,1000,2000,3000,5000,8000,10000,15000],t,'green',label='Tâche C')
plt.xlabel("tailles des instances")
plt.ylabel("Temps d'éxecution en secondes")
plt.title("Tâches A,B,C et D",color="blue")
plt.savefig("TD2.png",dpi=1500,bbox_inches="tight")

