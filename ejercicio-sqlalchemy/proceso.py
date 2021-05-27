from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv

# se importa la clase(s) del 
# archivo genera_tablas
from genera_base import Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

#Lectura del archivo
with open('data/mundial2018.csv', encoding='UTF8') as File:
  
    datos = csv.reader(File,delimiter='|', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
    next(datos)
    for row in datos:
        
        altura=int(row[7],base=0)
        goles=int(row[9],base=0)
        numeroT=int(row[0],base=0)
        print(altura)
        j = Jugador(numero=numeroT, nombre_FIFA=row[1], nombre_jug=row[4], apellido_jug=row[3],
            posicion=row[6], altura=altura, goles=goles, caps=row[8], pais=row[2])
        session.add(j) 

# confirmacion de transacciones
session.commit()
