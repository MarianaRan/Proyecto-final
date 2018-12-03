
# coding: utf-8

# In[13]:


import matplotlib.pyplot as plt
from pydataset import data
import pandas as pd
centro = pd.read_csv("C:/Users/Despacho/Documents/Mariana/Python/proyecto_final/centros_salud.csv", encoding="iso-8859-1")


# In[14]:


centro.head()


# In[15]:


x1 = centro["Alcadia"]
x2 = centro ["Depresion"]
plt.scatter(x1, x2, color="#3A5FCD") 
plt.plot(x1, x2, color="#00CED1", linewidth=1) 
plt.title("Casos de depresión atendidos en centros de salud de la Ciudad de México, 2017") 
plt.xlabel("Alcaldía") 
plt.ylabel("Casos presentados") 
plt.grid(alpha=0.5) 


# In[2]:


import seaborn as sns
import pandas as pd
datos= pd.read_csv('centros_salud.csv')
grafica = sns.pairplot(datos, hue='Alcadia', palette="Spectral")


# In[18]:


#DUDAS: Dividir en colores. NSE Alto Medio Bajo. 
#Poner en cada punto el nombre de la alcaldía
#Casos de depresión y de ansiedad en un mismo mapa, o en diferentes?
#Cambiar el signo (punto, diamante, más), pero sólo en algunos casos. Por ejemplo, en el mayor y el menor. 
#Densidad. Número mayor no es preciso porque son más habitantes. 

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

x = centro['NSE'] 
y = centro['Depresion'] + centro['Depresion_urgencias'] + centro['Depresion_telefonica'] + centro['Depresion_consulta_externa']
sns.regplot(x, y, data= centro)

