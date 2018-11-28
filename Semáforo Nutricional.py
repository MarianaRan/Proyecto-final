
# coding: utf-8

# In[12]:


import sys 
from termcolor import colored, cprint

class Comida:
    def __init__(self, nombre_comida, estado, sodio, azúcar, grasas_saturadas):
        self.nombre_comida = nombre_comida 
        self.estado = estado
        self.sodio = sodio
        self.azúcar = azúcar
        self.grasas_saturadas = grasas_saturadas

    def semáforo_nutricional(self, estado, sodio, azúcar, grasas_saturadas): 
        if self.estado == "Sólido": 
            if self.sodio <= 120: 
                print ((f"{self.nombre_comida} es"), colored ("BAJO", 'green'), ("en sodio"))
            elif 120 < self.sodio <= 600: 
                print ((f"{self.nombre_comida} es"), colored ("MEDIO", 'yellow'), ("en sodio"))
            elif self.sodio > 600: 
                print ((f"{self.nombre_comida} es"), colored ("ALTO", 'red'), ("en sodio. Cuidado con su consumo"))
            elif type(self.sodio) == float:
                print(f"Los valores deben de estar en miligramos")
                
            if self.azúcar <= 5: 
                print ((f"{self.nombre_comida} es"), colored ("BAJO", 'green'), ("en azúcar"))
            elif 5 < self.sodio <= 15: 
                print ((f"{self.nombre_comida} es"), colored ("MEDIO", 'yellow'), ("en azúcar"))
            elif self.sodio > 15: 
                print ((f"{self.nombre_comida} es"), colored ("ALTO", 'red'), ("en azúcar. Cuidado con su consumo"))
                  
            if self.grasas_saturadas <= 3: 
                print ((f"{self.nombre_comida} es"), colored ("BAJO", 'green'), ("en grasas"))
            elif 3 < self.sodio <= 20: 
                print ((f"{self.nombre_comida} es"), colored ("MEDIO", 'yellow'), ("en grasas"))
            elif self.sodio > 20: 
                print ((f"{self.nombre_comida} es"), colored ("ALTO", 'red'), ("en grasas. Cuidado con su consumo"))
            
            else: 
                print(f"Números no válidos. Recuerda tomar los valores del apartado'Infomación Nutrimental'")
                
        elif self.estado == "Líquido": 
            if self.sodio <= 0.3: 
                print ((f"{self.nombre_comida} es"), colored ("BAJO", 'green'), ("en sodio"))
            elif 0.3 < self.sodio <= 1.5: 
                print ((f"{self.nombre_comida} es"), colored ("MEDIO", 'yellow'), ("en sodio"))
            elif self.sodio > 1.5: 
                print ((f"{self.nombre_comida} es"), colored ("ALTO", 'red'), ("en sodio. Cuidado con su consumo"))
                  
            if self.azúcar <= 2.5: 
                print ((f"{self.nombre_comida} es"), colored ("BAJO", 'green'), ("en azúcar"))
            elif 2.5 < self.sodio <= 7.5: 
                print ((f"{self.nombre_comida} es"), colored ("MEDIO", 'orange'), ("en azúcar"))
            elif self.sodio > 7.5: 
                print ((f"{self.nombre_comida} es"), colored ("ALTO", 'red'), ("en azúcar. Cuidado con su consumo"))
                  
            if self.grasas_saturadas <= 1.5: 
                print ((f"{self.nombre_comida} es"), colored ("BAJO", 'green'), ("en grasas"))
            elif 1.5 < self.sodio <= 10: 
                print ((f"{self.nombre_comida} es"), colored ("MEDIO", 'yellow'), ("en grasas"))
            elif self.sodio > 10: 
                print ((f"{self.nombre_comida} es"), colored ("ALTO", 'red'), ("en grasas. Cuidado con su consumo"))
            
            else: 
                print(f"Números no válidos. Recuerda tomar los valores del apartado'Infomación Nutrimental'")

# In[13]:


twinky = Comida("Twinky", "Sólido", 170, 13, 2.5)
twinky.semáforo_nutricional("Sólido", 170, 13, 2.5)

