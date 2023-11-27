import os

def apagar_computadora():
    # Verificar si el sistema operativo es Windows o Linux
    if os.name == 'nt':  # Windows
        os.system('shutdown /s /t 0')
    elif os.name == 'posix':  # Linux
        os.system('shutdown now')

# Llamar a la función para apagar la computadora
apagar_computadora()