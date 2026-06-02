from sqlalchemy.orm import sessionmaker
from crear_base_entidades import engine, Profesor

# Configuración de la sesión
Session = sessionmaker(bind=engine)
session = Session()

# ==============================================================================
# 3. Función: filter()
# Propósito: Filtrar registros en base a una condición simple.
# ==============================================================================
print("3. Ejemplo con filter() -> Buscar al profesor Ana Romero:")
# Nota: filter() permite usar operadores de Python como ==, >, <, !=
profesor_filtrado = session.query(Profesor).filter(Profesor.nombres == "Ana").first()

if profesor_filtrado:
    print(f" - Profesor encontrado: {profesor_filtrado.nombres} {profesor_filtrado.apellidos} | Especialidad: {profesor_filtrado.especialidad}")
else:
    print(" - Profesor no encontrado.")

# Cerrar la sesión
session.close()