# =====================================================
# MAQUINA EXPENDEDORA
# Maquina de Estados Finitos de Mealy
# =====================================================


#====================================================
# Limitaciones de la maquina de estados finitos de Mealy
# Solo acepta monedas de $1, $2, $5 y $10
# El limite de saldo es $20, por lo que no se aceptan monedas que excedan este limite
# Una vez dispensando un producto, solo acepta la entrada de "SE" para confirmar la entrega del producto
# ====================================================


# =====================================================
# TABLAS EXPLICITAS DE LA MAQUINA
# =====================================================

# El orden de estas entradas corresponde a las columnas de cada fila de T.
Sigma = ("A", "B", "C", "D", "P1", "P2", "P3", "CANCELAR", "SE")

Q = (
    "S0", "S1", "S2", "S3", "S4",
    "S5", "S6", "S7", "S8", "S9",
    "S10", "S11", "S12", "S13", "S14",
    "S15", "S16", "S17", "S18", "S19",
    "S20", "S21", "S22", "S23", "S24",
    "S25", "S26", "S27", "S28", "S29",
    "D1_0", "D1_1", "D1_2", "D1_3", "D1_4",
    "D1_5", "D1_6", "D1_7", "D1_8", "D1_9",
    "D1_10", "D1_11", "D1_12", "D1_13", "D1_14",
    "D1_15", "D1_16", "D1_17", "D1_18", "D1_19",
    "D2_0", "D2_1", "D2_2", "D2_3", "D2_4",
    "D2_5", "D2_6", "D2_7", "D2_8", "D2_9",
    "D2_10", "D2_11", "D2_12", "D2_13", "D2_14",
    "D3_0", "D3_1", "D3_2", "D3_3", "D3_4",
    "D3_5", "D3_6", "D3_7", "D3_8", "D3_9",
)

q0 = "S0"

