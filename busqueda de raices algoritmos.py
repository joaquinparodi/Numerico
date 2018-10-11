#!/usr/bin/env python
# coding: utf-8

# In[2]:


#---------------------IMPORTS--------------------------#
import matplotlib
import numpy 
import scipy
import math


# In[3]:


#--------------------BISECCION------------------------#
def biseccion(f, x_inicial, x_final):
    a = x_inicial
    b = x_final
    
    error = abs(b-a)
    raiz_aprox = (a + b)/2
    
    i = 0
    while( error > 1e-5 ):
        
        raiz_aprox = (a + b)/2
        error = abs(b-a)/(2**i)
        
        if(f(a)*f(raiz_aprox) > 0):
            a = raiz_aprox
            
        if(f(b)*f(raiz_aprox) > 0):
            b = raiz_aprox
            
        if( f(raiz_aprox) == 0 ):
            return raiz_aprox
        
        i += 1
        
    return raiz_aprox


# In[16]:


def newton_raphson(f, f_fder, seed):
    x_act = seed
    error = 1.0 #Para inicializar
    
    #Controla que la seed no sea raiz
    if(f(x_act) == 0):
        return x_act
    
    #Primera iteracion
    x_sig = x_act - ( f(x_act)/f_fder(x_act) )
    if(f(x_act) == 0):
        return x_act
    error = abs(x_sig - x_act) 
    x_act = x_sig
    
    while( error > 1e-13 ):
        
        x_sig = x_act - (f(x_act)/f_fder(x_act))  
        if(f(x_act) == 0):
            return x_act  
        error = abs( x_sig - x_act ) 
        x_act = x_sig
    
    return x_act


# In[5]:


#------------------FUNCIONES--------------------------#
def f_1(x):
    return (x**2) - 2

def f_2(x):
    return (x**5) - 6.6*(x**4) + 5.12*(x**3) + 21.312*(x**2) - 38.016*(x) + 17.28 

def f_3(x):
    return (x-1.5)*math.exp( -4*(x - 1.5)**2 )

#---------------DERIVADAS PRIMERAS--------------------#
def f_1_fder(x):
    return 2*x

def f_2_fder(x):
    return 5*(x**4) - 25*(x**3) + 15.36*(x**2) + 42.624*8(x) - 38.016

def f_3_fder(x):
    return (-8*x + 12)*(x - 1.5)*math.exp(-4*( x - 1.5)**2 ) + math.exp( -4*(x - 1.5)**2 )


# In[17]:


print( newton_raphson(f_1, f_1_fder, 1.0) )


# In[15]:


print( biseccion(f_1, 0, 2.0) )

