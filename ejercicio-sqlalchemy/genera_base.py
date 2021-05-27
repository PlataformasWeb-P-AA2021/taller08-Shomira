'''
1. Dada la información en csv de la carpeta data; crea una base de datos en Sqlite.
2. Usar SqlAlchemy para el proceso.
3. NO se debe normalizar la información; es decir, para el ejercicio, se debe generar un sola tabla con los datos o características del CSV.
4. Crear un archivo para generar la base de datos.
5. Crear un archivo (proceso) para guardar la información.
6. Crear un archivo que permita presentar todos los jugadores, ordenados por el número de goles.
7. Crear un archivo que permita presentar todos los jugadores, ordenados por la estatura.
'''
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.sql.schema import UniqueConstraint

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Base = declarative_base()

# Ejemplo que representa la relación entre dos clases
# One to Many
# Un club tiene muchos jugadores asociados
'''
class Pais(Base):
    __tablename__ = 'pais'
    id = Column(Integer, primary_key=True)
    nombre_pais = Column(String(100), unique=True)
    jugador = relationship("jugador", back_populates="pais")
    
    def __repr__(self):
        return "Pais: nombre=%s \n jugador=%s "% (
                          self.nombre_pais,
                          self.jugador)
'''
class Jugador(Base):
    __tablename__ = 'jugador'
    id = Column(Integer, primary_key=True)
    numero = Column(Integer)
    nombre_FIFA = Column(String(100))
    nombre_jug = Column(String(100))
    apellido_jug= Column(String(100))
    posicion = Column(String(50))
    altura = Column(Integer)
    goles = Column(Integer)
    caps =Column(Integer)
    pais =Column(String(100))
    
    def __repr__(self):
        return "Jugador: numero =%d FIFADisplayName= %s nombre=%s apellido=%s posicion=%s altura=%d goles=%d caps=%d Nombre pais=%s\n "% (
                          self.numero,
                          self.nombre_FIFA,
                          self.nombre_jug,
                          self.apellido_jug,
                          self.posicion,
                          self.altura,
                          self.goles,
                          self.caps,
                          self.pais)

Base.metadata.create_all(engine)
