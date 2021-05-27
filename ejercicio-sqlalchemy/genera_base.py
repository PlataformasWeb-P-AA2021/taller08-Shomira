from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.sql.schema import UniqueConstraint

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

# se genera en enlace al gestor de base de datos
# para el ejemplo se usa la base de datossqlite
engine = create_engine(cadena_base_datos)

Base = declarative_base()

# Creacion de atributos de la Entidad Jugador
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
