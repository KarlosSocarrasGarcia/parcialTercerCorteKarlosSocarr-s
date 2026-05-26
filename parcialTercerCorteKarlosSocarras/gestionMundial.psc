Algoritmo GestionarMundial
    Definir i, j, op, eq1, eq2, g1, g2, t Como Entero
    Definir pts, dg Como Entero; Dimension pts[4], dg[4]
    Mientras op <> 3 Hacer
        Escribir "1. Registrar Partido | 2. Mostrar Tabla | 3. Salir"
        Leer op
        Si op = 1 Entonces
            Escribir "Elija Equipos (1:Arg, 2:Fra, 3:Din, 4:Tun) y sus Goles:"
            Leer eq1, eq2, g1, g2
            Si eq1 >= 1 Y eq1 <= 4 Y eq2 >= 1 Y eq2 <= 4 Y eq1 <> eq2 Entonces
                dg[eq1] <- dg[eq1] + (g1 - g2)
                dg[eq2] <- dg[eq2] + (g2 - g1)
                Si g1 > g2 Entonces
                    pts[eq1] <- pts[eq1] + 3
                Sino
                    Si g2 > g1 Entonces
                        pts[eq2] <- pts[eq2] + 3
                    Sino
                        pts[eq1] <- pts[eq1] + 1
                        pts[eq2] <- pts[eq2] + 1
                    FinSi
                FinSi
            Sino
                Escribir "Equipos invalidos."
            FinSi
        FinSi
        Si op = 2 Entonces
            Definir orden Como Entero; Dimension orden[4]
            Para i <- 1 Hasta 4 Hacer
                orden[i] <- i
            FinPara
            Para i <- 1 Hasta 4 Hacer
                Para j <- 1 Hasta 3 Hacer
                    Si (pts[orden[j]] < pts[orden[j+1]]) O (pts[orden[j]] = pts[orden[j+1]] Y dg[orden[j]] < dg[orden[j+1]]) Entonces
                        t <- orden[j]
                        orden[j] <- orden[j+1]
                        orden[j+1] <- t
                    FinSi
                FinPara
            FinPara
            Escribir "Eq - DG - PTS"
            Para i <- 1 Hasta 4 Hacer
                j <- orden[i]
                Escribir j, "   ", dg[j], "    ", pts[j]
            FinPara
        FinSi
    FinMientras
FinAlgoritmo