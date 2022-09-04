# Programa 11.2 - Consulta, registro por registro
import sqlite3
conexão = sqlite3.connect("agenda.db")
cursor = conexão.cursor()
cursor.execute("select * from agenda")
while True:
    resultado = cursor.fetchone()
    if resultado is None:
        break
    print(f"Nome:{resultado[0]}\nTelefone: {resultado[1]}")
cursor.close()
conexão.close()
