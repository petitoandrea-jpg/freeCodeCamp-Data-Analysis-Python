import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Importa i dati da medical_examination.csv
df = pd.read_csv('medical_examination.csv')

# 2. Aggiungi la colonna 'overweight' (BMI = kg / m^2)
# Altezza convertita in metri (height / 100)
bmi = df['weight'] / ((df['height'] / 100) ** 2)
df['overweight'] = (bmi > 25).astype(int)

# 3. Normalizza i dati: 0 se il valore è 1 (buono), 1 se è > 1 (cattivo)
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)


# 4. Disegna il grafico categorico
def draw_cat_plot():
    # 5. Crea il DataFrame con pd.melt
    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    )

    # 6. Raggruppa e conteggia i valori per ogni funzionalità divisa per cardio
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # 7 & 8. Crea il grafico sns.catplot e salva la figura
    g = sns.catplot(
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        data=df_cat,
        kind='bar'
    )
    
    fig = g.fig

    # 9. Non modificare le due righe successive
    fig.savefig('catplot.png')
    return fig


# 10. Disegna la mappa di calore (Heatmap)
def draw_heat_map():
    # 11. Pulisci i dati filtrando le anomalie di pressione, altezza e peso
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12. Calcola la matrice di correlazione
    corr = df_heat.corr()

    # 13. Genera la maschera per il triangolo superiore
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14. Imposta la figura matplotlib
    fig, ax = plt.subplots(figsize=(12, 12))

    # 15. Traccia la matrice di correlazione usando sns.heatmap()
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt='.1f',
        square=True,
        cbar_kws={'shrink': 0.5},
        ax=ax
    )

    # 16. Non modificare le due righe successive
    fig.savefig('heatmap.png')
    return fig