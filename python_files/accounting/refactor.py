import pandas as pd
from json import load
import matplotlib
import matplotlib.pyplot as plt


"""
    main variables retrieval
"""

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


"""
Some variables for filtering -- from Wolfram.nb
"""

with open("config\\settings.json", 'r') as f:
    category_dict = load(f)

gastos = [ "CASA", "CELULAR", "COM_VAR", "MENU", "PASAJE", "PERSONAL", "RECIBO", "VARIOS"]

ingresos = [ "INGRESO", "BLIND"]

grouped_by_year_and_month = raw_data.groupby([raw_data.Date.dt.year, raw_data.Date.dt.month])


def year_month(year: int, month: int) -> pd.core.series.Series:
    """
        To access to this varaibles, please evaluate
        grouped_by_year_and_month.get_group((year,month))

        Creating a function that takes (year, month) and returns
        the dataframe grouped, ready for aesthetics
    """
    
    df = grouped_by_year_and_month.get_group((year, month))

    return (df.loc[
        (df.Category != "INGRESO") & (df.Category != "BLIND")]
    .groupby('Category')
    .Amount.sum()
    )


def personal_settings()->None:
    '''
        Dark mode on matplotlib
    '''
    plt.style.use('dark_background')
    plt.rcParams['font.family'] = 'monospace'  # Set font family
    plt.rcParams['font.size'] = 12  # Set font size

personal_settings()

data_plot_pie = year_month(2025,3)
tot = data_plot_pie.sum()

fig, ax = plt.subplots()

ax.pie(
    data_plot_pie,
    colors = [category_dict[key]['color'] for key in list(data_plot_pie.index)],
)

ax.text(
    x = 0.0, y = 0.0,
    s = 'Expenses',
    ha = 'center',
    va = 'bottom'
)

ax.legend(
    loc = (-0.5,0),
    labels = [
        category_dict[key]['label'] + f'\nPEN {data_plot_pie[key]:.2f}\n'
        for key in list(data_plot_pie.index)]
    )
plt.show()




