import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. Importa i dati
    df = pd.read_csv('epa-sea-level.csv')

    # 2. Crea il grafico a dispersione
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # 3. Prima retta di regressione (1880 - 2050)
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_all = pd.Series(range(1880, 2051))
    y_all = res_all.slope * x_all + res_all.intercept
    ax.plot(x_all, y_all, 'r')

    # 4. Seconda retta di regressione (2000 - 2050)
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_recent = pd.Series(range(2000, 2051))
    y_recent = res_recent.slope * x_recent + res_recent.intercept
    ax.plot(x_recent, y_recent, 'green')

    # 5. Etichette e titolo
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    # Salva la figura e restituisce l'oggetto Axes richiesto dai test
    fig.savefig('sea_level_plot.png')
    return ax