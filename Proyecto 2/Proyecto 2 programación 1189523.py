class Barco:
    def __init__(self, nombre, longitud):
        self.nombre = nombre
        self.longitud = longitud
        self.casillas = []

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.barcos = []
        self.tablero = [[' ' for _ in range(10)] for _ in range(10)]

    def convertir_coordenada(self, coordenada):
        letra = coordenada[0].upper()
        if len(coordenada) == 3 and coordenada[1:] == "10":
            fila = 9  # Cambiar el número 10 a 9 para que sea un índice válido
        else:
            fila = int(coordenada[1:]) - 1
        columna = ord(letra) - ord('A')
        return fila, columna

    def colocar_barco(self, barco, coordenada, orientacion):
        fila, columna = self.convertir_coordenada(coordenada)

        if fila < 0 or fila >= 10:
            return False  # Coordenada no válida

        if orientacion == "H":
            for _ in range(barco.longitud):
                if columna >= 10 or self.tablero[fila][columna] != ' ':
                    return False
                barco.casillas.append((fila, columna))
                self.tablero[fila][columna] = 'X'
                columna += 1
        elif orientacion == "V":
            for _ in range(barco.longitud):
                if fila >= 10 or self.tablero[fila][columna] != ' ':
                    return False
                barco.casillas.append((fila, columna))
                self.tablero[fila][columna] = 'X'
                fila += 1
        return True

    def disparar(self, coordenada, tablero_oponente):
        fila, columna = self.convertir_coordenada(coordenada)

        if fila is None:
            return "Fallo"  # Coordenada no válida

        for barco in tablero_oponente.barcos:
            if (fila, columna) in barco.casillas:
                barco.casillas.remove((fila, columna))
                if not barco.casillas:
                    return "Hundido"
                return "Impacto"
        return "Fallo"

    def tiene_barcos_en_pie(self):
        return any(barco.casillas for barco in self.barcos)

class JuegoBatallaNaval:
    def __init__(self):
        self.jugadores = [Jugador("Jugador 1"), Jugador("Jugador 2")]

    def jugar(self):
        for jugador in self.jugadores:
            self.colocar_barcos(jugador)

        jugador_actual = 0
        while True:
            oponente = 1 - jugador_actual

            coordenada = input(f"{self.jugadores[jugador_actual].nombre}, ingresa una coordenada para disparar (por ejemplo, A5): ").upper()
            resultado = self.jugadores[oponente].disparar(coordenada, self.jugadores[oponente])

            if resultado == "Hundido":
                print(f"¡{self.jugadores[jugador_actual].nombre} hundió un barco!")
            elif resultado == "Impacto":
                print(f"¡{self.jugadores[jugador_actual].nombre} impactó un barco!")
            elif resultado == "Fallo":
                print(f"{self.jugadores[jugador_actual].nombre} falló el disparo.")

            if not self.jugadores[oponente].tiene_barcos_en_pie():
                print(f"{self.jugadores[jugador_actual].nombre} gana!")
                break

            jugador_actual = oponente

    def colocar_barcos(self, jugador):
        barcos = [
            Barco("Barco 1 (3 casillas)", 3),
            Barco("Barco 2 (3 casillas)", 3),
            Barco("Barco 3 (3 casillas)", 3),
            Barco("Barco 4 (5 casillas)", 5),
            Barco("Barco 5 (5 casillas)", 5)
        ]

        for barco in barcos:
            while True:
                coordenada = input(f"{jugador.nombre}, coloca tu {barco.nombre} (por ejemplo, A5) y la orientación (H para horizontal, V para vertical): ").upper()
                orientacion = input("Ingresa la orientación (H para horizontal, V para vertical): ").upper()
                if jugador.colocar_barco(barco, coordenada, orientacion):
                    jugador.barcos.append(barco)
                    break

if __name__ == "__main__":
    juego = JuegoBatallaNaval()
    juego.jugar()
