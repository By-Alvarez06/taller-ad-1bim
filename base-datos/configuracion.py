# ==============================================================================
# OPCIÓN 1: Conexión a PostgreSQL
# Motor: postgres:16
# Puerto expuesto al host: 5434
# Usuario: user | Password: password
# ==============================================================================
# Formato: postgresql+driver://usuario:password@host:puerto/nombre_bd
cadena_base_datos_postgres = 'postgresql+psycopg2://user:password@localhost:5434/universidad'


# ==============================================================================
# OPCIÓN 2: Conexión a MariaDB
# Motor: mariadb:11
# Puerto expuesto al host: 3308
# Usuario: root | Password: rootpassword
# ==============================================================================
# Formato: mysql+driver://usuario:password@host:puerto/nombre_bd?charset=utf8mb4
cadena_base_datos_mariadb = 'mysql+pymysql://root:rootpassword@localhost:3308/universidad?charset=utf8mb4'

cadena_base_datos = cadena_base_datos_postgres  # Cambiar variable segun el motor a ocupar