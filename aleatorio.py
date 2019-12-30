import random

def run():

    print('*_*_*_*_*_*_*_*_*_*_*_*_*_*_*')
    print('_____ADIVINA CON ZABALA_____')
    print('*_*_*_*_*_*_*_*_*_*_*_*_*_*_*')
    print(' ')
    name = input('¿Cuál es tu nombre?: ')
    print(' ')
    print('Hola {}, este es un juego interactivo de adivinanzas donde tu tendrás que adivinar un número aleatorio que será establecido por la máquina, también determinarás los parámetros de los número del rango y máximo de intentos que estás dispuesto a hacer para encontrar el número, buena suerte {}.'.format(name, name))
    print(' ')
    print('1) Escribe el rango de los números(El mayor y el menor)')
    min_num = int(input('   Escribe el menor número: '))
    max_num = int(input('   Escribe el mayor número: '))
    print(' ')
    number_found = False
    r_number = random.randint(min_num, max_num)
    intentos = 1
    print('2) Escribe el máximo de intentos que quieres tener para adivinar el número')
    max_intentos = int (input('   Escribe el máximo de intentos: '))
    print(' ')

    #Aquí comienza el bucle WHILE

    while number_found is False and intentos <= max_intentos:
        intentos_restantes = max_intentos - intentos

        number = int(input('Intenta adivinar un número entre el {} y el {}: '.format(min_num, max_num)))

        if number == r_number:
            print('*_*_*_*_*_*_*_*_*_*_*_*_*_*_*')
            print('Felicidades {}, haz encontrado el número {} con {} intento(s)'.format(name, r_number, intentos))
            print('*_*_*_*_*_*_*_*_*_*_*_*_*_*_*')
            number_found = True
        elif number > r_number:
            print(' ')
            print('El número que debes encontrar es menor que {}, llevas {} intentos, te quedan {} {}.'.format(number, intentos, intentos_restantes, name))
            print(' ')
            intentos += 1
        else:
            print(' ')
            print('El número que debes encontrar es mayor que {}, llevas {} intentos, te quedan {} {}.'.format(number, intentos, intentos_restantes, name))
            print(' ')
            intentos += 1

    if number_found is True and intentos <= max_intentos:
         print('_________LO LOGRASTE_________')
         print('*_*_*_*_*_*_*_*_*_*_*_*_*_*_*')
    else:
         print('Haz fallado el reto {}, no pudiste completarlo con los {} intentos que te propusiste, el número a adivinar era {}.'.format(name, max_intentos, r_number))

if __name__ == '__main__':
    run()