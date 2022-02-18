#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 00:08:24 2018

@author: laura
"""

import numpy as np

def simplexT(m,n,A,c,b,z):
   contador=0
   M=montaM(m,n,A,c,b,z)
   print("iteração i=",contador)

   print (M)
   sim=1
   while sim==1:
        contador=contador+1     
        k=-1
        l=-1
        cont=0
        minimo1=c[0]
        minimo2=100000
        for i in range(n-1):
            if minimo1>=c[i]:
                
                minimo1=c[i]
                k=i
                
        if minimo1>=0:
            sim=0
        else:
            for i in range(m-1):
                if A[i,k]<=0:
                    cont=cont+1
            if cont==(m-1):
                sim=0
            else:
                for i in range(m-1):
                    if(A[i,k]>0):
                        if minimo2>=(b[i]/A[i,k]):
                            minimo2=(b[i]/A[i,k])
                            l=i+1
                        
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



def simplexD(m,n,A,c,b,zbarra):

   M=montaM(m,n,A,c,b,zbarra)
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
   z=M[0,n-1]
   M=simplexT(m,n,A,c,b,z)
   return M
                

def pivoteamento(M,m,n,l,k):

    if M[l,k]!=1:
        M[l,:]=(M[l,:]/M[l,k])
    for i in range(m):
        if (i!=l) and (M[i,k]!=0):
            M[i,:]=-M[l,:]*M[i,k]+M[i,:]
    return M 

def montaM(m,n,A,c,b,zbarra):
    M=np.zeros((m,n ))
    M[0,n-1]=zbarra
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
sinal=int(input("o problema é de maximização (1) ou minimização (0)?"))
n=int(input("número de variáveis:"))

m=int(input("número de restrições:"))

zbarra=float(input("solução inicial:"))
b=[]
c=[]
A=np.zeros((m,n))
for i in range(n):
    print("vetor de custos c",i+1)
    c.append(float(input()))
for i in range(m):
    print("vetor de recursos b",i+1)
    b.append(float(input()))
for i in range(m):
    for j in range(n):
        print("elemento a",i+1,j+1, "da matriz A")
        aij=float(input())
        A[i,j]=aij
    
n=n+1
m=m+1


Matriz=simplexT(m,n,A,c,b,zbarra)
print("tabela de solução ótima")
print (Matriz)
if sinal==0:
    print("solução ótima: z=",-Matriz[0,n-1])
else:
    print("solução ótima: z=",Matriz[0,n-1])