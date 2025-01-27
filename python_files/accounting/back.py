import pandas as pd

dolar_to_soles = 3.78
path_to_csv = r'C:\Users\sgast\documents_personal\excel\cuentas.csv'

raw_data = pd.read_csv(path_to_csv, header=0, index_col=None)

raw_data.loc[raw_data.Category.str.upper() == 'USD_INC','Amount'] *= dolar_to_soles
raw_data.loc[raw_data.Category.str.upper() == 'USD_INC','Category'] = 'INCOME'

