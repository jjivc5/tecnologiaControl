import time
personas = [{"name": "Juan", "age": 20, "prom": 7}, 
            {"name": "Tom", "age": 14, "prom": 9}, 
            {"name": "Maria", "age": 35, "prom": 8.4}, 
            {"name": "Julia", "age": 17, "prom": 6.4}]

welcome = False
pause_time = 1


def process_entries(entry, handler):
    for data in entry:
        for key, value in data.items():
            handler(key, value)
        print("-"*30)
        time.sleep(1)
        

def show_all_entries(entry):
    def handler(key, value):
        print(f"{key} : {value}")
    process_entries(entry, handler)
    time.sleep(pause_time)

def show_only_names(entry):
    print("Los nombres son: \n")
    def handler(key, value):
        if key == "name":
            print(f"{value}")
    process_entries(entry, handler)

name = ""
age = 0
def show_names_ages(entry):
    def handler(key, value):
        if key == "name":
            name = value
        if key == "age":
            age = value
        print(f"El usuario {name} tiene un promedio de : {age} ")
    process_entries(entry, handler)
    time.sleep(pause_time)
while True:
    if welcome == False:
        print("Bienvenido al programa integrador \n")
        print("-"*20)
    welcome = True
    print("Seleccione una opción")
    print('''
          1. Mostrar todos los datos de las personas.
          2. Mostrar todos los nombres de las personas.
          3. Mostrar las edades de las personas, indicando el nombre.
          4. Mostrar el promedio de las personas, indicando el nombre.
          5. Calcular el promedio de los promedios de las notas.
          6. Calcular la media de las edades
          7. Salir
''')
    option = input("Ingrese la opción --> ")
    print("-----"*10)
    if option == "1":
        show_all_entries(personas)
        

    elif option == "2":
        show_only_names(personas)

    elif option == "3":
        show_names_ages(personas)

    elif option == "4":
        for persona in personas:
            for key, values in persona.items():
                if key == "name":
                    name = values
                if key == "prom":
                    prom = values
            print(f"El usuario {name} tiene un promedio de : {prom} ")
            time.sleep(2)
        time.sleep(pause_time)

    elif option == "5":
        prom = []
        for persona in personas:
            for key, values in persona.items():
                if key == "prom":
                    prom.append(values)

        print(f"El promedio de las notas es {sum(prom) / len(prom)}")
           
        time.sleep(pause_time)

    elif option == "6":
        media = []
        for persona in personas:
            for key, values in persona.items():
                if key == "age":
                    media.append(values)

        print(f"El promedio de las edades es {sum(media) / len(media)}")
           
        time.sleep(pause_time)
    elif option == "7":
        break
    else:
        print("No hay ingresado ninguna opción valida")

print("Fin del programa")