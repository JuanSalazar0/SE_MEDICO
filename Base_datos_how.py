import mysql.connector

midb=mysql.connector.connect(
    host="localhost",
    user='root',
    password= 'juan1234',
    database='medico' 
)

cursor = midb.cursor()
cursor.execute('select * from Sintomas')
resultado= cursor.fetchall()

cursor.execute('select * from enfermedades')
nombres=cursor.fetchall()
#print(resultado)
#id, nombre, s1,        s2,     s3,     s4,     s5,        s6, 
#0    1       2          3      4         5      6         7        
#print(resultado[0][1]) #imprime goku 
#consulta de datos 
def Checar_inf(respuesta, dato):
    if respuesta == "y":
        res = 1
    else:
        res = 0
     
    to_remove=[]
    for d in resultado:
        if d[dato] != res:
            to_remove.append(d)
            #print(to_remove)
            #print(resultado)
            #print("si entre")
    for i in to_remove:
        resultado.remove(i)
        #print(to_remove)

    if len(resultado) == 1:
        print("Mi diagnostico es:")
        print( resultado[0][1])
        quit()
       

for z in range(len(nombres)):
    print("TTe sientes de la  siguiente manera?")
    print(nombres[z][1])
    #print(z)
    respuesta = input("(y/n)" )
    Checar_inf(respuesta, z+2)
    if z == len(nombres): break