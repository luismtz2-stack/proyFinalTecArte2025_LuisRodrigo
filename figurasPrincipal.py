import pandas as pd

dataFile = pd.read_csv("figuras.csv")

areas = []
perimetros = []


for index, row in dataFile.iterrows():
        print(f"Fila {index}: Figura={row['FIGURA']}, Medida1={row['Medida1']}, Medida2={row['MEDIDA2']}")
