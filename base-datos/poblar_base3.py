import json
from sqlalchemy.orm import sessionmaker
from crear_base_entidades import engine, Carrera, Profesor

Session = sessionmaker(bind=engine)
session = Session()

# Tercero, insertamos los Profesores, asegurándonos de asignar correctamente la relación con Carrera

try:
    print("Iniciando carga de Profesores...")
    with open('data/datos_universidad/datos/profesores.json', 'r', encoding='utf-8') as f:
        datos = json.load(f)
        
    if isinstance(datos, dict):
        datos = [datos]

    for item in datos:
        correo = item['correo'].strip()
        
        if not session.query(Profesor).filter_by(correo=correo).first():
            # 1. Obtenemos el objeto Carrera
            obj_carrera = session.query(Carrera).filter_by(nombre=item['carrera'].strip()).first()

            # 2. Creamos al Profesor asignando el objeto
            nuevo_profesor = Profesor(
                nombres=item['nombres'].strip(),
                apellidos=item['apellidos'].strip(),
                correo=correo,
                especialidad=item['especialidad'].strip(),
                carrera=obj_carrera  # Asignación por objeto
            )
            session.add(nuevo_profesor)
            
    session.commit()
    print("[OK] Profesores agregados exitosamente.")
except Exception as e:
    session.rollback()
    print(f"[ERROR] Ocurrió un problema: {e}")
finally:
    session.close()