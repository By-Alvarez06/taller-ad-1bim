# importamos la función and_ para consultas con múltiples condiciones
from sqlalchemy import and_
from sqlalchemy.orm import sessionmaker
from crear_base_entidades import engine, Profesor

# Configuración de la sesión
Session = sessionmaker(bind=engine)
session = Session()

# ==============================================================================
# 2. Función: and_()
# Propósito: Cumplir MÚLTIPLES condiciones estrictas al mismo tiempo.
# ==============================================================================
print("2. Ejemplo con and_() -> Profesores de especialidad 'Bases de Datos' que tienen una 'a' en su nombre:")
profesores_and = session.query(Profesor).filter(
    and_(
        Profesor.especialidad == "Bases de Datos",
        Profesor.nombres.like("%a%") # .like() busca coincidencias parciales
    )
).all()

for prof in profesores_and:
    print(f" - {prof.nombres} {prof.apellidos} | Correo: {prof.correo}")

# Cerrar la sesión
session.close()