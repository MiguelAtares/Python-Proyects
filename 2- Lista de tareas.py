# El objetivo es crear una lista de tareas


#Mostrar la lista inicial de tareas y días de la semana

tareas_diarias =["Blink", "Programar", "Writing", "Duolingo", "Speak", "Cuadernillo C1", "Curso"]
day_of_week = ["lunes", "martes", "miercoles","jueves", "viernes", "sabado","domingo"]
while True:
    insert_day = input("¿Qué día de la semana es hoy?:").lower()
    if insert_day in day_of_week:
        break
    else:
        print("Día incorrecto. Por favor, ingresa un día válido de la semana:")

#Funcionamiento del código

#Día entre semana:

if insert_day in ["lunes", "martes", "miercoles", "jueves", "viernes"]:
    print("Recuerda, tienes que hacer:")
    for tarea in tareas_diarias:
        print(tarea)
    while True:
        nueva_tarea = input("¿Quieres añadir alguna nueva tarea para hoy? Escribe 'Si' / 'No' :").lower()
        if nueva_tarea == "si":
            while True:
                nueva_tarea = input("Añade las tareas (o pulsa 'salir' si no quieres añadir más):").lower()
                if nueva_tarea == "salir":
                    break  
                tareas_diarias.append(nueva_tarea)
                print(f"Has añadido la tarea: {nueva_tarea}")
            print("Lista de tareas actualizadas:")
            for tarea in tareas_diarias:
                print(tarea)
            break
    
        elif nueva_tarea == "no":
         print("Perfecto, tu lista definitiva de tareas hoy es:")
         for tarea in tareas_diarias:
             print(tarea)
         break

        else:
            print("No te he entendido, ¿'si' o 'no'?:")

#Sábado:
elif insert_day == "sabado":
    tareas_diarias.insert(0,"Poner la lavadora")
    tareas_diarias.pop(1)
    print("Hoy es sábado! Recuerda, tienes que hacer:")
    for tarea in tareas_diarias:
        print(tarea)
    while True:
        nueva_tarea = input("¿Quieres añadir alguna nueva tarea para hoy? Escribe 'Si' / 'No' :").lower()
        if nueva_tarea == "si":
            while True:
                nueva_tarea = input("Añade las tareas (o pulsa 'salir' si no quieres añadir más):").lower()
                if nueva_tarea == "salir":
                    break  
                tareas_diarias.append(nueva_tarea)
                print(f"Has añadido la tarea: {nueva_tarea}")
            print("Lista de tareas actualizadas:")
            for tarea in tareas_diarias:
                print(tarea)
            break
    
        elif nueva_tarea == "no":
         print("Perfecto, tu lista definitiva de tareas hoy es:")
         for tarea in tareas_diarias:
             print(tarea)
         break

        else:
            print("No te he entendido, ¿'si' o 'no'?:")

#Domingo:
elif insert_day == "domingo":
    print("Hoy es día de descanso, no te dejo añadir tareas!")


    






