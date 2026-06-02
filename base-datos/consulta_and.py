# consultas.py
from sqlalchemy import and_, or_
from sqlalchemy.orm import sessionmaker
from crear_base_entidades import engine, Facultad, Carrera, Profesor, RecursoAcademico

# Configuración de la sesión
Session = sessionmaker(bind=engine)
session = Session()

print("=== INICIANDO CONSULTAS ORM ===\n")

# ==============================================================================
# 1. Función: all()
# Propósito: Traer todos los registros de una tabla sin ningún filtro.
# ==============================================================================
print("1. Ejemplo con all() -> Listar todas las carreras:")
todas_las_carreras = session.query(Carrera).all()

for carrera in todas_las_carreras:
    print(f" - {carrera.nombre} (Código: {carrera.codigo})")
print("-" * 50)


# ==============================================================================
# 2. Función: filter()
# Propósito: Filtrar registros en base a una condición simple.
# ==============================================================================
print("2. Ejemplo con filter() -> Buscar al profesor Ana Romero:")
# Nota: filter() permite usar operadores de Python como ==, >, <, !=
profesor_filtrado = session.query(Profesor).filter(Profesor.nombres == "Ana").first()

if profesor_filtrado:
    print(f" - Profesor encontrado: {profesor_filtrado.nombres} {profesor_filtrado.apellidos} | Especialidad: {profesor_filtrado.especialidad}")
else:
    print(" - Profesor no encontrado.")
print("-" * 50)


# ==============================================================================
# 3. Función: order_by()
# Propósito: Ordenar los resultados de la consulta por una columna específica.
# ==============================================================================
print("3. Ejemplo con order_by() -> Listar recursos académicos ordenados por título (Z-A):")
# Usamos .desc() para orden descendente. Si no lo ponemos, por defecto es ascendente.
recursos_ordenados = session.query(RecursoAcademico).order_by(RecursoAcademico.titulo.desc()).all()

for recurso in recursos_ordenados:
    print(f" - {recurso.titulo} | Tipo: {recurso.tipo} | Publicado: {recurso.fecha_publicacion}")
print("-" * 50)


# ==============================================================================
# 4. Función: and_()
# Propósito: Cumplir MÚLTIPLES condiciones estrictas al mismo tiempo.
# ==============================================================================
print("4. Ejemplo con and_() -> Profesores de especialidad 'Bases de Datos' que usan correo '@universidad.edu':")
profesores_and = session.query(Profesor).filter(
    and_(
        Profesor.especialidad == "Bases de Datos",
        Profesor.correo.like("%@universidad.edu%") # .like() busca coincidencias parciales
    )
).all()

for prof in profesores_and:
    print(f" - {prof.nombres} {prof.apellidos} | Correo: {prof.correo}")
print("-" * 50)


# ==============================================================================
# 5. Función: or_()
# Propósito: Cumplir AL MENOS UNA de varias condiciones.
# ==============================================================================
print("5. Ejemplo con or_() -> Recursos que sean tipo 'Libro' o tipo 'Video':")
recursos_or = session.query(RecursoAcademico).filter(
    or_(
        RecursoAcademico.tipo == "Libro",
        RecursoAcademico.tipo == "Video"
    )
).all()

for rec in recursos_or:
    print(f" - {rec.titulo} | Clasificación: {rec.tipo}")
print("-" * 50)

# Cerrar la sesión
session.close()
print("=== CONSULTAS FINALIZADAS ===")