from datetime import datetime

# Obtener las fechas del usuario
fecha1 = input("Ingrese la primera fecha (formato: dd/mm/aaaa): ")
fecha2 = input("Ingrese la segunda fecha (formato: dd/mm/aaaa): ")

# Convertir las fechas a objetos de tipo datetime
fecha1 = datetime.strptime(fecha1, "%d/%m/%Y")
fecha2 = datetime.strptime(fecha2, "%d/%m/%Y")

# Calcular la diferencia entre las fechas
diferencia = fecha2 - fecha1

# Obtener los componentes de la diferencia en días, meses y años
dias = diferencia.days
meses = dias // 30  # Aproximación a meses considerando 30 días por mes
anios = meses // 12  # Aproximación a años considerando 12 meses por año

# Imprimir la diferencia en días, meses y años
print("La diferencia es de:")
print("Días:", dias)
print("Meses:", meses)
print("Años:", anios)