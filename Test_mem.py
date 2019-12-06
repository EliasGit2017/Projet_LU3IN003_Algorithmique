# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 18:44:09 2019

@author: azwbd
"""

@profile(precision=4)
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a

if __name__ == '__main__':
    my_func()
    
    
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 15:33:46 2019

--------Infini : ------------------------------------------------------------------------
math.inf
Un flottant positif infini. (Pour un infini négatif, utilisez -math.inf.) Équivalent au résultat de float('inf').
Nouveau dans la version 3.5.
    
         import math
         test=math.inf
         
         ou 
         
         test=float("inf")
       
         from decimal import Decimal
         pos_inf = Decimal('Infinity')
         neg_inf = Decimal('-Infinity')
-----------------------------------------------------------------------------------------
@author: Elias Bendjaballah 3700088
"""
import math
import time

import psutil
import os

def memory_usage_psutil():
    """retourne la quantité de mémoire utilisée par le programme"""
    process=psutil.Process(os.getpid())
    mem=process.memory_info()[0]/float(2**20)
    return mem 
    
"""Ouverture du fichier"""
lec=open("C:/Users/azwbd/OneDrive/Documents/3I003/Projet/Instances_genome/Inst_0000010_7.adn","r")
"""lecture des 2 premieres lignes"""
lenx=int(lec.readline())
leny=int(lec.readline())
"""stockage des sequences sous forme de tableau"""
x=lec.readline().split()
y=lec.readline().split()
lec.close()

def DIST_NAIF(x,y):
    """Entree : x et y deux mots
    Sortie : d(X,Y) la distance d'edition de x a y """
    return DIST_NAIF_REC(x,y,0,0,0,math.inf)

def substitution(a,b):
    """Entrée : a et b deux caractères appartennant à l'alphabet considéré ('A','T','C','G')
    Sortie : la valeur du coût de la subtitution de b à a (on remplace a par b)"""
    A={'A','T'}
    B={'G','C'}
    if (a != b):
        if ((a in A) and (b in A)) or ((a in B) and (b in B)):
            return 3
        else:
            return 4
    return 0

def substitution2(a,b):
    """Entrée : a et b deux caractères appartennant à l'alphabet considéré ('A','T','C','G')
    Sortie : la nouvelle valeur de l'élément substitué"""
    return a

def DIST_NAIF_REC(x,y,i,j,c,dist):
    """Realise l'exploration complete des alignements possibles pour un couple (x,y) donné
    et retourne le coût du meilleur alignement.
    Entree : x et y 2 mots de longueurs respectives lenx et leny
                i dans [0,n] et j dans [0,m] deux indices sur x et y
                c le cout d'un alignement
                dist le cout du meilleur alignement de (x,y) connu avant cet appel
     Sortie : dist le cout du meilleur alignement de (x,y) connu après cet appel"""
    if (i == lenx) and (j == leny):
        if(c < dist):
            dist=c
    else:
        if(i < lenx) and (j < leny):
            dist=DIST_NAIF_REC(x,y,i+1,j+1,c+substitution(x[i],y[j]),dist)
        if(i < lenx):
            dist=DIST_NAIF_REC(x,y,i+1,j,c+2,dist)
        if(j < leny):
            dist=DIST_NAIF_REC(x,y,i,j+1,c+2,dist)
    return dist


"---------------------------------------------------------------------------------"
#t1=time.process_time()
#print("Distance d'edition 1 : ",DIST_NAIF(x,y))
#t2=time.process_time()
#print("Temps d'execution = ",t2-t1)

"----------------------------------------------------------------------------------"

"""----------------------------- Tâche B -------------------------------------------------"""

def DIST_1(x,y):
    T=[[0]*(leny+1) for i in range (lenx+1)]
    for i in range(lenx+1):
        T[i][0]=i*2
    for j in range(1,leny+1):
        T[0][j]=j*2
    for i in range(1,lenx+1):
        for j in range(1,leny+1):
            T[i][j]=min(T[i-1][j]+2,T[i][j-1]+2,T[i-1][j-1]+substitution(x[i-1],y[j-1]))
    for a in T:
        print(a)
    return (T[lenx][leny],T)


def DIST_T(x,y):
    T=[[0]*(leny+1) for i in range (lenx+1)]
    for i in range(lenx+1):
        T[i][0]=i*2
    for j in range(1,leny+1):
        T[0][j]=j*2
    for i in range(1,lenx+1):
        for j in range(1,leny+1):
            T[i][j]=min(T[i-1][j]+2,T[i][j-1]+2,T[i-1][j-1]+substitution(x[i-1],y[j-1]))
    for a in T:
        print(a)
    return T

t1=time.process_time()      
print("Distance d'édition 2 : ",DIST_1(x,y)[0])        
t2=time.process_time()
print("Temps d'execution 2 = ",t2-t1)

T=DIST_T(x,y)

def SOL_1(x,y,T):
    u=[]
    v=[]
    i=lenx
    j=leny
    while(i>0 and j>0):
        if(T[i][j]==T[i][j-1]+2):
            """insertion"""
            u.insert(0,"-")
            v.insert(0,y[j-1])
            j-=1
            continue
        if(T[i][j]==T[i-1][j]+2):
            """suppression"""
            u.insert(0,x[i-1])
            v.insert(0,"-")
            i-=1
            continue
        if(T[i][j]==T[i-1][j-1]+substitution(x[i-1],y[j-1])):
            """match ou substitution"""
            u.insert(0,x[i-1])
            v.insert(0,substitution2(x[i-1],y[j-1]))
            i-=1
            j-=1
            continue
    while(i>0):
        u.insert(0,x[i-1])
        v.insert(0,"-")
        i-=1
    while(j>0):
        u.insert(0,"-")
        v.insert(0,y[j-1])
        j-=1
    return (u,v)

#print("Un alignement minimal est : \n",SOL_1(x,y,T))

def PROG_DYN(x,y):
    Res=DIST_1(x,y)
    print("Distance d'édition par programmation dynamique 1 : ",Res[0])
    print("Un alignement minimal possible est : \n",SOL_1(x,y,Res[1]))

PROG_DYN(x,y)

"""-------------------------- Tâche C ------------------------------------------"""
def DIST_2(x,y):
    T=[[0]*(leny+1) for i in range(2)]
    k=lenx
    cpt=0
    i=1
    for j in range(1,leny+1):
        T[0][j]=j*2
    T[1][0]=2
    while(cpt<k):
        for j in range(1,leny+1):
            T[i][j]=min(T[(i-1)%2][j]+2,T[i][j-1]+2,T[(i-1)%2][j-1]+substitution(x[cpt],y[j-1]))
        for a in T:
            print(a)
        print("--------------------")
        i=(i+1)%2
        T[i][0]=T[(i-1)%2][0]+2
        cpt+=1
    if(k%2==0):
        return T[0][leny]
    return T[1][leny]

print("Distance d'édition 3 : ",DIST_2(x,y))
