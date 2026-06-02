from sqlalchemy.orm import sessionmaker
from crear_base_entidades import engine, Carrera

# Configuración de la sesión
Session = sessionmaker(bind=engine)
session = Session()

# ==============================================================================
# 1. Función: all()
# Propósito: Traer todos los registros de una tabla sin ningún filtro.
# ==============================================================================
print("1. Ejemplo con all() -> Listar todas las carreras:")
carreras = session.query(Carrera).all()

for carrera in carreras:
    print(f" - {carrera.nombre} (Código: {carrera.codigo}) / Facultad: {carrera.facultad.nombre}")
