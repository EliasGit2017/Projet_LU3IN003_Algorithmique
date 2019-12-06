# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 15:33:46 2019
@author: Elias Bendjaballah 3700088
"""

import math
import time

    
"""Ouverture du fichier"""
lec=open("C:/Users/azwbd/OneDrive/Documents/3I003/Projet/Instances_genome/Inst_0000015_4.adn","r")
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
    Entree : x et y 2 mots de longueurs respectives len(x) et len(y)
                i dans [0,n] et j dans [0,m] deux indices sur x et y
                c le cout d'un alignement
                dist le cout du meilleur alignement de (x,y) connu avant cet appel
     Sortie : dist le cout du meilleur alignement de (x,y) connu après cet appel"""
    if (i == len(x)) and (j == len(y)):
        if(c < dist):
            dist=c
    else:
        if(i < len(x)) and (j < len(y)):
            dist=DIST_NAIF_REC(x,y,i+1,j+1,c+substitution(x[i],y[j]),dist)
        if(i < len(x)):
            dist=DIST_NAIF_REC(x,y,i+1,j,c+2,dist)
        if(j < len(y)):
            dist=DIST_NAIF_REC(x,y,i,j+1,c+2,dist)
    return dist


"----------------------------------------------------------------------------------------"
t1=time.process_time()
print("Distance d'edition 1 : ",DIST_NAIF(x,y))
t2=time.process_time()
print("Temps d'execution = ",t2-t1)

"-----------------------------------------------------------------------------------------"

"""----------------------------- Tâche B -------------------------------------------------"""

def DIST_1(x,y):
    """Entrée : x et y deux mots 
    Sortie : retourne la distance d'édition entre x et y ainsi que le tableau T des distances d'édition """
    T=[[0]*(len(y)+1) for i in range (len(x)+1)]
    for i in range(len(x)+1):
        T[i][0]=i*2
    for j in range(1,len(y)+1):
        T[0][j]=j*2
    for i in range(1,len(x)+1):
        for j in range(1,len(y)+1):
            T[i][j]=min(T[i-1][j]+2,T[i][j-1]+2,T[i-1][j-1]+substitution(x[i-1],y[j-1]))
    for a in T:
        print(a)
    return (T[len(x)][len(y)],T)


t1=time.process_time()      
print("Distance d'édition 2 : ",DIST_1(x,y)[0])        
t2=time.process_time()
print("Temps d'execution 2 = ",t2-t1)


def SOL_1(x,y,T):
    """Entrée : x et y deux mots
                T une matrice de dimensions [0,...,|x|]*[0,...,|y|] dont chaque case de coordonées
                i et j contient les valeurs des distances d'édition correspondantes aux mots
                x[0...i] et y[0...j]
        Sortie : (u,v) un alignement optimal où u et v représentent respectivement x et y modifiés """
    u=[]
    v=[]
    i=len(x)
    j=len(y)
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
    """Entrée : x et y deux mots
    Sortie : retourne la distance d'édition d(x,y) ainsi qu'un alignement optimal"""
    Res=DIST_1(x,y)
    print("Distance d'édition par programmation dynamique 1 : ",Res[0])
    print("Un alignement minimal possible est : \n",SOL_1(x,y,Res[1]))


PROG_DYN(x,y)

"""-------------------------- Tâche C ------------------------------------------"""
def DIST_2(x,y):
    """Entrée : x et y deux mots 
    Sortie : retourne la distance d'édition entre x et y ainsi que le tableau T des distances d'édition """
    T=[[0]*(len(y)+1) for i in range(2)]
    k=len(x)
    cpt=0
    i=1
    for j in range(1,len(y)+1):
        T[0][j]=j*2
    T[1][0]=2
    while(cpt<k):
        for j in range(1,len(y)+1):
            T[i][j]=min(T[(i-1)%2][j]+2,T[i][j-1]+2,T[(i-1)%2][j-1]+substitution(x[cpt],y[j-1]))
