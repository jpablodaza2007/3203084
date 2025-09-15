import psycopg2
conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password=1234,
    dbname="ejemplo",
    port=5432,
)
print(conn)
print("Conexion exitosa")

cursor = conn.cursor()
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES ('Felipe', '18');")
cursor.execute("SELECT id, nombre, edad FROM usuarios")
for usuarios in cursor.fetchall():
    print(f"ID: {usuarios[0]}, Nombre: {usuarios[1]}, Edad: {usuarios[2]}")

conn.commit()
cursor.close()
conn.close()