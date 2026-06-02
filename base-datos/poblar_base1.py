import json
from sqlalchemy.orm import sessionmaker
from crear_base_entidades import engine, Facultad

Session = sessionmaker(bind=engine)
session = Session()

# Primero cargamos los datos de Facultades para asegurar las relaciones posteriores

try:
    print("Iniciando carga de Facultades...")
    with open('data/datos_universidad/datos/facultades.json', 'r', encoding='utf-8') as f:
        datos = json.load(f)
        
    # Validamos si es un solo diccionario o una lista de diccionarios
    if isinstance(datos, dict):
        datos = [datos]

    for item in datos:
        nombre = item['nombre'].strip()
        
        # Validamos que no exista para evitar duplicados
        if not session.query(Facultad).filter_by(nombre=nombre).first():
            nueva_facultad = Facultad(
                nombre=nombre,
                ubicacion=item['ubicacion'].strip(),
                decano=item['decano'].strip()
            )
            session.add(nueva_facultad)
            
    session.commit()
    print("[OK] Facultades agregadas exitosamente.")
except FileNotFoundError:
    print("[ERROR] Archivo facultades.json no encontrado en data/data_universidad/")
except Exception as e:
    session.rollback()
    print(f"[ERROR] Ocurrió un problema: {e}")
finally:
    session.close()