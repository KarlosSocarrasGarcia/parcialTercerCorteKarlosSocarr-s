def gestionarMundial():
    equiposMundial = ("Argentina", "Francia", "Dinamarca", "Tunez")
    grupo = {equipo: {"PJ": 0, "PG": 0, "PE": 0, "PP": 0, "GF": 0, "GC": 0, "PTS": 0} for equipo in equiposMundial}
    while True:
        print("\n 1. Registrar Partido | 2. Mostrar Tabla | 3. Salir ")
        opcionMenu = input("Selecciona una opcion: ")
        if opcionMenu == "1":
            equipoLocal = input("Equipo 1: ")
            equipoVisitante = input("Equipo 2: ")
            if equipoLocal in equiposMundial and equipoVisitante in equiposMundial:
                golesLocal = int(input("Goles de " + equipoLocal + ": "))
                golesVisitante = int(input("Goles de " + equipoVisitante + ": "))
                grupo[equipoLocal]["PJ"], grupo[equipoVisitante]["PJ"] = grupo[equipoLocal]["PJ"] + 1, grupo[equipoVisitante]["PJ"] + 1
                grupo[equipoLocal]["GF"], grupo[equipoLocal]["GC"] = grupo[equipoLocal]["GF"] + golesLocal, grupo[equipoLocal]["GC"] + golesVisitante
                grupo[equipoVisitante]["GF"], grupo[equipoVisitante]["GC"] = grupo[equipoVisitante]["GF"] + golesVisitante, grupo[equipoVisitante]["GC"] + golesLocal
                if golesLocal > golesVisitante:
                    grupo[equipoLocal]["PG"], grupo[equipoLocal]["PTS"], grupo[equipoVisitante]["PP"] = grupo[equipoLocal]["PG"] + 1, grupo[equipoLocal]["PTS"] + 3, grupo[equipoVisitante]["PP"] + 1
                elif golesVisitante > golesLocal:
                    grupo[equipoVisitante]["PG"], grupo[equipoVisitante]["PTS"], grupo[equipoLocal]["PP"] = grupo[equipoVisitante]["PG"] + 1, grupo[equipoVisitante]["PTS"] + 3, grupo[equipoLocal]["PP"] + 1
                else:
                    grupo[equipoLocal]["PE"], grupo[equipoLocal]["PTS"] = grupo[equipoLocal]["PE"] + 1, grupo[equipoLocal]["PTS"] + 1
                    grupo[equipoVisitante]["PE"], grupo[equipoVisitante]["PTS"] = grupo[equipoVisitante]["PE"] + 1, grupo[equipoVisitante]["PTS"] + 1
                print("Partido registrado con exito.")
            else:
                print("Uno o ambos equipos no pertenecen al grupo.")
        elif opcionMenu == "2":
            print("\nEquipo - PJ - PG - PE - PP - GF - GC - DG - PTS")
            tablaPosiciones = [[nombre, grupo[nombre]["PJ"], grupo[nombre]["PG"], grupo[nombre]["PE"], grupo[nombre]["PP"], grupo[nombre]["GF"], grupo[nombre]["GC"], grupo[nombre]["GF"] - grupo[nombre]["GC"], grupo[nombre]["PTS"]] for nombre in grupo]
            for i in range(4):
                for j in range(0, 3 - i):
                    if (tablaPosiciones[j][8] < tablaPosiciones[j+1][8]) or (tablaPosiciones[j][8] == tablaPosiciones[j+1][8] and tablaPosiciones[j][7] < tablaPosiciones[j+1][7]):
                        tablaPosiciones[j], tablaPosiciones[j+1] = tablaPosiciones[j+1], tablaPosiciones[j]
            for fila in tablaPosiciones:
                print(fila[0] + " - " + str(fila[1]) + " - " + str(fila[2]) + " - " + str(fila[3]) + " - " + str(fila[4]) + " - " + str(fila[5]) + " - " + str(fila[6]) + " - " + str(fila[7]) + " - " + str(fila[8]))
        elif opcionMenu == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opcion invalida.")

gestionarMundial()