import time
personas = [{"name": "Juan", "age": 20, "prom": 7}, 
            {"name": "Tom", "age": 14, "prom": 9}, 
            {"name": "Maria", "age": 35, "prom": 8.4}, 
            {"name": "Julia", "age": 17, "prom": 6.4}]
#nombres = []
welcome = False
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
    print("-----"*3)
    if option == "1":
        for persona in personas:
            for key, values in persona.items():
                print(f"{key} : {values}")
            time.sleep(1)
            print("\n")
        time.sleep(5)

    elif option == "2":
        print("Los nombres son: ")
        for persona in personas:
            for key, values in persona.items():
                if key == "name":
                    print(f"{values}")
                    print("---"*10)
        time.sleep(5)

    elif option == "3":
        for persona in personas:
            for key, values in persona.items():
                if key == "name":
                    name = values
                if key == "age":
                    age = values
            print(f"El usuario {name} tiene {age} años")
            time.sleep(2)
        time.sleep(5)

    elif option == "4":
        for persona in personas:
            for key, values in persona.items():
                if key == "name":
                    name = values
                if key == "prom":
                    prom = values
            print(f"El usuario {name} tiene un promedio de : {prom} ")
            time.sleep(2)
        time.sleep(5)

    elif option == "5":
        prom = []
        for persona in personas:
            for key, values in persona.items():
                if key == "prom":
                    prom.append(values)

        print(f"El promedio de las notas es {sum(prom) / len(prom)}")
           
        time.sleep(5)

    elif option == "6":
        media = []
        for persona in personas:
            for key, values in persona.items():
                if key == "age":
                    media.append(values)

        print(f"El promedio de las edades es {sum(media) / len(media)}")
           
        time.sleep(5)
    elif option == "7":
        break
    else:
        print("No hay ingresado ninguna opción valida")

print("Fin del programa")