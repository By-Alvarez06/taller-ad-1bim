from sqlalchemy.orm import sessionmaker
from crear_base_entidades import engine, Facultad, Carrera, Profesor, RecursoAcademico

# Configuración de la sesión
Session = sessionmaker(bind=engine)
session = Session()

# Definimos la facultad que queremos buscar
nombre_facultad_buscada = "Facultad de Ingeniería"

# Construcción de la consulta:
# 1. Queremos los Recursos, pero también traemos al Profesor y la Carrera para mostrar información completa.
# 2. Hacemos JOIN secuenciales: Recurso -> Profesor -> Carrera -> Facultad
# 3. Filtramos por el nombre de la facultad.
resultados = session.query(RecursoAcademico) \
    .join(Profesor) \
    .join(Carrera) \
    .join(Facultad) \
    .filter(Facultad.nombre == nombre_facultad_buscada) \
    .all()

# Verificamos si hay resultados
if resultados:
    for recurso in resultados:
        print(f"- Recurso: {recurso.titulo} ({recurso.tipo})")
        print(f"   -> Autor: {recurso.profesor.nombres} {recurso.profesor.apellidos}")
        print(f"   -> Carrera: {recurso.profesor.carrera.nombre}")
        print(f"   -> URL: {recurso.url}")
        print("-" * 50)
else:
    print(f"No se encontraron recursos académicos asociados a la {nombre_facultad_buscada}.")

# Cerrar la sesión
session.close()