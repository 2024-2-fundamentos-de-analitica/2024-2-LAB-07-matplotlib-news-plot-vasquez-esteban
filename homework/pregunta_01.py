"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import os
from glob import glob

import matplotlib.pyplot as plt  # type: ignore
import pandas as pd  # type: ignore


def _load_data():
    """Load CSV"""

    df = pd.read_csv("files/input/news.csv", index_col=0)
    print(df.info())

    return df


def _create_ouptput_directory(output_directory):
    if os.path.exists(output_directory):
        for file in glob(f"{output_directory}/*"):
            os.remove(file)
        os.rmdir(output_directory)
    os.makedirs(output_directory)


def _create_graph(df):
    """Create plt graph"""

    colors = {
        "Television": "dimgray",
        "Newspaper": "grey",
        "Internet": "tab:blue",
        "Radio": "lightgrey",
    }

    zorders = {
        "Television": 1,
        "Newspaper": 1,
        "Internet": 2,
        "Radio": 1,
    }

    linewidths = {
        "Television": 2,
        "Newspaper": 2,
        "Internet": 4,
        "Radio": 2,
    }

    plt.figure()

    for col in df.columns:
        plt.plot(
            df[col],
            label=col,
            color=colors[col],
            zorder=zorders[col],
            linewidth=linewidths[col],
        )

    for col in df.columns:
        first_year = df.index[0]
        last_year = df.index[-1]

        plt.scatter(
            x=first_year, y=df[col][first_year], color=colors[col], zorder=zorders[col]
        )

        plt.text(
            first_year - 0.2,
            df[col][first_year],
            str(df[col][first_year]) + "%",
            ha="right",
            va="center",
            color=colors[col],
        )

        plt.scatter(
            x=last_year, y=df[col][last_year], color=colors[col], zorder=zorders[col]
        )

        plt.text(
            last_year + 0.2,
            df[col][last_year],
            str(df[col][last_year]) + "%",
            ha="left",
            va="center",
            color=colors[col],
        )

    plt.title("How people get their news", fontsize=16)
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["left"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)

    plt.xticks(ticks=df.index, labels=df.index, ha="center")

    plt.tight_layout()
    plt.savefig("files/plots/news.png")


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """

    df = _load_data()
    _create_ouptput_directory("files/plots")
    _create_graph(df)

    return 1


pregunta_01()
