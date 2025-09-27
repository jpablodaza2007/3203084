import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np


datos = {
    "nombre": ["juan","lina","Mauricio","coco","samuel","maria","sebastian",
               "carlos","maria","tom","zac","rocki","toni","lana","higor"],
    "edad": [23,24,30,17,20,90,17,17,28,34,45,32,43,21,38],
    "ciudad": ["mosquera","bogota","bucaramanga","mosquera","mosquera","mosquera",
               "Peru","bucaramanga","bucaramanga","bucaramanga","bucaramanga",
               "bucaramanga","bucaramanga","bucaramanga","bucaramanga"],
    "salario": [100,200,300,400,500,600,700,800,900,1000,100,200,300,400,500],
}


df = pd.DataFrame(datos)


plt.style.use("default")
sb.set_palette("husl")


plt.figure(figsize=(12, 8))

plt.subplot(2, 3, 1)
plt.scatter(df['nombre'], df['salario'],
            color='skyblue', edgecolor='black')
plt.title('Salario por empleado')
plt.xlabel('Empleado')
plt.ylabel('Salario')
plt.xticks(rotation=45)


plt.tight_layout()
plt.show()

df = pd.DataFrame(datos)

# Estilo
plt.style.use("default")
sb.set_palette("husl")

# Gráfico de barras
plt.figure(figsize=(12, 8))
plt.bar(df['nombre'], df['salario'], color="skyblue", edgecolor="black")

# Títulos y etiquetas
plt.title("Salario por empleado")
plt.xlabel("Empleado")
plt.ylabel("Salario")
plt.xticks(rotation=45)

# Mostrar
plt.tight_layout()
plt.show()





