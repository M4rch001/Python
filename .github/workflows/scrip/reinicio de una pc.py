import os

def reiniciar_pc():
    if os.name == 'nt':  # Verificar si el sistema operativo es Windows
        os.system('shutdown /r /t 0')  # Reiniciar la PC en Windows
    elif os.name == 'posix':  # Verificar si el sistema operativo es Linux o macOS
        os.system('sudo reboot')  # Reiniciar la PC en Linux o macOS

reiniciar_pc()