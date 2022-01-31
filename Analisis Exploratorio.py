#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Analisis exploratorio del conjunto de datos

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm 


# In[2]:


#Carga de archivo csv desde una URL
url = 'https://raw.githubusercontent.com/crisvel23/analisis_exploratorio_datos/master/analisis/MSP_VACUNA_COVID_2021.csv'
df = pd.read_csv(url, encoding='latin-1', sep=";") #index_col=0
print(df.head(8)) 


# In[3]:


#Conocer información básica
print('Cantidad de Filas y columnas:',df.shape)
print('Nombre columnas:',df.columns) 


# In[4]:


#Columnas, nulos y tipo de datos
df.info() 


# In[5]:


#Descripción estadística de los datos numéricos
df.describe() 


# In[6]:


#Cargar de una 2da fuente de datos: vacunacion_formato
url = 'https://raw.githubusercontent.com/crisvel23/analisis_exploratorio_datos/master/analisis/vacunacion_formato.csv'
df_pop = pd.read_csv(url, encoding='latin-1', sep=",")
print(df_pop.head(6)) 


# In[7]:


df_pop_es = df_pop[df_pop[" nacionalidad"] == ' Ecuatoriano/a' ]
df_pop_es.head() 


# In[8]:


df_pop_es.shape 


# In[9]:


df_pop_ar = df_pop[(df_pop[" provincia"] == 'PICHINCHA')]
df_pop_ar.head() 


# In[10]:


df_pop_ar.shape 


# In[11]:


df_pop_ar.set_index(' gedad').plot(kind='bar') 


# In[12]:


#Carga del 1er archivo MSP_VACUNA_COVID_2021
url = 'https://raw.githubusercontent.com/crisvel23/analisis_exploratorio_datos/master/analisis/MSP_VACUNA_COVID_2021.csv'
df = pd.read_csv(url, encoding='latin-1', sep=";") #index_col=0
print(df.head(8)) 


# In[15]:


#Filtro por provincias
df_provincia = df.replace(np.nan, '', regex=True)
df_provincia = df_provincia[ df_provincia['provincia'].str.contains('PICHINCHA') ]
df_provincia  


# In[16]:


df_provincia.shape 


# In[19]:


df_provincia.shape 


# In[ ]:




