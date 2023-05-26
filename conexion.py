import mysql.connector

conexion1 = mysql.connector.connect(
    host='tiako.mysql.database.azure.com', 
    user='kirabelak', 
    password='Tec2.tiako', 
    database='tiakodb')
cursor1=conexion1.cursor()
cursor1.execute("select * from publicacion")
for tabla in cursor1:
    print(tabla)
conexion1.close()   