#        for a in T:
#            print(a)
#        print("--------------------")
        i=(i+1)%2
        T[i][0]=T[(i-1)%2][0]+2
        cpt+=1
    if(k%2==0):
        return T[0][len(y)]
    return T[1][len(y)]

t1=time.process_time()
print("Distance d'édition 3 : ",DIST_2(x,y))
t2=time.process_time()
print("Temps d'éxecution CPU : ",t2-t1)


"""------------------------Tâche D------------------------------------------"""


def coupure(x,y):
    """Entrée : x et y deux mots
    Sortie : l'indice j* permettant de réaliser la coupure de (x,y) sachant que i*=len(x)//2 """
    T=[[0]*(len(y)+1) for i in range(2)]
    I=[[0]*(len(y)+1) for i in range(2)]
    k=len(x)
    coup=k//2
    cpt=0
    i=1
    i2=1
    for j in range(1,len(y)+1):
        T[0][j]=j*2
    T[i][0]=2
    for j in range(0,len(y)+1):
        I[0][j]=j
        I[1][j]=j
    while(cpt<k):
        for j in range(1,len(y)+1):
            T[i][j]=min(T[(i-1)%2][j]+2,T[i][j-1]+2,T[(i-1)%2][j-1]+substitution(x[cpt],y[j-1]))
            if(cpt>=coup):
                if(T[i][j]==T[(i-1)%2][j]+2):
                    I[i2][j]=I[(i2-1)%2][j]
                elif(T[i][j]==T[i][j-1]+2):
                    I[i2][j]=I[i2][j-1]
                elif(T[i][j]==T[(i-1)%2][j-1]+substitution(x[cpt],y[j-1])):
                    I[i2][j]=I[(i2-1)%2][j-1]
        if(cpt>=coup):
            i2=(i2+1)%2
#        print("Affichage de I:")
#        for a in I:
#            print(a)
        #time.sleep(1) #A retirer une fois ok
        i=(i+1)%2
        T[i][0]=T[(i-1)%2][0]+2
        cpt+=1
    if((k-coup)%2==0):
        return I[0][len(y)]
    return I[1][len(y)]

print("Affichage de I : ",coupure(x,y))

def mot_gaps(k):
    """Entrée : k un entier naturel
    Sortie : le mot constitué de k gaps """
    return ['-']*k


def align_lettre_mot(x,y):
    """Entrée : x un mot de longueur 1 et y un mot non vide de longueur quelconque
    Sortie : un meilleur alignement parmi ceux possibles pour (x,y) """
    i=0
    while(i<len(y)):
        if(y[i]==x[0]):
            return (mot_gaps(i)+x+mot_gaps(len(y)-i-1),y)
        i+=1
    i=0
    while(i<len(y)):
        if(substitution(x[0],y[i])==3):
            return (mot_gaps(i)+[substitution2(x[0],y[i])]+mot_gaps(len(y)-i-1),y)
        i+=1
    if(i==len(y)):
        return (mot_gaps(i-1)+[substitution2(x[0],y[i-1])],y)
    

def SOL_2(x,y,u,v):
    """Entrée : x et y deux mots
                u et v deux paramètres servant à stocker les alignements optimaux temporaires
                et qui contiendront en fin d'éxecution les alignements optimaux de x et y
                (u et v sont des variables globales initialisées en tant que listes vides)
    Sortie : (u,v) l'alignement optimal calculé pour (x,y) """
    n=len(x)
    m=len(y)
    i=n//2
    if(m==0 and n!=0):
        u+=x
        v+=['-']*n
    elif(n==0 and m!=0):
        u+=['-']*m
        v+=y
    elif(n==1 and m>=1):
        u+=align_lettre_mot(x,y)[0]
        v+=align_lettre_mot(x,y)[1]
    elif(n>1 and m>=1):
       j=coupure(x,y)
       SOL_2(x[:i],y[:j],u,v)
       SOL_2(x[i:],y[j:],u,v)
    return (u,v)
"""Variables globales u et v servant à stocker l'alignement final"""
u=[]
v=[]
print(SOL_2(x,y,u,v))    
