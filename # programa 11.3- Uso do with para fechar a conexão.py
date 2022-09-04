# programa 11.3- Uso do with para fechar a conexão
import sqlite3
from contextlib import closing
with sqlite3.connect("agenda.db")as conexão:
    cursor.execute('selct * from agenda')
    while True:
        resultado = cursor.fetchone()
        if resultado is None:
            break
        print(f"Nome: {resultado[0]} \nTelefone: {resultado[1]}")

