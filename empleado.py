import pandas as pd
datos = {
        "nombre":["juan","lina"],
        "edad":[23,24],
        "ciudad":["mosquera","bogota"],
        "salario":[200,300],
    }

df = pd.DataFrame(datos)

edad = df[df["edad"]>20]

print(df)
print(df.shape)
print(df.columns.tolist())
print(df.head(3))
print(df.tail(2))
print(df.describe())
print(df["nombre"])
print(edad)
df.to_csv('Empleado.csv', index= False)