# T[estado][columna de Sigma] = (estado siguiente, salida)
T = {
    "S0": (("S1", "MS(1)"), ("S2", "MS(2)"), ("S5", "MS(5)"), ("S10", "MS(10)"), ("S0", "SaldoInsuficiente"), ("S0", "SaldoInsuficiente"), ("S0", "SaldoInsuficiente"), ("S0", "Esperar"), ("S0", "Esperar")),
    "S1": (("S2", "MS(2)"), ("S3", "MS(3)"), ("S6", "MS(6)"), ("S11", "MS(11)"), ("S1", "SaldoInsuficiente"), ("S1", "SaldoInsuficiente"), ("S1", "SaldoInsuficiente"), ("S0", "CancelarYDevolver(1)"), ("S1", "Esperar")),
    "S2": (("S3", "MS(3)"), ("S4", "MS(4)"), ("S7", "MS(7)"), ("S12", "MS(12)"), ("S2", "SaldoInsuficiente"), ("S2", "SaldoInsuficiente"), ("S2", "SaldoInsuficiente"), ("S0", "CancelarYDevolver(2)"), ("S2", "Esperar")),
    "S3": (("S4", "MS(4)"), ("S5", "MS(5)"), ("S8", "MS(8)"), ("S13", "MS(13)"), ("S3", "SaldoInsuficiente"), ("S3", "SaldoInsuficiente"), ("S3", "SaldoInsuficiente"), ("S0", "CancelarYDevolver(3)"), ("S3", "Esperar")),
    "S4": (("S5", "MS(5)"), ("S6", "MS(6)"), ("S9", "MS(9)"), ("S14", "MS(14)"), ("S4", "SaldoInsuficiente"), ("S4", "SaldoInsuficiente"), ("S4", "SaldoInsuficiente"), ("S0", "CancelarYDevolver(4)"), ("S4", "Esperar")),
    "S5": (("S6", "MS(6)"), ("S7", "MS(7)"), ("S10", "MS(10)"), ("S15", "MS(15)"), ("S5", "SaldoInsuficiente"), ("S5", "SaldoInsuficiente"), ("S5", "SaldoInsuficiente"), ("S0", "CancelarYDevolver(5)"), ("S5", "Esperar")),
    "S6": (("S7", "MS(7)"), ("S8", "MS(8)"), ("S11", "MS(11)"), ("S16", "MS(16)"), ("S6", "SaldoInsuficiente"), ("S6", "SaldoInsuficiente"), ("S6", "SaldoInsuficiente"), ("S0", "CancelarYDevolver(6)"), ("S6", "Esperar")),
    "S7": (("S8", "MS(8)"), ("S9", "MS(9)"), ("S12", "MS(12)"), ("S17", "MS(17)"), ("S7", "SaldoInsuficiente"), ("S7", "SaldoInsuficiente"), ("S7", "SaldoInsuficiente"), ("S0", "CancelarYDevolver(7)"), ("S7", "Esperar")),
    "S8": (("S9", "MS(9)"), ("S10", "MS(10)"), ("S13", "MS(13)"), ("S18", "MS(18)"), ("S8", "SaldoInsuficiente"), ("S8", "SaldoInsuficiente"), ("S8", "SaldoInsuficiente"), ("S0", "CancelarYDevolver(8)"), ("S8", "Esperar")),
    "S9": (("S10", "MS(10)"), ("S11", "MS(11)"), ("S14", "MS(14)"), ("S19", "MS(19)"), ("S9", "SaldoInsuficiente"), ("S9", "SaldoInsuficiente"), ("S9", "SaldoInsuficiente"), ("S0", "CancelarYDevolver(9)"), ("S9", "Esperar")),
    "S10": (("S11", "MS(11)"), ("S12", "MS(12)"), ("S15", "MS(15)"), ("S20", "MS(20)"), ("D1_0", "IniciarP1"), ("S10", "SaldoInsuficiente"), ("S10", "SaldoInsuficiente"), ("S0", "CancelarYDevolver(10)"), ("S10", "Esperar")),
    "S11": (("S12", "MS(12)"), ("S13", "MS(13)"), ("S16", "MS(16)"), ("S21", "MS(21)"), ("D1_1", "IniciarP1"), ("S11", "SaldoInsuficiente"), ("S11", "SaldoInsuficiente"), ("S0", "CancelarYDevolver(11)"), ("S11", "Esperar")),
    "S12": (("S13", "MS(13)"), ("S14", "MS(14)"), ("S17", "MS(17)"), ("S22", "MS(22)"), ("D1_2", "IniciarP1"), ("S12", "SaldoInsuficiente"), ("S12", "SaldoInsuficiente"), ("S0", "CancelarYDevolver(12)"), ("S12", "Esperar")),
    "S13": (("S14", "MS(14)"), ("S15", "MS(15)"), ("S18", "MS(18)"), ("S23", "MS(23)"), ("D1_3", "IniciarP1"), ("S13", "SaldoInsuficiente"), ("S13", "SaldoInsuficiente"), ("S0", "CancelarYDevolver(13)"), ("S13", "Esperar")),
    "S14": (("S15", "MS(15)"), ("S16", "MS(16)"), ("S19", "MS(19)"), ("S24", "MS(24)"), ("D1_4", "IniciarP1"), ("S14", "SaldoInsuficiente"), ("S14", "SaldoInsuficiente"), ("S0", "CancelarYDevolver(14)"), ("S14", "Esperar")),
    "S15": (("S16", "MS(16)"), ("S17", "MS(17)"), ("S20", "MS(20)"), ("S25", "MS(25)"), ("D1_5", "IniciarP1"), ("D2_0", "IniciarP2"), ("S15", "SaldoInsuficiente"), ("S0", "CancelarYDevolver(15)"), ("S15", "Esperar")),
    "S16": (("S17", "MS(17)"), ("S18", "MS(18)"), ("S21", "MS(21)"), ("S26", "MS(26)"), ("D1_6", "IniciarP1"), ("D2_1", "IniciarP2"), ("S16", "SaldoInsuficiente"), ("S0", "CancelarYDevolver(16)"), ("S16", "Esperar")),
    "S17": (("S18", "MS(18)"), ("S19", "MS(19)"), ("S22", "MS(22)"), ("S27", "MS(27)"), ("D1_7", "IniciarP1"), ("D2_2", "IniciarP2"), ("S17", "SaldoInsuficiente"), ("S0", "CancelarYDevolver(17)"), ("S17", "Esperar")),
    "S18": (("S19", "MS(19)"), ("S20", "MS(20)"), ("S23", "MS(23)"), ("S28", "MS(28)"), ("D1_8", "IniciarP1"), ("D2_3", "IniciarP2"), ("S18", "SaldoInsuficiente"), ("S0", "CancelarYDevolver(18)"), ("S18", "Esperar")),
    "S19": (("S20", "MS(20)"), ("S21", "MS(21)"), ("S24", "MS(24)"), ("S29", "MS(29)"), ("D1_9", "IniciarP1"), ("D2_4", "IniciarP2"), ("S19", "SaldoInsuficiente"), ("S0", "CancelarYDevolver(19)"), ("S19", "Esperar")),
    "S20": (("S20", "RechazarMoneda"), ("S20", "RechazarMoneda"), ("S20", "RechazarMoneda"), ("S20", "RechazarMoneda"), ("D1_10", "IniciarP1"), ("D2_5", "IniciarP2"), ("D3_0", "IniciarP3"), ("S0", "CancelarYDevolver(20)"), ("S20", "Esperar")),
    "S21": (("S21", "RechazarMoneda"), ("S21", "RechazarMoneda"), ("S21", "RechazarMoneda"), ("S21", "RechazarMoneda"), ("D1_11", "IniciarP1"), ("D2_6", "IniciarP2"), ("D3_1", "IniciarP3"), ("S0", "CancelarYDevolver(21)"), ("S21", "Esperar")),
    "S22": (("S22", "RechazarMoneda"), ("S22", "RechazarMoneda"), ("S22", "RechazarMoneda"), ("S22", "RechazarMoneda"), ("D1_12", "IniciarP1"), ("D2_7", "IniciarP2"), ("D3_2", "IniciarP3"), ("S0", "CancelarYDevolver(22)"), ("S22", "Esperar")),
    "S23": (("S23", "RechazarMoneda"), ("S23", "RechazarMoneda"), ("S23", "RechazarMoneda"), ("S23", "RechazarMoneda"), ("D1_13", "IniciarP1"), ("D2_8", "IniciarP2"), ("D3_3", "IniciarP3"), ("S0", "CancelarYDevolver(23)"), ("S23", "Esperar")),
    "S24": (("S24", "RechazarMoneda"), ("S24", "RechazarMoneda"), ("S24", "RechazarMoneda"), ("S24", "RechazarMoneda"), ("D1_14", "IniciarP1"), ("D2_9", "IniciarP2"), ("D3_4", "IniciarP3"), ("S0", "CancelarYDevolver(24)"), ("S24", "Esperar")),
    "S25": (("S25", "RechazarMoneda"), ("S25", "RechazarMoneda"), ("S25", "RechazarMoneda"), ("S25", "RechazarMoneda"), ("D1_15", "IniciarP1"), ("D2_10", "IniciarP2"), ("D3_5", "IniciarP3"), ("S0", "CancelarYDevolver(25)"), ("S25", "Esperar")),
    "S26": (("S26", "RechazarMoneda"), ("S26", "RechazarMoneda"), ("S26", "RechazarMoneda"), ("S26", "RechazarMoneda"), ("D1_16", "IniciarP1"), ("D2_11", "IniciarP2"), ("D3_6", "IniciarP3"), ("S0", "CancelarYDevolver(26)"), ("S26", "Esperar")),
    "S27": (("S27", "RechazarMoneda"), ("S27", "RechazarMoneda"), ("S27", "RechazarMoneda"), ("S27", "RechazarMoneda"), ("D1_17", "IniciarP1"), ("D2_12", "IniciarP2"), ("D3_7", "IniciarP3"), ("S0", "CancelarYDevolver(27)"), ("S27", "Esperar")),
    "S28": (("S28", "RechazarMoneda"), ("S28", "RechazarMoneda"), ("S28", "RechazarMoneda"), ("S28", "RechazarMoneda"), ("D1_18", "IniciarP1"), ("D2_13", "IniciarP2"), ("D3_8", "IniciarP3"), ("S0", "CancelarYDevolver(28)"), ("S28", "Esperar")),
    "S29": (("S29", "RechazarMoneda"), ("S29", "RechazarMoneda"), ("S29", "RechazarMoneda"), ("S29", "RechazarMoneda"), ("D1_19", "IniciarP1"), ("D2_14", "IniciarP2"), ("D3_9", "IniciarP3"), ("S0", "CancelarYDevolver(29)"), ("S29", "Esperar")),
    "D1_0": (("D1_0", "Esperar"), ("D1_0", "Esperar"), ("D1_0", "Esperar"), ("D1_0", "Esperar"), ("D1_0", "Esperar"), ("D1_0", "Esperar"), ("D1_0", "Esperar"), ("D1_0", "Esperar"), ("S0", "ConfirmarEntrega")),
    "D1_1": (("D1_1", "Esperar"), ("D1_1", "Esperar"), ("D1_1", "Esperar"), ("D1_1", "Esperar"), ("D1_1", "Esperar"), ("D1_1", "Esperar"), ("D1_1", "Esperar"), ("D1_1", "Esperar"), ("S0", "ConfirmarEntregaYDevolver(1)")),
    "D1_2": (("D1_2", "Esperar"), ("D1_2", "Esperar"), ("D1_2", "Esperar"), ("D1_2", "Esperar"), ("D1_2", "Esperar"), ("D1_2", "Esperar"), ("D1_2", "Esperar"), ("D1_2", "Esperar"), ("S0", "ConfirmarEntregaYDevolver(2)")),
    "D1_3": (("D1_3", "Esperar"), ("D1_3", "Esperar"), ("D1_3", "Esperar"), ("D1_3", "Esperar"), ("D1_3", "Esperar"), ("D1_3", "Esperar"), ("D1_3", "Esperar"), ("D1_3", "Esperar"), ("S0", "ConfirmarEntregaYDevolver(3)")),
    "D1_4": (("D1_4", "Esperar"), ("D1_4", "Esperar"), ("D1_4", "Esperar"), ("D1_4", "Esperar"), ("D1_4", "Esperar"), ("D1_4", "Esperar"), ("D1_4", "Esperar"), ("D1_4", "Esperar"), ("S0", "ConfirmarEntregaYDevolver(4)")),
    "D1_5": (("D1_5", "Esperar"), ("D1_5", "Esperar"), ("D1_5", "Esperar"), ("D1_5", "Esperar"), ("D1_5", "Esperar"), ("D1_5", "Esperar"), ("D1_5", "Esperar"), ("D1_5", "Esperar"), ("S0", "ConfirmarEntregaYDevolver(5)")),
    "D1_6": (("D1_6", "Esperar"), ("D1_6", "Esperar"), ("D1_6", "Esperar"), ("D1_6", "Esperar"), ("D1_6", "Esperar"), ("D1_6", "Esperar"), ("D1_6", "Esperar"), ("D1_6", "Esperar"), ("S0", "ConfirmarEntregaYDevolver(6)")),
    "D1_7": (("D1_7", "Esperar"), ("D1_7", "Esperar"), ("D1_7", "Esperar"), ("D1_7", "Esperar"), ("D1_7", "Esperar"), ("D1_7", "Esperar"), ("D1_7", "Esperar"), ("D1_7", "Esperar"), ("S0", "ConfirmarEntregaYDevolver(7)")),
    "D1_8": (("D1_8", "Esperar"), ("D1_8", "Esperar"), ("D1_8", "Esperar"), ("D1_8", "Esperar"), ("D1_8", "Esperar"), ("D1_8", "Esperar"), ("D1_8", "Esperar"), ("D1_8", "Esperar"), ("S0", "ConfirmarEntregaYDevolver(8)")),
    "D1_9": (("D1_9", "Esperar"), ("D1_9", "Esperar"), ("D1_9", "Esperar"), ("D1_9", "Esperar"), ("D1_9", "Esperar"), ("D1_9", "Esperar"), ("D1_9", "Esperar"), ("D1_9", "Esperar"), ("S0", "ConfirmarEntregaYDevolver(9)")),
    "D1_10": (("D1_10", "Esperar"), ("D1_10", "Esperar"), ("D1_10", "Esperar"), ("D1_10", "Esperar"), ("D1_10", "Esperar"), ("D1_10", "Esperar"), ("D1_10", "Esperar"), ("D1_10", "Esperar"), ("S0", "ConfirmarEntregaYDevolver(10)")),
    "D1_11": (("D1_11", "Esperar"), ("D1_11", "Esperar"), ("D1_11", "Esperar"), ("D1_11", "Esperar"), ("D1_11", "Esperar"), ("D1_11", "Esperar"), ("D1_11", "Esperar"), ("D1_11", "Esperar"), ("S0", "ConfirmarEntregaYDevolver(11)")),
    "D1_12": (("D1_12", "Esperar"), ("D1_12", "Esperar"), ("D1_12", "Esperar"), ("D1_12", "Esperar"), ("D1_12", "Esperar"), ("D1_12", "Esperar"), ("D1_12", "Esperar"), ("D1_12", "Esperar"), ("S0", "ConfirmarEntregaYDevolver(12)")),
    "D1_13": (("D1_13", "Esperar"), ("D1_13", "Esperar"), ("D1_13", "Esperar"), ("D1_13", "Esperar"), ("D1_13", "Esperar"), ("D1_13", "Esperar"), ("D1_13", "Esperar"), ("D1_13", "Esperar"), ("S0", "ConfirmarEntregaYDevolver(13)")),
    "D1_14": (("D1_14", "Esperar"), ("D1_14", "Esperar"), ("D1_14", "Esperar"), ("D1_14", "Esperar"), ("D1_14", "Esperar"), ("D1_14", "Esperar"), ("D1_14", "Esperar"), ("D1_14", "Esperar"), ("S0", "ConfirmarEntregaYDevolver(14)")),
    "D1_15": (("D1_15", "Esperar"), ("D1_15", "Esperar"), ("D1_15", "Esperar"), ("D1_15", "Esperar"), ("D1_15", "Esperar"), ("D1_15", "Esperar"), ("D1_15", "Esperar"), ("D1_15", "Esperar"), ("S0", "ConfirmarEntregaYDevolver(15)")),
    "D1_16": (("D1_16", "Esperar"), ("D1_16", "Esperar"), ("D1_16", "Esperar"), ("D1_16", "Esperar"), ("D1_16", "Esperar"), ("D1_16", "Esperar"), ("D1_16", "Esperar"), ("D1_16", "Esperar"), ("S0", "ConfirmarEntregaYDevolver(16)")),
    "D1_17": (("D1_17", "Esperar"), ("D1_17", "Esperar"), ("D1_17", "Esperar"), ("D1_17", "Esperar"), ("D1_17", "Esperar"), ("D1_17", "Esperar"), ("D1_17", "Esperar"), ("D1_17", "Esperar"), ("S0", "ConfirmarEntregaYDevolver(17)")),
    "D1_18": (("D1_18", "Esperar"), ("D1_18", "Esperar"), ("D1_18", "Esperar"), ("D1_18", "Esperar"), ("D1_18", "Esperar"), ("D1_18", "Esperar"), ("D1_18", "Esperar"), ("D1_18", "Esperar"), ("S0", "ConfirmarEntregaYDevolver(18)")),
    "D1_19": (("D1_19", "Esperar"), ("D1_19", "Esperar"), ("D1_19", "Esperar"), ("D1_19", "Esperar"), ("D1_19", "Esperar"), ("D1_19", "Esperar"), ("D1_19", "Esperar"), ("D1_19", "Esperar"), ("S0", "ConfirmarEntregaYDevolver(19)")),
    "D2_0": (("D2_0", "Esperar"), ("D2_0", "Esperar"), ("D2_0", "Esperar"), ("D2_0", "Esperar"), ("D2_0", "Esperar"), ("D2_0", "Esperar"), ("D2_0", "Esperar"), ("D2_0", "Esperar"), ("S0", "ConfirmarEntrega")),
    "D2_1": (("D2_1", "Esperar"), ("D2_1", "Esperar"), ("D2_1", "Esperar"), ("D2_1", "Esperar"), ("D2_1", "Esperar"), ("D2_1", "Esperar"), ("D2_1", "Esperar"), ("D2_1", "Esperar"), ("S0", "ConfirmarEntregaYDevolver(1)")),
    "D2_2": (("D2_2", "Esperar"), ("D2_2", "Esperar"), ("D2_2", "Esperar"), ("D2_2", "Esperar"), ("D2_2", "Esperar"), ("D2_2", "Esperar"), ("D2_2", "Esperar"), ("D2_2", "Esperar"), ("S0", "ConfirmarEntregaYDevolver(2)")),
    "D2_3": (("D2_3", "Esperar"), ("D2_3", "Esperar"), ("D2_3", "Esperar"), ("D2_3", "Esperar"), ("D2_3", "Esperar"), ("D2_3", "Esperar"), ("D2_3", "Esperar"), ("D2_3", "Esperar"), ("S0", "ConfirmarEntregaYDevolver(3)")),
    "D2_4": (("D2_4", "Esperar"), ("D2_4", "Esperar"), ("D2_4", "Esperar"), ("D2_4", "Esperar"), ("D2_4", "Esperar"), ("D2_4", "Esperar"), ("D2_4", "Esperar"), ("D2_4", "Esperar"), ("S0", "ConfirmarEntregaYDevolver(4)")),
    "D2_5": (("D2_5", "Esperar"), ("D2_5", "Esperar"), ("D2_5", "Esperar"), ("D2_5", "Esperar"), ("D2_5", "Esperar"), ("D2_5", "Esperar"), ("D2_5", "Esperar"), ("D2_5", "Esperar"), ("S0", "ConfirmarEntregaYDevolver(5)")),
    "D2_6": (("D2_6", "Esperar"), ("D2_6", "Esperar"), ("D2_6", "Esperar"), ("D2_6", "Esperar"), ("D2_6", "Esperar"), ("D2_6", "Esperar"), ("D2_6", "Esperar"), ("D2_6", "Esperar"), ("S0", "ConfirmarEntregaYDevolver(6)")),
    "D2_7": (("D2_7", "Esperar"), ("D2_7", "Esperar"), ("D2_7", "Esperar"), ("D2_7", "Esperar"), ("D2_7", "Esperar"), ("D2_7", "Esperar"), ("D2_7", "Esperar"), ("D2_7", "Esperar"), ("S0", "ConfirmarEntregaYDevolver(7)")),
    "D2_8": (("D2_8", "Esperar"), ("D2_8", "Esperar"), ("D2_8", "Esperar"), ("D2_8", "Esperar"), ("D2_8", "Esperar"), ("D2_8", "Esperar"), ("D2_8", "Esperar"), ("D2_8", "Esperar"), ("S0", "ConfirmarEntregaYDevolver(8)")),
    "D2_9": (("D2_9", "Esperar"), ("D2_9", "Esperar"), ("D2_9", "Esperar"), ("D2_9", "Esperar"), ("D2_9", "Esperar"), ("D2_9", "Esperar"), ("D2_9", "Esperar"), ("D2_9", "Esperar"), ("S0", "ConfirmarEntregaYDevolver(9)")),
    "D2_10": (("D2_10", "Esperar"), ("D2_10", "Esperar"), ("D2_10", "Esperar"), ("D2_10", "Esperar"), ("D2_10", "Esperar"), ("D2_10", "Esperar"), ("D2_10", "Esperar"), ("D2_10", "Esperar"), ("S0", "ConfirmarEntregaYDevolver(10)")),
    "D2_11": (("D2_11", "Esperar"), ("D2_11", "Esperar"), ("D2_11", "Esperar"), ("D2_11", "Esperar"), ("D2_11", "Esperar"), ("D2_11", "Esperar"), ("D2_11", "Esperar"), ("D2_11", "Esperar"), ("S0", "ConfirmarEntregaYDevolver(11)")),
    "D2_12": (("D2_12", "Esperar"), ("D2_12", "Esperar"), ("D2_12", "Esperar"), ("D2_12", "Esperar"), ("D2_12", "Esperar"), ("D2_12", "Esperar"), ("D2_12", "Esperar"), ("D2_12", "Esperar"), ("S0", "ConfirmarEntregaYDevolver(12)")),
    "D2_13": (("D2_13", "Esperar"), ("D2_13", "Esperar"), ("D2_13", "Esperar"), ("D2_13", "Esperar"), ("D2_13", "Esperar"), ("D2_13", "Esperar"), ("D2_13", "Esperar"), ("D2_13", "Esperar"), ("S0", "ConfirmarEntregaYDevolver(13)")),
    "D2_14": (("D2_14", "Esperar"), ("D2_14", "Esperar"), ("D2_14", "Esperar"), ("D2_14", "Esperar"), ("D2_14", "Esperar"), ("D2_14", "Esperar"), ("D2_14", "Esperar"), ("D2_14", "Esperar"), ("S0", "ConfirmarEntregaYDevolver(14)")),
    "D3_0": (("D3_0", "Esperar"), ("D3_0", "Esperar"), ("D3_0", "Esperar"), ("D3_0", "Esperar"), ("D3_0", "Esperar"), ("D3_0", "Esperar"), ("D3_0", "Esperar"), ("D3_0", "Esperar"), ("S0", "ConfirmarEntrega")),
    "D3_1": (("D3_1", "Esperar"), ("D3_1", "Esperar"), ("D3_1", "Esperar"), ("D3_1", "Esperar"), ("D3_1", "Esperar"), ("D3_1", "Esperar"), ("D3_1", "Esperar"), ("D3_1", "Esperar"), ("S0", "ConfirmarEntregaYDevolver(1)")),
    "D3_2": (("D3_2", "Esperar"), ("D3_2", "Esperar"), ("D3_2", "Esperar"), ("D3_2", "Esperar"), ("D3_2", "Esperar"), ("D3_2", "Esperar"), ("D3_2", "Esperar"), ("D3_2", "Esperar"), ("S0", "ConfirmarEntregaYDevolver(2)")),
    "D3_3": (("D3_3", "Esperar"), ("D3_3", "Esperar"), ("D3_3", "Esperar"), ("D3_3", "Esperar"), ("D3_3", "Esperar"), ("D3_3", "Esperar"), ("D3_3", "Esperar"), ("D3_3", "Esperar"), ("S0", "ConfirmarEntregaYDevolver(3)")),
    "D3_4": (("D3_4", "Esperar"), ("D3_4", "Esperar"), ("D3_4", "Esperar"), ("D3_4", "Esperar"), ("D3_4", "Esperar"), ("D3_4", "Esperar"), ("D3_4", "Esperar"), ("D3_4", "Esperar"), ("S0", "ConfirmarEntregaYDevolver(4)")),
    "D3_5": (("D3_5", "Esperar"), ("D3_5", "Esperar"), ("D3_5", "Esperar"), ("D3_5", "Esperar"), ("D3_5", "Esperar"), ("D3_5", "Esperar"), ("D3_5", "Esperar"), ("D3_5", "Esperar"), ("S0", "ConfirmarEntregaYDevolver(5)")),
    "D3_6": (("D3_6", "Esperar"), ("D3_6", "Esperar"), ("D3_6", "Esperar"), ("D3_6", "Esperar"), ("D3_6", "Esperar"), ("D3_6", "Esperar"), ("D3_6", "Esperar"), ("D3_6", "Esperar"), ("S0", "ConfirmarEntregaYDevolver(6)")),
    "D3_7": (("D3_7", "Esperar"), ("D3_7", "Esperar"), ("D3_7", "Esperar"), ("D3_7", "Esperar"), ("D3_7", "Esperar"), ("D3_7", "Esperar"), ("D3_7", "Esperar"), ("D3_7", "Esperar"), ("S0", "ConfirmarEntregaYDevolver(7)")),
    "D3_8": (("D3_8", "Esperar"), ("D3_8", "Esperar"), ("D3_8", "Esperar"), ("D3_8", "Esperar"), ("D3_8", "Esperar"), ("D3_8", "Esperar"), ("D3_8", "Esperar"), ("D3_8", "Esperar"), ("S0", "ConfirmarEntregaYDevolver(8)")),
    "D3_9": (("D3_9", "Esperar"), ("D3_9", "Esperar"), ("D3_9", "Esperar"), ("D3_9", "Esperar"), ("D3_9", "Esperar"), ("D3_9", "Esperar"), ("D3_9", "Esperar"), ("D3_9", "Esperar"), ("S0", "ConfirmarEntregaYDevolver(9)")),
}

