from sqlalchemy.orm import sessionmaker
from crear_base_entidades import engine, RecursoAcademico

# Configuración de la sesión
Session = sessionmaker(bind=engine)
session = Session()

# ==============================================================================
# 5. Función: order_by()
# Propósito: Ordenar los resultados de la consulta por una columna específica.
# ==============================================================================
print("5. Ejemplo con order_by() -> Listar recursos académicos ordenados por título (Z-A):")
# Usamos .desc() para orden descendente. Si no lo ponemos, por defecto es ascendente.
recursos_ordenados = session.query(RecursoAcademico).order_by(RecursoAcademico.titulo.desc()).all()

for recurso in recursos_ordenados:
    print(f" - {recurso.titulo} | Tipo: {recurso.tipo} | Publicado: {recurso.fecha_publicacion}")

# Cerrar la sesión
session.close()