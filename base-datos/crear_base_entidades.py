# crear_base_entidades.py
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from configuracion import cadena_base_datos

# Configuración del motor y la base declarativa
engine = create_engine(cadena_base_datos)
Base = declarative_base()

# ==========================================
# 1. ENTIDAD FACULTAD
# ==========================================
class Facultad(Base):
    __tablename__ = 'facultad'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(150), nullable=False, unique=True)
    ubicacion = Column(String(150))
    decano = Column(String(100))
    
    # Relación 1:N - Una facultad tiene muchas carreras
    carreras = relationship("Carrera", back_populates="facultad")

    def __repr__(self):
        return f"Facultad({self.id}): Nombre={self.nombre} | Ubicacion={self.ubicacion} | Decano={self.decano}"

# ==========================================
# 2. ENTIDAD CARRERA
# ==========================================
class Carrera(Base):
    __tablename__ = 'carrera'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(150), nullable=False, unique=True)
    codigo = Column(String(50), unique=True)
    
    # Clave Foránea: Depende de Facultad
    facultad_id = Column(Integer, ForeignKey('facultad.id'))
    
    # Relaciones
    facultad = relationship("Facultad", back_populates="carreras")
    profesores = relationship("Profesor", back_populates="carrera")

    def __repr__(self):
        return f"Carrera({self.id}): Nombre={self.nombre} | Codigo={self.codigo} | Facultad={self.facultad.nombre}"

# ==========================================
# 3. ENTIDAD PROFESOR
# ==========================================
class Profesor(Base):
    __tablename__ = 'profesor'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombres = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    correo = Column(String(150), unique=True)
    especialidad = Column(String(100))
    
    # Clave Foránea: Depende de Carrera
    carrera_id = Column(Integer, ForeignKey('carrera.id'))
    
    # Relaciones
    carrera = relationship("Carrera", back_populates="profesores")
    recursos = relationship("RecursoAcademico", back_populates="profesor")

    def __repr__(self):
        return f"Profesor({self.id}): Nombres={self.nombres} | Apellidos={self.apellidos} | Correo={self.correo} | Especialidad={self.especialidad} | Carrera={self.carrera.nombre}"

# ==========================================
# 4. ENTIDAD RECURSO ACADÉMICO
# ==========================================
class RecursoAcademico(Base):
    __tablename__ = 'recurso_academico'
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(200), nullable=False)
    fecha_publicacion = Column(Date)
    tipo = Column(String(50))
    url = Column(String(255))
    
    # Clave Foránea: Depende de Profesor
    profesor_id = Column(Integer, ForeignKey('profesor.id'))
    
    # Relación
    profesor = relationship("Profesor", back_populates="recursos")

    def __repr__(self):
        return f"RecursoAcademico({self.id}): Titulo={self.titulo} | Tipo={self.tipo} | Fecha={self.fecha_publicacion} | URL={self.url} | Profesor={self.profesor.nombres} {self.profesor.apellidos}"

# Generar físicamente las tablas en la base de datos
Base.metadata.create_all(engine)
print("Base de datos y tablas creadas con éxito.")