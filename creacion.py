import psycopg2
conn = psycopg2.connect(
    host="localhost",
    user="postgres",
     password=1234,
    dbname="ejemplo",
    port=5432
)
print(conn)
print("Conexion exitosa")

cursor = conn.cursor()

cursor.execute("CREATE TABLE usuarios (id SERIAL PRIMARY KEY, nombre VARCHAR(50), edad INT);")

conn.commit()
cursor.close()
conn.close()