from Funciones import*
lista=["Juan Pérez","Maria Garcia","Carlos López","Ana Martinez",
       "Pedro Ródriguez","Laura Hernández",
       "Miguel Sánchez","Isabel Gomez","Francisco Días",
       "Elena Fernández"
       ]
lista2=[]

while True:
    print("\nBienvenido Ingrese lo que quiere Hacer\n")

    print(" 1-Asignar Sueldos aleatorios")
    print(" 2-Clasificar sueldos")
    print(" 3-Generar Archivo Csv")
    print(" 4-Ver estadísticas")
    print(" 5-Reporte de sueldos")
    print(" 6-Salir del programa\n")

    opc=v_int(1,6,"Opcion")
    if opc==1:
        empleados(lista2)
        trabajadores=empleados(lista)
        print("Los sueldos ya son aleatorios\n")
    if opc==2:
        opc_2(trabajadores)
    if opc==3:
        opc_3(trabajadores) 
    if opc==4:
        opc_4(trabajadores)
    if opc==5:
        opc_5(trabajadores)
    if opc==6:
        print("Finalizando programa...\nDesarrollado por Pablo Mery\nRut 21.005.183-K")
        break
