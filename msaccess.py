import pyodbc

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\\Users\\arnon\\Documents\\Abnamro\\BANK.accdb;')
cursor = conn.cursor()
cursor.execute('select * from parameters')

for row in cursor.fetchall():
    print (row)
