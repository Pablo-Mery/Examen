from csv import writer  
def v_int(mini,maxi,texto):
    try:
        num =int(input(f"Ingrese {texto} que desea: "))
        if mini < num and num > maxi:
            print ("Valor No valido")
        else:
            return num
    except:
        print("Caracter no valido")
                
def empleados(lista):
    sueldo=0
    trabajadores =[
               ("Juan Pérez", 1000000),
               ("Maria Garcia", 2500000),
               ("Carlos López", 300000),
               ("Ana Martinez", 500000),
               ("Pedro Ródriguez", 300000),
               ("Laura Hernández", 1000000),
               ("Miguel Sánchez", 700000),
               ("Isabel Gomez", 1200000),
               ("Francisco Días", 2000000),
               ("Elena Fernández", 1500000)
               ]
    return trabajadores
def opc_2(Lista):
    con=0
    con1=0
    con2=0
    trabajadores = Lista
    Menos=[]
    Entre=[]
    mayor=[]
    Total=0
    for i in trabajadores:
        if int(i[1]) < 800000:
            con+=1
            Menos.append(i)
        if 800000 <= int(i[1]) and int(i[1]) <=2000000:
            con1+=1
            Entre.append(i)
        if int(i[1]) > 2000000:
            con2+=1
            mayor.append(i)
        Total=Total+int(i[1])
    print(f"Sueldo Menores a $800.000 Total: {con}\n")
    print("Nombre Empleado         Sueldo")
    for i in Menos:
        pero=24-len(i[0])
        print(f"{i[0]}"+" "*pero+f"{i[1]}")
    print(f"\nSueldo entre $800.000 y 2000000 \nTotal: {con1}\n")
    
    print("Nombre Empleado         Sueldo")
    for i in Entre:
        pero=24-len(i[0])
        print(f"{i[0]}"+" "*pero+f"{i[1]}")
        
    print(f"\nSueldos Superiores a 2000000 \nTotal: {con2}\n")
    print("Nombre Empleado         Sueldo")
    for i in mayor:
        pero=24-len(i[0])
        print(f"{i[0]}"+" "*pero+f"{i[1]}")

    print(f"\nTotal Sueldos:     ${Total}")
    
def opc_3 (lista):
    """
    with "sueldos_personal.csv", "w" as csv_files:
        cvs_file.csvwriter(lista)
    """
def opc_4 (lista):
    trabajadores=lista
    sueldos=[]
    Promedio=0
    for i in trabajadores:
        sueldos.append(i[1])
    for i in sueldos:
        Promedio=Promedio+i
    print(f"\nEl sueldo Mas altos es: {max(sueldos)}\n")
    print(f"El sueldo Más bajo es: {min(sueldos)}\n")
    print("El Promedio de los sueldo es:", round(Promedio/10))    
def opc_5(lista):
    trabajadores=lista
    sueldos=[]
    for i in trabajadores:
        sueldos.append(i[1])
    print("Nombre empleado     Sueldo Base      Descuento Salud   Descuento AFP   Sueldo Liquido")
    for i in trabajadores:
        pero=20-len((i[0]))
        talta=16-len(str(i[1]))
        otro=16-len(str(round((i[1])*0.07)))
        pera=14-len(str(round((i[1])*0.12)))
        Total=round((i[1])-((i[1])*0.07)-((i[1])*0.12))
        print(f"{(i[0])}"+" "*pero+f"{(i[1])}"+" "*talta,round((i[1])*0.07)," "*otro,round((i[1])*0.12)," "*pera,  Total)

