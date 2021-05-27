
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ # se importa el operador and

# se importa la clase(s) del 
# archivo genera_base
from genera_base import Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

# se genera enlace al gestor de base de datos
# para el ejemplo se usa la base de datos sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()


# Obtener todos los registros de·
# la tabla Jugadores ordenados por la altura
jugadores = session.query(Jugador).order_by(Jugador.altura).all()

print("Listado de jugadores Ordenados por su altura")
for j in jugadores:
    # Imprime cada jugador
    print("%s" % (j))
   