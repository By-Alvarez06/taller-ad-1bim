from sqlalchemy import or_
from sqlalchemy.orm import sessionmaker
from crear_base_entidades import engine, RecursoAcademico

# Configuración de la sesión
Session = sessionmaker(bind=engine)
session = Session()

# ==============================================================================
# 4. Función: or_()
# Propósito: Cumplir AL MENOS UNA de varias condiciones.
# ==============================================================================
print("4. Ejemplo con or_() -> Recursos que sean tipo 'Libro' o tipo 'Video':")
recursos_or = session.query(RecursoAcademico).filter(
    or_(
        RecursoAcademico.tipo == "Libro",
        RecursoAcademico.tipo == "Video"
    )
).all()

for rec in recursos_or:
    print(f" - {rec.titulo} | Clasificación: {rec.tipo}")

# Cerrar la sesión
session.close()