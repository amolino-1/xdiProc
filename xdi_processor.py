import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = []

with open("MEX1_29687_processed.xdi", "r", encoding="utf8") as file:
    for line in file:
        if not line.startswith("#"):
            row = line.split()
            if row:
                data.append(row)

columns = ["energy", "bragg", "count_time", "i0", "i1", "i2"]
df = pd.DataFrame(data, columns=columns).astype(float)

df = df.drop(columns=["bragg", "count_time", "i0"])

print(df.head())
print("\n")

df["ln_i1_i2"] = np.log(df["i1"] / df["i2"])

print(df.head())
print("\n")


plt.plot(df["energy"], df["ln_i1_i2"])
plt.xlabel("Energy")
plt.ylabel("ln(i1/i2)")
plt.show()
