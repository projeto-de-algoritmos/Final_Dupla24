import pandas as pd

def mostrarTabela():
    pilotos_bruto = pd.read_csv('drivers.csv')
    brasileiros = pilotos_bruto.query("nationality == 'Brazilian'")
    pilotos_filtr = brasileiros[['code', 'forename', 'surname', 'nationality']]
    pilotos_ord = pilotos_filtr.sort_values(by=['surname'], kind='mergesort')
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_colwidth', None)
    pilotos_ord.columns = ['CÓDIGO', 'NOME', 'SOBRENOME', 'NACIONALIDADE']
    print(pilotos_ord.to_string(index=False))