#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 13:03:48 2019

@author: 3700088
"""
t=[]
#%%
import linecache
import os
import tracemalloc
import time
import math

def display_top(snapshot, key_type='lineno', limit=10):
    snapshot = snapshot.filter_traces((
        tracemalloc.Filter(False, "<frozen importlib._bootstrap>"),
        tracemalloc.Filter(False, "<unknown>"),
    ))
    top_stats = snapshot.statistics(key_type)

    print("Top %s lines" % limit)
    for index, stat in enumerate(top_stats[:limit], 1):
        frame = stat.traceback[0]
        # replace "/path/to/module/file.py" with "module/file.py"
        filename = os.sep.join(frame.filename.split(os.sep)[-2:])
        print("#%s: %s:%s: %.1f KiB"
              % (index, filename, frame.lineno, stat.size / 1024))
        line = linecache.getline(frame.filename, frame.lineno).strip()
        if line:
            print('    %s' % line)

    other = top_stats[limit:]
    if other:
        size = sum(stat.size for stat in other)
        print("%s other: %.1f KiB" % (len(other), size / 1024))
    total = sum(stat.size for stat in top_stats)
    print("Total allocated size: %.1f KiB" % (total / 1024))

#
#tracemalloc.start()

"""Ouverture du fichier"""
lec=open("C:/Users/azwbd/OneDrive/Documents/3I003/Projet/Instances_genome/Inst_0001000_23.adn","r")
"""lecture des 2 premieres lignes"""
lenx=int(lec.readline())
leny=int(lec.readline())
"""stockage des sequences sous forme de tableau"""
x=lec.readline().split()
y=lec.readline().split()
lec.close()


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
#
def substitution2(a,b):
    """Entrée : a et b deux caractères appartennant à l'alphabet considéré ('A','T','C','G')
    Sortie : la nouvelle valeur de l'élément substitué"""
    return a

"""----------------------------- Tâche B -------------------------------------------------"""


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

#print("Affichage de I : ",coupure(x,y))

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

"----------------------------------------------------------------------------------------"
#
tracemalloc.start()
#
t1=time.process_time()
u=[]
v=[]
print(SOL_2(x,y,u,v))
t2=time.process_time()
print("Temps d'execution = ",t2-t1)
#
snapshot = tracemalloc.take_snapshot()
display_top(snapshot)
#%%
#30.9 KiB