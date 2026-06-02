import json
from sqlalchemy.orm import sessionmaker
from crear_base_entidades import engine, Facultad, Carrera

Session = sessionmaker(bind=engine)
session = Session()

# Segundo, insertamos las Carreras, asegurándonos de asignar correctamente la relación con Facultad

try:
    print("Iniciando carga de Carreras...")
    with open('data/datos_universidad/datos/carreras.json', 'r', encoding='utf-8') as f:
        datos = json.load(f)
        
    if isinstance(datos, dict):
        datos = [datos]

    for item in datos:
        nombre = item['nombre'].strip()
        
        if not session.query(Carrera).filter_by(nombre=nombre).first():
            # 1. Obtenemos el objeto Facultad consultando por su nombre
            obj_facultad = session.query(Facultad).filter_by(nombre=item['facultad'].strip()).first()

            # 2. Creamos la carrera asignando el objeto
            nueva_carrera = Carrera(
                nombre=nombre,
                codigo=item['codigo'].strip(),
                facultad=obj_facultad  # Asignación por objeto
            )
            session.add(nueva_carrera)
            
    session.commit()
    print("[OK] Carreras agregadas exitosamente.")
except Exception as e:
    session.rollback()
    print(f"[ERROR] Ocurrió un problema: {e}")
finally:
    session.close()