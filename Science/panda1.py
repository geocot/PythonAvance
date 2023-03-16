import science1 as np
import pandas as pd

df = pd.read_csv("signalements-coyotes.csv")
print(df[df["Nb_coyotes"] == 6])
print(df.iloc[570])

