import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def grade_plot(df):
    fig, ax = plt.subplots()

    modules = df['Module']
    x = np.arange(len(modules))

    width = 0.2
    ax.bar(x - 3 * width / 2, df['Leo'], width, label='Leo', color='#0343df')
    ax.bar(x - width / 2, df['Daniel'], width, label='Daniel', color='#e50000')
    ax.bar(x + width / 2, df['Ilias'], width, label='Ilias', color='#ffff14')
    ax.bar(x + 3 * width / 2, df['Sam'], width, label='Sam', color='#929591')

    ax.set_ylabel('Grade')
    ax.set_title('Module Results')
    ax.set_xticks(x)
    ax.set_xticklabels(modules.astype(str).values, rotation='vertical')
    ax.legend()

    plt.show()