
import pandas as pd
import os

def loader() -> pd.DataFrame:

    path = r'C:/Users/sgast/tania/tania_new_excel.xlsx'
    df = pd.read_excel(path)
    return (df.iloc[:,13:-6])

def hoja_resumenes(df:pd.DataFrame) -> pd.DataFrame:

    df_resumen = df.copy()

    df_resumen = pd.concat([
        df_resumen[df_resumen == 'Seguro'].count(),
        df_resumen[df_resumen == 'Riesgoso'].count(), 
        df_resumen.isnull().sum()], 
        axis = 1)

    df_resumen.reset_index(inplace= True)
    df_resumen.columns = ['Comportamiento','ST','RT','Null']

    new_col = df_resumen.Comportamiento.str.split('.', expand = True)
    new_col = new_col.iloc[:,:2]
    new_col.columns = ['Categoria','Comportamiento']

    df_resumen = pd.concat([
        new_col, 
        df_resumen[['ST','RT','Null']]],
        axis = 1)

    return df_resumen

def hoja_promedio(df_resumen:pd.DataFrame) -> pd.DataFrame:

    FP_dict = {
        'Mecánica de Movimientos Corporales': 1,
        'EPP': 2,
        'Factores o Condición de Trabajo / Naturaleza': 2,
        'Herramientas y Equipos': 3,
        'Orden y Limpieza': 2,
        'Trabajos de Alto Riesgo': 2
    }

    pd.options.display.float_format = '{:.2f}% '.format
    
    df_g = df_resumen.groupby('Categoria')[['Null','ST','RT']].sum()
    
    sums = df_g.sum(axis = 1).values

    df_g2 = df_g[['Null','ST','RT']].div(sums/100, axis = 0) 
    
    df_g2['FP'] = df_g.index.map(lambda x: FP_dict[x])
    
    df_g2['Nivel_Criticidad'] = df_g2.apply(
        lambda x: 100 * x.iloc[3] * x.iloc[2] / (x.iloc[0] + x.iloc[1] + x.iloc[2] * x.iloc[3]), 
        axis = 1)
    
    return df_g2


if __name__ == '__main__':
    
    df_ingresos = loader()
    
    df_resumen = hoja_resumenes(df_ingresos)
    
    df_promedio = hoja_promedio(df_resumen)

    path_to_save = r'C:\Users\sgast\tania\excel_from_python.xlsx'

    with pd.ExcelWriter(path_to_save) as w:
        df_ingresos.to_excel(w, sheet_name='INGRESOS', index=True)
        df_resumen.to_excel(w, sheet_name='RESUMEN', index=True)
        df_promedio.to_excel(w, sheet_name='PROMEDIO', index=True)

    print("DataFrames uploaded to Excel sheets successfully.")
    
    os.startfile(path_to_save)