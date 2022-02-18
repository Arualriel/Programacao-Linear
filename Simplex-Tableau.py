#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 07:29:21 2018

@author: laura
"""
import numpy as np

def simplexT(m,n,A,c,b):
   contador=0
   M=montaM(m,n,A,c,b)
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
                

def pivoteamento(M,m,n,l,k):

    if M[l,k]!=1:
#        for j in range(n):
 #           if(j!=l):
        M[l,:]=(M[l,:]/M[l,k])
    for i in range(m):
        if (i!=l) and (M[i,k]!=0):
            M[i,:]=-M[l,:]*M[i,k]+M[i,:]
            #for j in range(n):
            #    M[i,j]=-M[l,j]*M[i,k]+M[i,j]
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