Gamma = {
    "Esperar", "RechazarMoneda", "SaldoInsuficiente",
    "MS(1)", "MS(2)", "MS(3)", "MS(4)", "MS(5)",
    "MS(6)", "MS(7)", "MS(8)", "MS(9)", "MS(10)",
    "MS(11)", "MS(12)", "MS(13)", "MS(14)", "MS(15)",
    "MS(16)", "MS(17)", "MS(18)", "MS(19)", "MS(20)",
    "MS(21)", "MS(22)", "MS(23)", "MS(24)", "MS(25)",
    "MS(26)", "MS(27)", "MS(28)", "MS(29)",
    "IniciarP1", "IniciarP2", "IniciarP3",
    "CancelarYDevolver(1)", "CancelarYDevolver(2)",
    "CancelarYDevolver(3)", "CancelarYDevolver(4)",
    "CancelarYDevolver(5)", "CancelarYDevolver(6)",
    "CancelarYDevolver(7)", "CancelarYDevolver(8)",
    "CancelarYDevolver(9)", "CancelarYDevolver(10)",
    "CancelarYDevolver(11)", "CancelarYDevolver(12)",
    "CancelarYDevolver(13)", "CancelarYDevolver(14)",
    "CancelarYDevolver(15)", "CancelarYDevolver(16)",
    "CancelarYDevolver(17)", "CancelarYDevolver(18)",
    "CancelarYDevolver(19)", "CancelarYDevolver(20)",
    "CancelarYDevolver(21)", "CancelarYDevolver(22)",
    "CancelarYDevolver(23)", "CancelarYDevolver(24)",
    "CancelarYDevolver(25)", "CancelarYDevolver(26)",
    "CancelarYDevolver(27)", "CancelarYDevolver(28)",
    "CancelarYDevolver(29)",
    "ConfirmarEntrega",
    "ConfirmarEntregaYDevolver(1)", "ConfirmarEntregaYDevolver(2)",
    "ConfirmarEntregaYDevolver(3)", "ConfirmarEntregaYDevolver(4)",
    "ConfirmarEntregaYDevolver(5)", "ConfirmarEntregaYDevolver(6)",
    "ConfirmarEntregaYDevolver(7)", "ConfirmarEntregaYDevolver(8)",
    "ConfirmarEntregaYDevolver(9)", "ConfirmarEntregaYDevolver(10)",
    "ConfirmarEntregaYDevolver(11)", "ConfirmarEntregaYDevolver(12)",
    "ConfirmarEntregaYDevolver(13)", "ConfirmarEntregaYDevolver(14)",
    "ConfirmarEntregaYDevolver(15)", "ConfirmarEntregaYDevolver(16)",
    "ConfirmarEntregaYDevolver(17)", "ConfirmarEntregaYDevolver(18)",
    "ConfirmarEntregaYDevolver(19)"
}


# =====================================================
# SIMULADOR DE LA MAQUINA
# =====================================================

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

        columna = Sigma.index(entrada)
        estado_siguiente, salida = T[estado_actual][columna]

        print("Entrada:", entrada)
        print("Salida:", salida)
        print("Estado siguiente:", estado_siguiente)
        estado_actual = estado_siguiente


if __name__ == "__main__":
    print("Cantidad de estados:", len(Q))
    print("Cantidad de entradas:", len(Sigma))
    print("Cantidad de transiciones:", sum(len(fila) for fila in T.values()))
    print("Cantidad de salidas:", len(Gamma))
    ejecutar_maquina()
