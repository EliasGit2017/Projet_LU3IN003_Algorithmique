#### -*- coding: utf-8 -*-
###"""
###Created on Sat Oct 26 15:33:46 2019
###
###--------Infini : ------------------------------------------------------------------------
###math.inf
###Un flottant positif infini. (Pour un infini négatif, utilisez -math.inf.) Équivalent au résultat de float('inf').
###Nouveau dans la version 3.5.
###    
###         import math
###         test=math.inf
###         
###         ou 
###         
###         test=float("inf")
###         
###         from decimal import Decimal
###         pos_inf = Decimal('Infinity')
###         neg_inf = Decimal('-Infinity')
###-----------------------------------------------------------------------------------------
###@author: Elias Bendjaballah 3700088
###"""
###import math
###import time
###
###import psutil
###import os
###
###def memory_usage_psutil():
###    """retourne la quantité de mémoire utilisée par le programme"""
###    process=psutil.Process(os.getpid())
###    mem=process.memory_info()[0]/float(2**20)
###    return mem  
###
###"""Ouverture du fichier"""
###lec=open("C:/Users/azwbd/OneDrive/Documents/3I003/Projet/Instances_genome/Inst_0000013_89.adn","r")
###"""lecture des 2 premieres lignes"""
###lenx=int(lec.readline())
###leny=int(lec.readline())
###"""stockage des sequences sous forme de tableau"""
###x=lec.readline().split()
###y=lec.readline().split()
###lec.close()
###
###def DIST_NAIF(x,y):
###    """Entree : x et y deux mots
###    Sortie : d(X,Y) la distance d'edition de x a y """
###    return DIST_NAIF_REC(x,y,0,0,0,math.inf)
###
###def substitution(a,b):
###    A={'A','T'}
###    B={'G','C'}
###    if (a != b):
###        if ((a in A) and (b in A)) or ((a in B) and (b in B)):
###            return 3
###        else:
###            return 4
###    return 0
###        
###def DIST_NAIF_REC(x,y,i,j,c,dist):
###    """Realise l'exploration complete des alignements possibles pour un couple (x,y) donne
###    et retourne le coût du meilleur alignement.
###    Entree : x et y 2 mots de longueurs respectives lenx et leny
###                i dans [0,n] et j dans [0,m] deux indices sur x et y
###                c le cout d'un alignement
###                dist le cout du meilleur alignement de (x,y) connu avant cet appel
###     Sortie : dist le cout du meilleur alignement de (x,y) connu après cet appel"""
###    if (i == lenx) and (j == leny):
###        if(c < dist):
###            dist=c
###    else:
###        if(i < lenx) and (j < leny):
###            dist=DIST_NAIF_REC(x,y,i+1,j+1,c+substitution(x[i],y[j]),dist)
###        if(i < lenx):
###            dist=DIST_NAIF_REC(x,y,i+1,j,c+2,dist)
###        if(j < leny):
###            dist=DIST_NAIF_REC(x,y,i,j+1,c+2,dist)
###    return dist
###"---------------------------------------------------------------------------------"
####t1=time.time()
####print("Distance d'edition : ",DIST_NAIF(x,y))
####t2=time.time()
####print("Temps d'execution = ",t2-t1)
###
###
###def substitution2(a,b):
###    """Entrée : a et b deux caractères appartennant à l'alphabet considéré ('A','T','C','G')
###    Sortie : la nouvelle valeur de l'élément substitué"""
###    return a
###
###def DIST_1(x,y):
###    T=[[0]*(len(y)+1) for i in range (len(x)+1)]
###    for i in range(len(x)+1):
###        T[i][0]=i*2
###    for j in range(1,len(y)+1):
###        T[0][j]=j*2
###    for i in range(1,len(x)+1):
###        for j in range(1,len(y)+1):
###            T[i][j]=min(T[i-1][j]+2,T[i][j-1]+2,T[i-1][j-1]+substitution(x[i-1],y[j-1]))
###    for a in T:
###        print(a)
###    return T[len(x)][len(y)]
###        
###print("Distance d'édition 2 : ",DIST_1(x,y)) 
###
###
###
###def DIST_T(x,y):
###    T=[[0]*(len(y)+1) for i in range (len(x)+1)]
###    for i in range(len(x)+1):
###        T[i][0]=i*2
###    for j in range(1,len(y)+1):
###        T[0][j]=j*2
###    for i in range(1,len(x)+1):
###        for j in range(1,len(y)+1):
###            T[i][j]=min(T[i-1][j]+2,T[i][j-1]+2,T[i-1][j-1]+substitution(x[i-1],y[j-1]))
###    for a in T:
###        print(a)
###    return T
###
###T=DIST_T(x,y)
###
####def SOL_1(x,y,T):
####    Al=[[""]*(len(y)) for i in range (len(x))]
####    Bl=[[""]*(len(y)) for i in range (len(x))]
####    for i in range(1,len(x)):
####        for j in range(1,len(y)):
####            if(T[i][j]==T[i][j-1]+2):
####                Al[i][j]=Al[i][j-1]+"-"
####                Bl[i][j]+=Bl[i][j-1]+y[j-1]
####            if(T[i][j]==T[i-1][j]+2):
####                Al[i][j]+=Al[i-1][j]+x[i-1]
####                Bl[i][j]+=Bl[i-1][j]+"-"
####            if(T[i][j]==T[i-1][j-1]+substitution(x[i-1],y[j-1])):
####                Al[i][j]+=Al[i-1][j-1]+x[i-1]
####                Bl[i][j]+=Bl[i-1][j-1]+substitution2(x[i-1],y[j-1])
####    print(Al)
####    print("--------------------------------")
####    print(Bl)
####  
####print(SOL_1(x,y,T))
###
###
###def SOL_1(x,y,T):
###    u=[]
###    v=[]
###    i=len(x)
###    j=len(y)
###    while(i>0 and j>0):
###        if(T[i][j]==T[i-1][j-1]+substitution(x[i-1],y[j-1])):
###            """match ou substitution"""
###            u.insert(0,x[i-1])
###            v.insert(0,substitution2(x[i-1],y[j-1]))
###            i-=1
###            j-=1
###            #print(i,j)
###            continue
###        if(T[i][j-1]<T[i][j]):
###            """insertion"""
###            u.insert(0,"-")
###            v.insert(0,y[j-1])
###            j-=1
###            #print(i,j)
###            continue
###        if(T[i-1][j] < T[i][j]):
###            """suppression"""
###            u.insert(0,x[i-1])
###            v.insert(0,"-")
###            i-=1
###            #print(i,j)
###            continue
###    while(i>0):
###        u.insert(0,x[i-1])
###        v.insert(0,"-")
###        i-=1
###    while(j>0):
###        u.insert(0,"-")
###        v.insert(0,y[j-1])
###        j-=1
###    return (u,v)
###
###print("Un alignement minimal est : \n",SOL_1(x,y,T))
###
####def SOL_1(x,y,T):
####    u=[]
####    v=[]
####    #A=[[""]*(len(y)+1) for i in range (len(x)+1)]
####    #B=[[""]*(len(y)+1) for i in range (len(x)+1)]
####    for i in range(0,len(x)):
####        for j in range(0,len(y)):
####            if(j > 0 and T[i][j]==T[i][j-1]+2):
####                u.append("-")
####                v.append(y[i])
####            if(i > 0 and T[i][j]==T[i-1][j]+2):
####                u.append(x[i])
####                v.append("-")
####            if(T[i][j]==T[i-1][j-1]+substitution(x[i],y[j])):
####                u.append(x[i])
####                v.append(y[j])
####    return (u,v)
###            
####print(SOL_1(x,y,T))           
###
####remplir le tableau avec dans chaque case les alignements obtenus à l'étape correspondant aux coordonnées de la case du tableau
####programmation dynamique, prendre le min à chaque étape
####def SOL_1(x,y,T):
####    
####    A=[[""]*(len(y)+1) for i in range (len(x)+1)]
####    B=[[""]*(len(y)+1) for i in range (len(x)+1)]
####    for i in range(0,len(x)):
####        for j in range(0,len(y)):
####            if(j > 0 and T[i][j]==T[i][j-1]+2):
####                A[i][j]=A[i][j-1]+"-"
####                B[i][j]=B[i][j-1]+y[j]
####            if(i > 0 and T[i][j]==T[i-1][j]+2):
####                A[i][j]=A[i-1][j]+x[i]
####                B[i][j]=B[i-1][j]+"-"
####            if(T[i][j]==T[i-1][j-1]+substitution(x[i],y[j])):
###
###
###
####                A[i][j]=A[i-1][j-1]+x[i]
####                B[i][j]=[i-1][j-1]+y[j]
####    print(A)
####    print("--------------------")
####    print(B)
#####    return (A[len(x)][len(y)],B[len(x)][len(y)])
####def SOL_1(x,y,T):
####    u=[]
####    v=[]
####    A=[[("","")]*(len(y)+1) for i in range (len(x)+1)]
####    for i in range(0,len(x)):
####        for j in range(0,len(y)):
####            if(j > 0 and T[i][j]==T[i][j-1]+2):
#####                u.append("-")
#####                v.append(y[j])
#####                print("u=",u,"v=",v)
####                A[i][j][0]+="-"
####                A[i][j][1]+=y[j]
####            if(i > 0 and T[i][j]==T[i-1][j]+2):
#####                u.append(x[i])
#####                v.append("-")
#####                print("u=",u,"v=",v)
####                A[i][j][0]+=x[i]
####                A[i][j][1]+="-"
####            if(T[i][j]==T[i-1][j-1]+substitution(x[i],y[j])):
#####                u.append(x[i])
#####                v.append(substitution2(x[i],y[j]))
#####                A[i][j]=(u,v)
#####                print("u=",u,"v=",v)
####                A[i][j][0]+=x[i]
####                A[i][j][1]+=substitution2(x[i],y[j])
####    print(A)
####    print("--------------------")
####    return
###
###import linecache
###import os
###import tracemalloc
###
###def display_top(snapshot, key_type='lineno', limit=10):
###    snapshot = snapshot.filter_traces((
###        tracemalloc.Filter(False, "<frozen importlib._bootstrap>"),
###        tracemalloc.Filter(False, "<unknown>"),
###    ))
###    top_stats = snapshot.statistics(key_type)
###
###    print("Top %s lines" % limit)
###    for index, stat in enumerate(top_stats[:limit], 1):
###        frame = stat.traceback[0]
###        # replace "/path/to/module/file.py" with "module/file.py"
###        filename = os.sep.join(frame.filename.split(os.sep)[-2:])
###        print("#%s: %s:%s: %.1f KiB"
###              % (index, filename, frame.lineno, stat.size / 1024))
###        line = linecache.getline(frame.filename, frame.lineno).strip()
###        if line:
###            print('    %s' % line)
###
###    other = top_stats[limit:]
###    if other:
###        size = sum(stat.size for stat in other)
###        print("%s other: %.1f KiB" % (len(other), size / 1024))
###    total = sum(stat.size for stat in top_stats)
###    print("Total allocated size: %.1f KiB" % (total / 1024))
###
###
###tracemalloc.start()
###snapshot = tracemalloc.take_snapshot()
###display_top(snapshot)
### -*- coding: utf-8 -*-
##"""
##Created on Sat Oct 26 15:33:46 2019
##
##--------Infini : ------------------------------------------------------------------------
##math.inf
##Un flottant positif infini. (Pour un infini négatif, utilisez -math.inf.) Équivalent au résultat de float('inf').
##Nouveau dans la version 3.5.
##    
##         import math
##         test=math.inf
##         
##         ou 
##         
##         test=float("inf")
##       
##         from decimal import Decimal
##         pos_inf = Decimal('Infinity')
##         neg_inf = Decimal('-Infinity')
##-----------------------------------------------------------------------------------------
##@author: Elias Bendjaballah 3700088
##"""
##import math
##import time
##
##import tracemalloc
##import memory_profiler
##
##import psutil
##import os
##
##def memory_usage_psutil():
##    """retourne la quantité de mémoire utilisée par le programme"""
##    process=psutil.Process(os.getpid())
##    mem=process.memory_info()[0]/float(2**20)
##    return mem 
##    
##"""Ouverture du fichier"""
##lec=open("C:/Users/azwbd/OneDrive/Documents/3I003/Projet/Instances_genome/Inst_0000010_44.adn","r")
##"""lecture des 2 premieres lignes"""
##lenx=int(lec.readline())
##leny=int(lec.readline())
##"""stockage des sequences sous forme de tableau"""
##x=lec.readline().split()
##y=lec.readline().split()
##lec.close()
##
##def DIST_NAIF(x,y):
##    """Entree : x et y deux mots
##    Sortie : d(X,Y) la distance d'edition de x a y """
##    return DIST_NAIF_REC(x,y,0,0,0,math.inf)
##
##def substitution(a,b):
##    """Entrée : a et b deux caractères appartennant à l'alphabet considéré ('A','T','C','G')
##    Sortie : la valeur du coût de la subtitution de b à a (on remplace a par b)"""
##    A={'A','T'}
##    B={'G','C'}
##    if (a != b):
##        if ((a in A) and (b in A)) or ((a in B) and (b in B)):
##            return 3
##        else:
##            return 4
##    return 0
##
##def substitution2(a,b):
##    """Entrée : a et b deux caractères appartennant à l'alphabet considéré ('A','T','C','G')
##    Sortie : la nouvelle valeur de l'élément substitué"""
##    return a
##
##@profile(precision=3)
##def DIST_NAIF_REC(x,y,i,j,c,dist):
##    """Realise l'exploration complete des alignements possibles pour un couple (x,y) donné
##    et retourne le coût du meilleur alignement.
##    Entree : x et y 2 mots de longueurs respectives lenx et leny
##                i dans [0,n] et j dans [0,m] deux indices sur x et y
##                c le cout d'un alignement
##                dist le cout du meilleur alignement de (x,y) connu avant cet appel
##     Sortie : dist le cout du meilleur alignement de (x,y) connu après cet appel"""
##    if (i == lenx) and (j == leny):
##        if(c < dist):
##            dist=c
##    else:
##        if(i < lenx) and (j < leny):
##            dist=DIST_NAIF_REC(x,y,i+1,j+1,c+substitution(x[i],y[j]),dist)
##        if(i < lenx):
##            dist=DIST_NAIF_REC(x,y,i+1,j,c+2,dist)
##        if(j < leny):
##            dist=DIST_NAIF_REC(x,y,i,j+1,c+2,dist)
##    return dist
##
##
##"---------------------------------------------------------------------------------"
##t1=time.time()
##print("Distance d'edition 1 : ",DIST_NAIF(x,y))
##t2=time.time()
##print("Temps d'execution = ",t2-t1)
##
###Inst_0000010_8.adn (45 bytes) plus petit que Inst_0000010_7.adn (48 bytes)
###A trier
###Inst=["Inst_0000010_44.adn","Inst_0000010_7.adn","Inst_0000010_8.adn","Inst_0000012_13.adn","Inst_0000012_32.adn","Inst_0000012_56.adn","Inst_0000013_45.adn"]
###res=[0.07789802551269531,11.643845081329346,4.310308218002319,20.040199041366577,18.853809118270874,139.10138869285583,800.0115644931793]
##"----------------------------------------------------------------------------------"
##
##
##def DIST_1(x,y):
##    T=[[0]*(len(y)+1) for i in range (len(x)+1)]
##    for i in range(len(x)+1):
##        T[i][0]=i*2
##    for j in range(1,len(y)+1):
##        T[0][j]=j*2
##    for i in range(1,len(x)+1):
##        for j in range(1,len(y)+1):
##            T[i][j]=min(T[i-1][j]+2,T[i][j-1]+2,T[i-1][j-1]+substitution(x[i-1],y[j-1]))
##    for a in T:
##        print(a)
##    return T[len(x)][len(y)]
##
##
##def DIST_T(x,y):
##    T=[[0]*(len(y)+1) for i in range (len(x)+1)]
##    for i in range(len(x)+1):
##        T[i][0]=i*2
##    for j in range(1,len(y)+1):
##        T[0][j]=j*2
##    for i in range(1,len(x)+1):
##        for j in range(1,len(y)+1):
##            T[i][j]=min(T[i-1][j]+2,T[i][j-1]+2,T[i-1][j-1]+substitution(x[i-1],y[j-1]))
##    for a in T:
##        print(a)
##    return T
##
##t1=time.time()      
##print("Distance d'édition 2 : ",DIST_1(x,y))        
##t2=time.time()
##print("Temps d'execution 2 = ",t2-t1)
##
##T=DIST_T(x,y)
##
##def SOL_1(x,y,T):
##    u=[]
##    v=[]
##    i=len(x)
##    j=len(y)
##    while(i>0 and j>0):
##        if(T[i][j]==T[i][j-1]+2):
##            """insertion"""
##            u.insert(0,"-")
##            v.insert(0,y[j-1])
##            j-=1
##            continue
##        if(T[i][j]==T[i-1][j]+2):
##            """suppression"""
##            u.insert(0,x[i-1])
##            v.insert(0,"-")
##            i-=1
##            continue
##        if(T[i][j]==T[i-1][j-1]+substitution(x[i-1],y[j-1])):
##            """match ou substitution"""
##            u.insert(0,x[i-1])
##            v.insert(0,substitution2(x[i-1],y[j-1]))
##            i-=1
##            j-=1
##            continue
##    while(i>0):
##        u.insert(0,x[i-1])
##        v.insert(0,"-")
##        i-=1
##    while(j>0):
##        u.insert(0,"-")
##        v.insert(0,y[j-1])
##        j-=1
##    return (u,v)
##
##print("Un alignement minimal est : \n",SOL_1(x,y,T))
##
##def DIST_2(x,y):
##    T=[[0]*(len(y)+1) for i in range(2)]
##    k=len(x)
##    cpt=0
##    i=1
##    for j in range(1,len(y)+1):
##        T[0][j]=j*2
##    T[1][0]=2
##    while(cpt<k):
##        for j in range(1,len(y)+1):
##            T[i][j]=min(T[(i-1)%2][j]+2,T[i][j-1]+2,T[(i-1)%2][j-1]+substitution(x[cpt],y[j-1]))
##        print("--------------------")
##        for a in T:
##            print(a)
##        print("--------------------")
##        i=(i+1)%2
##        T[1][0]*=2
##        cpt+=1
##    return T[1][len(y)]
##
##print("Distance d'édition 2 : ",DIST_2(x,y))
## -*- coding: utf-8 -*-
#"""
#Created on Sat Oct 26 15:33:46 2019
#
#--------Infini : ------------------------------------------------------------------------
#math.inf
#Un flottant positif infini. (Pour un infini négatif, utilisez -math.inf.) Équivalent au résultat de float('inf').
#Nouveau dans la version 3.5.
#    
#         import math
#         test=math.inf
#         
#         ou 
#         
#         test=float("inf")
#       
#         from decimal import Decimal
#         pos_inf = Decimal('Infinity')
#         neg_inf = Decimal('-Infinity')
#-----------------------------------------------------------------------------------------
#@author: Elias Bendjaballah 3700088
#"""
##%%
#import math
#import time
#
#
#import psutil
#import os
#
#def memory_usage_psutil():
#    """retourne la quantité de mémoire utilisée par le programme"""
#    process=psutil.Process(os.getpid())
#    mem=process.memory_info().rss
#    return mem/1024
#    
#"""Ouverture du fichier"""
#lec=open("C:/Users/azwbd/OneDrive/Documents/3I003/Projet/Instances_genome/Inst_0000010_7.adn","r")
#"""lecture des 2 premieres lignes"""
#lenx=int(lec.readline())
#leny=int(lec.readline())
#"""stockage des sequences sous forme de tableau"""
#x=lec.readline().split()
#y=lec.readline().split()
#lec.close()
#
#def DIST_NAIF(x,y):
#    """Entree : x et y deux mots
#    Sortie : d(X,Y) la distance d'edition de x a y """
#    return DIST_NAIF_REC(x,y,0,0,0,math.inf)
#
#def substitution(a,b):
#    """Entrée : a et b deux caractères appartennant à l'alphabet considéré ('A','T','C','G')
#    Sortie : la valeur du coût de la subtitution de b à a (on remplace a par b)"""
#    A={'A','T'}
#    B={'G','C'}
#    if (a != b):
#        if ((a in A) and (b in A)) or ((a in B) and (b in B)):
#            return 3
#        else:
#            return 4
#    return 0
#
#def substitution2(a,b):
#    """Entrée : a et b deux caractères appartennant à l'alphabet considéré ('A','T','C','G')
#    Sortie : la nouvelle valeur de l'élément substitué"""
#    return a
#
#def DIST_NAIF_REC(x,y,i,j,c,dist):
#    """Realise l'exploration complete des alignements possibles pour un couple (x,y) donné
#    et retourne le coût du meilleur alignement.
#    Entree : x et y 2 mots de longueurs respectives lenx et leny
#                i dans [0,n] et j dans [0,m] deux indices sur x et y
#                c le cout d'un alignement
#                dist le cout du meilleur alignement de (x,y) connu avant cet appel
#     Sortie : dist le cout du meilleur alignement de (x,y) connu après cet appel"""
#    if (i == lenx) and (j == leny):
#        if(c < dist):
#            dist=c
#    else:
#        if(i < lenx) and (j < leny):
#            dist=DIST_NAIF_REC(x,y,i+1,j+1,c+substitution(x[i],y[j]),dist)
#        if(i < lenx):
#            dist=DIST_NAIF_REC(x,y,i+1,j,c+2,dist)
#        if(j < leny):
#            dist=DIST_NAIF_REC(x,y,i,j+1,c+2,dist)
#    return dist
#
#
#"----------------------------------------------------------------------------------------"
#t1=time.process_time()
#print("Distance d'edition 1 : ",DIST_NAIF(x,y))
#t2=time.process_time()
#print("Temps d'execution = ",t2-t1)
##%%
#"-----------------------------------------------------------------------------------------"
#
#"""----------------------------- Tâche B -------------------------------------------------"""
#
#def DIST_1(x,y):
#    T=[[0]*(leny+1) for i in range (lenx+1)]
#    for i in range(lenx+1):
#        T[i][0]=i*2
#    for j in range(1,leny+1):
#        T[0][j]=j*2
#    for i in range(1,lenx+1):
#        for j in range(1,leny+1):
#            T[i][j]=min(T[i-1][j]+2,T[i][j-1]+2,T[i-1][j-1]+substitution(x[i-1],y[j-1]))
#    for a in T:
#        print(a)
#    return (T[lenx][leny],T)
#
#
#def DIST_T(x,y):
#    T=[[0]*(leny+1) for i in range (lenx+1)]
#    for i in range(lenx+1):
#        T[i][0]=i*2
#    for j in range(1,leny+1):
#        T[0][j]=j*2
#    for i in range(1,lenx+1):
#        for j in range(1,leny+1):
#            T[i][j]=min(T[i-1][j]+2,T[i][j-1]+2,T[i-1][j-1]+substitution(x[i-1],y[j-1]))
#    for a in T:
#        print(a)
#    return T
#
#t1=time.process_time()      
#print("Distance d'édition 2 : ",DIST_1(x,y)[0])        
#t2=time.process_time()
#print("Temps d'execution 2 = ",t2-t1)
#
#T=DIST_T(x,y)
#
#def SOL_1(x,y,T):
#    u=[]
#    v=[]
#    i=lenx
#    j=leny
#    while(i>0 and j>0):
#        if(T[i][j]==T[i][j-1]+2):
#            """insertion"""
#            u.insert(0,"-")
#            v.insert(0,y[j-1])
#            j-=1
#            continue
#        if(T[i][j]==T[i-1][j]+2):
#            """suppression"""
#            u.insert(0,x[i-1])
#            v.insert(0,"-")
#            i-=1
#            continue
#        if(T[i][j]==T[i-1][j-1]+substitution(x[i-1],y[j-1])):
#            """match ou substitution"""
#            u.insert(0,x[i-1])
#            v.insert(0,substitution2(x[i-1],y[j-1]))
#            i-=1
#            j-=1
#            continue
#    while(i>0):
#        u.insert(0,x[i-1])
#        v.insert(0,"-")
#        i-=1
#    while(j>0):
#        u.insert(0,"-")
#        v.insert(0,y[j-1])
#        j-=1
#    return (u,v)
#
##print("Un alignement minimal est : \n",SOL_1(x,y,T))
#
#def PROG_DYN(x,y):
#    Res=DIST_1(x,y)
#    print("Distance d'édition par programmation dynamique 1 : ",Res[0])
#    print("Un alignement minimal possible est : \n",SOL_1(x,y,Res[1]))
#
#PROG_DYN(x,y)
#
#"""-------------------------- Tâche C ------------------------------------------"""
#def DIST_2(x,y):
#    T=[[0]*(leny+1) for i in range(2)]
#    k=lenx
#    cpt=0
#    i=1
#    for j in range(1,leny+1):
#        T[0][j]=j*2
#    T[1][0]=2
#    while(cpt<k):
#        for j in range(1,leny+1):
#            T[i][j]=min(T[(i-1)%2][j]+2,T[i][j-1]+2,T[(i-1)%2][j-1]+substitution(x[cpt],y[j-1]))
#        for a in T:
#            print(a)
#        print("--------------------")
#        i=(i+1)%2
#        T[i][0]=T[(i-1)%2][0]+2
#        cpt+=1
#    if(k%2==0):
#        return T[0][leny]
#    return T[1][leny]
#
#t1=time.process_time()
#print("Distance d'édition 3 : ",DIST_2(x,y))
#t2=time.process_time()
#print("Temps d'éxecution CPU : ",t2-t1)
#
##%%
#x1=['A','T','T','G','T','A']
#y1=['A','T','C','T','T','A']
#
#lenx=6
#leny=6
#
#def coupure(x,y):
#    T=[[0]*(leny+1) for i in range(2)]
#    I=[[0]*(leny+1) for i in range(2)]
#    k=lenx
#    coup=k//2
#    cpt=0
#    i=1
#    i2=1
#    for j in range(1,leny+1):
#        T[0][j]=j*2
#    T[i][0]=2
#    for j in range(0,leny+1):
#        I[0][j]=j
#        I[1][j]=j
#    while(cpt<k):
#        for j in range(1,leny+1):
#            T[i][j]=min(T[(i-1)%2][j]+2,T[i][j-1]+2,T[(i-1)%2][j-1]+substitution(x[cpt],y[j-1]))
#            if(cpt>=coup):
#                if(T[i][j]==T[(i-1)%2][j]+2):
#                    I[i2][j]=I[(i2-1)%2][j]
#                elif(T[i][j]==T[i][j-1]+2):
#                    I[i2][j]=I[i2][j-1]
#                elif(T[i][j]==T[(i-1)%2][j-1]+substitution(x[cpt],y[j-1])):
#                    I[i2][j]=I[(i2-1)%2][j-1]
#        if(cpt>=coup):
#            i2=(i2+1)%2
#        print("Affichage de I:")
#        for a in I:
#            print(a)
#        time.sleep(2)
#        i=(i+1)%2
#        T[i][0]=T[(i-1)%2][0]+2
#        cpt+=1
#    if((k-coup)%2==0):
#        print("dis one")
#        return I[0]
#    return I[1]
#
#print("Affichage de I : ",coupure(x1,y1))  
##%%

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
    mem=process.memory_info().rss
    return mem/1024
    
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


