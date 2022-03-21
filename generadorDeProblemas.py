from random import randint
print('''
        Opciones:
        1 - Motores
        2 - Máquinas térmicas
        3 - Máquinas frigoríficas
        ''')
opcion = input('Introduzca una opción:\n')
# opcion = '3'

if opcion == str(1):
    # Código para problemas de motores
    print('')
elif opcion == str(2):
    # Código para problemas de máquinas térmicas
    print('')
elif opcion == str(3):
    print('Escriba q1 para el calor del foco caliente, t1 para la temperatura del foco caliente, q2 para la temperatura del foco frío, t2 para la temperatura del foco caliente y wo para el trabajo.')
    problema = input('Introduzca la plantilla del problema:\n')
    # problema = 'dasfafsd q1 asdfasdf'
    if 'q1' in problema:
        q1 = 101
        while q1 % 100 != 0:
            q1 = randint(500, 20000)
        problema = problema.replace('q1', str(q1))
    print(problema)
    
