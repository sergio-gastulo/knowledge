#%%
import pandas as pd

dolar_to_soles = 3.78
path_to_csv = r'C:\Users\sgast\documents_personal\excel\cuentas.csv'

raw_data = pd.read_csv(
    path_to_csv, 
    header=0, 
    index_col=None,
    dtype={
        "Category": "string",
        "Description": "string", 
        "Amount": "float64"
    },
    parse_dates=["Date"],
    dayfirst=True
    )

raw_data.loc[raw_data.Category == 'USD_INC','Amount'] *= dolar_to_soles
raw_data.loc[raw_data.Category == 'USD_INC','Category'] = 'INGRESO'


#%%


# Some variables for filtering -- from Wolfram.nb

from json import load
with open("settings.json", 'r') as f:
    category_dict = load(f)

gastos = [ "CASA", "CELULAR", "COM_VAR", "MENU", "PASAJE", "PERSONAL", "RECIBO", "VARIOS"]

ingresos = [ "INGRESO", "BLIND"]


# %%

# Running a group by

grouped_by_year_and_month = raw_data.groupby([raw_data.Date.dt.year, raw_data.Date.dt.month])

# To access to this varaibles, please evaluate
# grouped_by_year_and_month.get_group((year,month))

#%%

# Creating a function that takes (year, month) and returns
# the dataframe grouped, ready for aesthetics

def year_month(year: int, month: int) -> pd.core.series.Series:
    
    df = grouped_by_year_and_month.get_group((year, month))

    return (df.loc[
        (df.Category != "INGRESO") & (df.Category != "BLIND")]
    .groupby('Category')
    .Amount.sum()
    )

# %%

import matplotlib.pyplot as plt

def personal_settings()->None:
    '''
        Dark mode on matplotlib
    '''
    plt.style.use('dark_background')
    plt.rcParams['font.family'] = 'monospace'  # Set font family
    plt.rcParams['font.size'] = 12  # Set font size

#%%

import matplotlib.pyplot as plt

data_plot_pie = year_month(2024,8)
tot = data_plot_pie.sum()

fig, ax = plt.subplots()

ax.pie(
    data_plot_pie,
    colors = [category_dict[key]['color'] for key in list(data_plot_pie.index)],
)

ax.set_title('Expenses')
ax.legend(
    loc = (-1,0),
    labels = [
        category_dict[key]['label'] + f'\n PEN {data_plot_pie[key]:.2f}'
        for key in list(data_plot_pie.index)
        ]
        )
plt.show()


# %%