def DIST_T(x,y):
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
    return T

t1=time.process_time()      
print("Distance d'édition 2 : ",DIST_1(x,y)[0])        
t2=time.process_time()
print("Temps d'execution 2 = ",t2-t1)

T=DIST_T(x,y)

def SOL_1(x,y,T):
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
    Res=DIST_1(x,y)
    print("Distance d'édition par programmation dynamique 1 : ",Res[0])
    print("Un alignement minimal possible est : \n",SOL_1(x,y,Res[1]))

PROG_DYN(x,y)

"""-------------------------- Tâche C ------------------------------------------"""
def DIST_2(x,y):
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
        for a in T:
            print(a)
        print("--------------------")
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



def coupure(x,y):
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
        print("Affichage de I:")
        for a in I:
            print(a)
        #time.sleep(1) #A retirer une fois ok
        i=(i+1)%2
        T[i][0]=T[(i-1)%2][0]+2
        cpt+=1
    if((k-coup)%2==0):
        return I[0][len(y)]
    return I[1][len(y)]

print("Affichage de I : ",coupure(x,y))

def mot_gaps(k):
    return ['-']*k

#A simplifier
def align_lettre_mot(x,y):
    i=0
    while(i<len(y)):
        if(y[i]==x[0]):
            return (mot_gaps(i)+x+mot_gaps(len(y)-i-1),y)
        i+=1
    if(i==len(y)):
        i=0
        while(i<len(y)):
            if(substitution(x[0],y[i])==3):
                return (mot_gaps(i)+substitution2(x[0],y[i])+mot_gaps(len(y)-i-1),y)
            i+=1
    if(i==len(y)):
        return (mot_gaps(i-1)+[substitution2(x[0],y[i-1])],y)
    

def SOL_2(x,y,u,v):
    n=len(x)
    m=len(y)
    i=n//2
    if(m==0 and n!=0):
        v+=(x,['-']*n)
    if(n==0 and m!=0):
        return(['-']*m,y) 
    if(n==1 and m>=1):
        return(align_lettre_mot(x,y)[0],align_lettre_mot(x,y)[1])
    elif(n>1 and m>=1):
       j=coupure(x,y)
       return (SOL_2(x[:i+1],y[:j+1]),SOL_2(x[i+1:],y[j+1:]))


print(SOL_2(x,y))    
