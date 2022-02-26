import random
import names

class Estudiantes:
    n_alumnos = random.randint(2,10)
    print(n_alumnos)
    alumnos = []


    for i in range (1, n_alumnos):
        name = names.get_full_name()
        alumnos.append(name)

    for x in alumnos:
        print (x)

clase = Estudiantes()