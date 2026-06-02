import json
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from crear_base_entidades import engine, Profesor, RecursoAcademico

Session = sessionmaker(bind=engine)
session = Session()

# Finalmente, insertamos los Recursos Académicos, asegurándonos de asignar correctamente la relación con Profesor

try:
    print("Iniciando carga de Recursos Académicos...")
    with open('data/datos_universidad/datos/recursos_academicos.json', 'r', encoding='utf-8') as f:
        datos = json.load(f)
        
    if isinstance(datos, dict):
        datos = [datos]

    for item in datos:
        titulo = item['titulo'].strip()
        
        if not session.query(RecursoAcademico).filter_by(titulo=titulo).first():
            # 1. Procesar el nombre del profesor ("Ana Romero" -> ["Ana", "Romero"])
            nombre_completo = item['profesor'].strip().split()
            nombre_prof = nombre_completo[0]
            apellido_prof = " ".join(nombre_completo[1:]) if len(nombre_completo) > 1 else ""

            # 2. Consultamos al profesor coincidiendo nombres y apellidos
            obj_profesor = session.query(Profesor).filter_by(
                nombres=nombre_prof, 
                apellidos=apellido_prof
            ).first()

            # 3. Procesar la fecha (String -> Objeto Date)
            fecha_str = item['fecha_publicacion'].strip()
            fecha_obj = datetime.strptime(fecha_str, '%Y-%m-%d').date()

            # 4. Crear el recurso asignando el objeto
            nuevo_recurso = RecursoAcademico(
                titulo=titulo,
                fecha_publicacion=fecha_obj,
                tipo=item['tipo'].strip(),
                url=item['url'].strip(),
                profesor=obj_profesor  # Asignación por objeto
            )
            session.add(nuevo_recurso)
            
    session.commit()
    print("[OK] Recursos Académicos agregados exitosamente.")
except Exception as e:
    session.rollback()
    print(f"[ERROR] Ocurrió un problema: {e}")
finally:
    session.close()