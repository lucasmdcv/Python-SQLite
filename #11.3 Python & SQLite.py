#11.3 Python & SQLite
import sqlite3
conexão= sqlite3.connect("agenda.db")
cursor = conexão.cursor()
cursor.execute('''
        create table ageda(
            nome text,
            telefone text )
        ''')
cursor.execute(''' 
        insert into agenda (nome, telefone)
            values(?, ?)
            ''',("Nilo","7788-1432"))
conexão.commit()
cursor.close()
conexão.close()