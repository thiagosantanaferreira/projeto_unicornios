# projeto_unicornios




# gitbub
1. caso ja tenha uma pasta criado
* git remote add origin https://github.com/thiagosantanaferreira/projeto_unicornios.git
* git branch -M main
* git push -u origin main

2. Após cada alteração, subir os arquivos no github:
* git add .
* git commit -m "commit message"
* git push

3. Comandos panda
* df.columns -> verifica o nome das colunas do Datafrane
* df.head() -> visualiza parte dao Dataframe
* df.info() -> verifica o tipo de dado de cada coluna
* df.isnull() -> verifica os campos null
* df.isnull().sum() -> como em cada coluna quais campos são null
* df.nunique() -> retornar quantidade de campos unicos.
* df['Mes'] = pd.DatetimeIndex(df['Data Adesão']).month -> retorna o Mês(.month) | Ano (.year) | Dia(.day)

# Gerando graficos
* analise_por_pais = analise_por_valor.sort_values('Valor', ascending=False)
* plt.figure(figsize=(15,6))
* plt.plot(analise_por_valor['Pais], analise_por_valor['Valor])
* plt.xticks(rotation = 45, ha ='right');