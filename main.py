import random
import os
import statistics

# https://github.com/BenjaLuengo-Voltyk/BENJAMIN_LUENGO_FPY1101_003D

trabajadores = ["Juan Perez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", "Laura Hernandez", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

def menu():
    os.system("cls")
    print(f"""
    Seleccione qué desea hacer en el programa (1-5):
    1.- Asignar sueldos aleatorios
    2.- Clasificar sueldos
    3.- Ver estadísticas
    4.- Reporte de sueldos
    5.- Salir del programa
          """)
    opt = input("    Opción seleccionada: ")
    
    while opt not in ["1", "2", "3", "4", "5"]:
        os.system("cls")
        print(f"""
    Opción inválida. Por favor seleccione una de las siguientes opciones:
    1.- Asignar sueldos aleatorios
    2.- Clasificar sueldos
    3.- Ver estadísticas
    4.- Reporte de sueldos
    5.- Salir del programa
              """)
        opt = input("    Opción seleccionada: ")

    return opt

def asignar_sueldos():
    print("    Asignando sueldos aleatorios...\n")
    global sueldos_ran
    sueldos_ran = []
    for i in range(10):
        
        ran = random.randint(300_000, 2_500_000)
    
        sueldos_ran.append(ran)

    global sueldos_asig
        
    sueldos_asig = []
    for i in range(len(trabajadores)):

        sueldos_asig.append(trabajadores[i])
        sueldos_asig.append(sueldos_ran[i])
    
    print("    Presione ENTER para continuar")
    input()

def clasificar_sueldos():
    sueldos_ran.sort()

    cant_men800k = 0
    cant_may800k = 0
    cant_2mil = 0

    total = 0

    for i in range(len(sueldos_ran)):
        total += sueldos_ran[i]

    for i in range(len(trabajadores)):
        if sueldos_ran[i] < 800_000:
            cant_men800k += 1
        elif sueldos_ran[i] >= 800_000 and sueldos_ran[i] < 2_000_000:
            cant_may800k += 1
        else:
            cant_2mil += 1

    print(f"""
    Sueldos menores a $800.000 
    TOTAL: {cant_men800k}
          
    Nombre empleado   Sueldo""")
    for i in range(len(trabajadores)):
        if sueldos_ran[i] < 800_000:
            print(f"""    {trabajadores[i]}     {sueldos_ran[i]}""")

    print(f"""
    Sueldos entre $800.000 y $2.000.000 
    TOTAL: {cant_may800k}
          
    Nombre empleado   Sueldo""")
    for i in range(len(trabajadores)):
        if sueldos_ran[i] > 800_000 and sueldos_ran[i] < 2_000_000:
            print(f"""    {trabajadores[i]}     {sueldos_ran[i]}""")

    print(f"""
    Sueldos superiores a $2.000.000 
    TOTAL: {cant_2mil}
          
    Nombre empleado   Sueldo""")
    for i in range(len(trabajadores)):
        if sueldos_ran[i] > 2_000_000:
            print(f"""    {trabajadores[i]}     {sueldos_ran[i]}""")
    
    print(f"""
    TOTAL SUELDOS: ${total}
          """)

    print("    Presione ENTER para continuar")
    input()

def ver_estadisticas():
    sueldos_ran.sort(reverse=True)
    mayor = sueldos_ran[0]

    sueldos_ran.sort()
    menor = sueldos_ran[0] 

    total = 0

    for i in range(len(sueldos_ran)):
        total += sueldos_ran[i]

    prom = total / len(sueldos_ran)
    
    geo = statistics.geometric_mean(sueldos_ran)

    print(f"""
    Sueldo más alto: {round(mayor)}
    Sueldo más bajo: {round(menor)}
    Promedio de sueldos: {round(prom)}
    Media geométrica: {round(geo)}
          """)
    
    print("    Presione ENTER para continuar")
    input()

def reporte_sueldos():
    desc_salud = []
    desc_afp = []
    sueldo_liq = []

    for i in range(len(sueldos_ran)):
        salud = sueldos_ran[i] * 0.07
        desc_salud.append(round(salud))

        afp = sueldos_ran[i] * 0.12
        desc_afp.append(round(afp))

    for i in range(len(sueldos_ran)):
        liq = sueldos_ran[i] - (desc_salud[i] + desc_afp[i])
        sueldo_liq.append(round(liq))

    print(f"""
    Nombre empleado     Sueldo Base     Descuento Salud     Descuento AFP   Sueldo Líquido""")

    for i in range(len(trabajadores)):
        print(f"""    {trabajadores[i]}         {sueldos_ran[i]}            {desc_salud[i]}          {desc_afp[i]}             {sueldo_liq[i]}""")
        
        with open("reporte.csv", "+a") as archivo:
            archivo.write(f"{trabajadores[i]},{sueldos_ran[i]},{desc_salud[i]},{desc_afp[i]},{sueldo_liq[i]}\n")
    
    print("    Presione ENTER para continuar")
    input()

def salir():
    os.system("cls")
    print("Finalizando programa...")
    print("Desarrollado por Benjamin Luengo")
    print("RUT 21.391.676-9")

while True:
    opt = menu()
    match opt:
        case "1":
            asignar_sueldos()
        case "2":
            clasificar_sueldos()
        case "3":
            ver_estadisticas()
        case "4":
            reporte_sueldos()
        case "5":
            salir()
            break