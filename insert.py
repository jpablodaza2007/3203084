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
vars1 =input("Ingrese el nombre: ")
vars2 =input("Ingrese la edad: ")
cursor.execute(f"INSERT INTO usuarios (nombre, edad) VALUES ('{vars1}', {vars2});")
cursor.execute("SELECT id, nombre, edad FROM usuarios")
for usuarios in cursor.fetchall():
    print(f"ID: {usuarios[0]}, Nombre: {usuarios[1]}, Edad: {usuarios[2]}")

conn.commit()
cursor.close()
conn.close()