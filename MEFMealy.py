
# =====================================================
# MAQUINA EXPENDEDORA
# Maquina de Estados Finitos de Mealy
# =====================================================


# -----------------------------------------------------
# 1. CONJUNTO DE ESTADOS Q
# -----------------------------------------------------

Q = set()

# Estados de saldo: S0 hasta S29
for b in range(30):
    Q.add(f"S{b}")

# Estados de dispensacion del producto 1
for c in range(20):
    Q.add(f"D1_{c}")

# Estados de dispensacion del producto 2
for c in range(15):
    Q.add(f"D2_{c}")

# Estados de dispensacion del producto 3
for c in range(10):
    Q.add(f"D3_{c}")


# -----------------------------------------------------
# 2. ALFABETO DE ENTRADA SIGMA
# -----------------------------------------------------

Sigma = {
    "A", "B", "C", "D",
    "P1", "P2", "P3",
    "CANCELAR", "SE"
}


# -----------------------------------------------------
# 3. ESTADO INICIAL
# -----------------------------------------------------

q0 = "S0"


# -----------------------------------------------------
# 4. TABLA DE TRANSICIONES T
# -----------------------------------------------------

T = {}

# Inicializar las 675 transiciones.
# Toda combinacion comienza con un bucle
# que conserva el estado y produce Esperar.

for q in Q:
    for a in Sigma:
        T[(q, a)] = (q, "Esperar")


# -----------------------------------------------------
# 4.1 TRANSICIONES DE MONEDAS
# -----------------------------------------------------

monedas = {
    "A": 1,
    "B": 2,
    "C": 5,
    "D": 10
}

for b in range(30):

    for simbolo, valor in monedas.items():

        if b < 20:
            nuevo_estado = f"S{b + valor}"
            salida = f"MS({b + valor})"

            T[(f"S{b}", simbolo)] = (
                nuevo_estado, salida
            )

        else:
            T[(f"S{b}", simbolo)] = (
                f"S{b}", "RechazarMoneda"
            )


# -----------------------------------------------------
# 4.2 TRANSICIONES DE SELECCION DE PRODUCTOS
# -----------------------------------------------------

precios = {
    "P1": 10,
    "P2": 15,
    "P3": 20
}

for b in range(30):

    for producto, precio in precios.items():

        if b >= precio:

            cambio = b - precio
            nuevo_estado = f"D{producto[1]}_{cambio}"

            T[(f"S{b}", producto)] = (
                nuevo_estado,
                f"Iniciar{producto}"
            )

        else:

            T[(f"S{b}", producto)] = (
                f"S{b}", "SaldoInsuficiente"
            )


# -----------------------------------------------------
# 4.3 TRANSICIONES DE CANCELACION
# -----------------------------------------------------

T[("S0", "CANCELAR")] = (
    "S0", "Esperar"
)

for b in range(1, 30):

    T[(f"S{b}", "CANCELAR")] = (
        "S0", f"CancelarYDevolver({b})"
    )


# -----------------------------------------------------
# 4.4 TRANSICIONES DE CONFIRMACION DE ENTREGA
# -----------------------------------------------------

# Estados del producto 1
for c in range(20):

    if c == 0:
        salida = "ConfirmarEntrega"
    else:
        salida = f"ConfirmarEntregaYDevolver({c})"

    T[(f"D1_{c}", "SE")] = ("S0", salida)


# Estados del producto 2
for c in range(15):

    if c == 0:
        salida = "ConfirmarEntrega"
    else:
        salida = f"ConfirmarEntregaYDevolver({c})"

    T[(f"D2_{c}", "SE")] = ("S0", salida)


# Estados del producto 3
for c in range(10):

    if c == 0:
        salida = "ConfirmarEntrega"
    else:
        salida = f"ConfirmarEntregaYDevolver({c})"

    T[(f"D3_{c}", "SE")] = ("S0", salida)


# -----------------------------------------------------
# 5. ALFABETO DE SALIDA GAMMA
# -----------------------------------------------------

Gamma = {
    salida
    for estado_siguiente, salida in T.values()
}


# -----------------------------------------------------
# 6. SIMULADOR DE LA MAQUINA
# -----------------------------------------------------

def ejecutar_maquina():

    estado_actual = q0

    print("================================")
    print("     MAQUINA EXPENDEDORA")
    print("================================")

    print("P1 = $10")
    print("P2 = $15")
    print("P3 = $20")

    print("--------------------------------")
    print("A = $1 | B = $2 | C = $5 | D = $10")
    print("--------------------------------")
    print("CANCELAR = Cancelar operacion")
    print("SE = Confirmar entrega")
    print("SALIR = Cerrar simulador")
    print("================================")

    while True:

        print("\nEstado actual:", estado_actual)

        entrada = input("Entrada: ").strip().upper()

        if entrada == "SALIR":
            print("Simulador finalizado.")
            break

        if entrada not in Sigma:
            print("Entrada no valida.")
            continue

        # Consulta directa a la tabla T
        estado_siguiente, salida = T[
            (estado_actual, entrada)
        ]

        print("Entrada:", entrada)
        print("Salida:", salida)
        print("Estado siguiente:", estado_siguiente)

        # Actualizar el estado de la maquina
        estado_actual = estado_siguiente


# -----------------------------------------------------
# 7. EJECUCION
# -----------------------------------------------------

if __name__ == "__main__":

    print("Cantidad de estados:", len(Q))
    print("Cantidad de entradas:", len(Sigma))
    print("Cantidad de transiciones:", len(T))
    print("Cantidad de salidas:", len(Gamma))

    ejecutar_maquina()
