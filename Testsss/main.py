import generate_fake_dataframe
import pandas as pd
import numpy as np
from itertools import cycle


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    novo = generate_fake_dataframe

    df3 = novo.generate_fake_dataframe(
        size=100,
        cols="ccii",
        col_names=["Nome","Materias","Tempo","Pontuacao"],
        intervals=[('names', 16),
                   ("subjects",9),
                   (0,1440),
                   (0,100)
                   ])
    df3.to_csv('C:\Faculdade\Iesb\Setimo semestre\Inteligencia Artificial 2\DataFrame_Random.csv', index=False)
