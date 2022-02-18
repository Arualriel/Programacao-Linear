#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 18:14:40 2018

@author: laura
"""

import numpy as np

def dualsimplex(m,n,A,c,b):
    sim=1
    cont=0
#fornecer pl na forma canonica: matriz A, vetor c, b
    M=montaM(m,n,A,c,b)
    
    
    
    while sim==1:
        cont=0
        l=0
        k=0
        minimo=b[0]
        maximo=0
        for i in range(m-1):
            if(b[i]>0):
                cont=cont+1
            if (b[i]<=minimo) and (b[i]<0):
                minimo=b[i]
                l=i
        if cont==(m-1):
            sim=0
            print("solucao atual otima \n",M[:,:])
        cont=0
        for i in range(n-1):
            if A[l,i]>=0:
                cont=cont+1
        if cont==(n-1):
            sim=0
            print("nao ha solucao viavel para o problema \n")
        else:        
            for i in range(n-1):
                if(A[l,i]<0):
                    if(c[i]/A[l,i])>=maximo:
                        maximo=c[i]/A[l,i]
                        k=i
            print("x",k+1," entra da base \n")
            print("x",l+1," sai da base \n")
        M=pivoteamento(M,m,n,l+1,k)
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
        
    return M[:,:]
        

        
def pivoteamento(M,m,n,l,k):

    if M[l,k]!=1:
        for j in range(m):
            M[j,k]=(M[j,k]/M[l,k])
    for i in range(m):
        if (i!=l) and (M[i,k]!=0):
            M[i,:]=-M[l,:]*M[i,k]+M[i,:]
            for j in range(n):
                M[i,j]=-M[l,j]*M[i,k]+M[i,j]
    return M        
def montaM(m,n,A,c,b):
    M=np.zeros((m,n))
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
                print(A)
                M[i,j]=A[i-1,j]
    return M
    
#variaveis
n=7
#n=n+1        
#restricoes          
m=4
#m=m+1
A=np.array([[-3.,-1.,-1.,1.,0.,0.],[3.,-3.,-1.,0.,1.,0.],[1.,1.,1.,0.,0.,1.]]
)
b=[-3.,-6.,3.]
c=[3.,2.,1.,0.,0.,0.]


Matriz=dualsimplex(m,n,A,c,b)
print (Matriz)