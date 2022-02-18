#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 17:16:04 2018

@author: laura
"""

import numpy as np



def simplexT(m,n,A,c,b):

   M=montaM(m,n,A,c,b)
   contador=0
   print ("iteração i=",contador)
   print (M)
   sim=1
   
   while sim==1:
        contador=contador+1
        k=-1
        l=-1
        cont=0
        minimo1=b[0]
        maximo=-1000000
        for i in range(m-1):
            if (minimo1>=b[i]) and (b[i]<0):
                minimo1=b[i]
                l=i

        if minimo1>=0:
            sim=0
        else:
            for j in range(n-1):
                if A[l,j]>=0:
                    cont=cont+1
            if cont==(n-1):
                sim=0
            else:
                for i in range(n-1):
                    if(A[l,i]<0):
                        
                        if maximo<=(c[i]/A[l,i]):
                            maximo=(c[i]/A[l,i])
                            k=i
                        
                l=l+1
                M=pivoteamento(M,m,n,l,k)
                for i in range(m):
                    if i>0:
                        b[i-1]=M[i,n-1]
                for i in range(n):
                    if i<(n-1):
                        c[i]=M[0,i]
                        
                for i in range(m):
                    for j in range(n):
                        if (i>0) and (j<n-1):
                            A[i-1,j]=M[i,j]
                print("iteração i=",contador)
                print(M)
            cont=0
   return M
                

def pivoteamento(M,m,n,l,k):

    if M[l,k]!=1:
        M[l,:]=(M[l,:]/M[l,k])
    for i in range(m):
        if (i!=l) and (M[i,k]!=0):
            M[i,:]=-M[l,:]*M[i,k]+M[i,:]
    return M 

def montaM(m,n,A,c,b):
    M=np.zeros((m,n ))
    for i in range(n):
        if i!=(n-1):
            M[0,i]=c[i]
        else:
            M[0,i]=0
    for i in range(m):
        if i!=0:
            M[i,n-1]=b[i-1]
    for i in range(m):
        for j in range(n):
            if (i>0) and (j<n-1):
                M[i,j]=A[i-1,j]
    return M
    
print("Informe o PL na forma canônica")
n=int(input("número de variáveis:"))

m=int(input("número de restrições:"))


b=[]
c=[]
linha=[]
A=np.zeros((m,n))
for i in range(n):
    print("vetor de custos i=",i+1)
    c.append(int(input()))
for i in range(m):
    print("vetor de recursos i=",i+1)
    b.append(int(input()))
for i in range(m):
    for j in range(n):
        print("elemento a",i+1,j+1, "da matriz A")
        aij=int(input())
        A[i,j]=aij
    
n=n+1
m=m+1


Matriz=simplexT(m,n,A,c,b)
print("tabela de solução ótima")
print (Matriz)
print("solução ótima: z=",-Matriz[0,n-1])