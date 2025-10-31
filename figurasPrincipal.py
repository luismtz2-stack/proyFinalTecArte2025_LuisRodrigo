import pandas as pd
from funciones import triangulo, circulo, rectangulo

dataFile = pd.read_csv("figuras.csv", delim_whitespace=True)

print("Procesando figuras ...\n")

areas = []

for index, row in dataFile.iterrows():
    FIGURA = row['FIGURA']
    MEDIDA1 = row['MEDIDA1']
    MEDIDA2 = row['MEDIDA2']

    if FIGURA == 't':  # triángulo
        area = triangulo(MEDIDA1, MEDIDA2)
    elif FIGURA == 'r':  # rectángulo
        area = rectangulo(MEDIDA1, MEDIDA2)
    elif FIGURA == 'c':  # círculo
        area = circulo(MEDIDA1)
    else:
        area = None

    areas.append(area)
    print(f"Fila {index}: FIGURA={FIGURA}, MEDIDA1={MEDIDA1}, MEDIDA2={MEDIDA2}, AREA={area}")

