import pandas as pd

to_read = "C:/Users/Usuario2/Desktop/Pasantias/test_csv.xlsx"

file = pd.read_excel(to_read)

file = file.head(file["Nombre del agente"].shape[0])


