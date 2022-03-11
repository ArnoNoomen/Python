import pyodbc

print(pyodbc.drivers())
conn_str = (r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};'
            r'DBQ=C:\\Users\\arnon\\Documents\\Abnamro\\BANK.accdb;'
            )
conn_str = (r'DSN=arno;'
            )
print(conn_str)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()
cursor.execute('select * from parameters')

for row in cursor.fetchall():
    print (row)
