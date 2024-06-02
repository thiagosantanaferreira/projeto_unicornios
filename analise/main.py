import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('data\data.csv')
df.rename (columns={
    'Unnamed: 0' : 'Id',
    'Company' : 'Empresa',
    'Valuation $B': 'Valor',
    'Date Joined': 'Data Adesão',
    'Country': 'Pais',
    'City': 'Cidade',
    'Industry' : 'Setor',
    'Select Investors': 'Investidores'
}, inplace=True)

df['Valor'] = df['Valor'].str.replace('\$', '', regex=True)
df['Valor'] = df['Valor'].fillna(0).astype(float)

df['Data Adesão'] = pd.to_datetime(df['Data Adesão'])

df['Mes'] = pd.DatetimeIndex(df['Data Adesão']).month
df['Ano'] = pd.DatetimeIndex(df['Data Adesão']).year
df = df.drop(columns=['Data Adesão'],axis=0)

# Tabela analitica utilizando o GROUPBY
''' analise_agrupada = df.groupby(by=['Pais','Ano', 'Empresa']).count()['Id'].reset_index()
analise_agrupada.loc[analise_agrupada['Pais'] == 'Brazil'] '''

#Tabela analitica agrupada por maior valor
''' analise_por_valor = df.groupby(by=['Pais']).sum()['Valor'].reset_index()
analise_por_valor = analise_por_valor.sort_values('Valor', ascending=False)
analise_por_valor[:6] 
print(analise_por_valor[:6]) '''
