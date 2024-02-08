import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = []

with open("/home/andrew/Pria/MEX1_29686_processed.xdi", "r") as file:
    for line in file:
        if not line.startswith("#"):
            row = line.split()
            if row:
                data.append(row)

# Convert list to DataFrame
columns = ["energy", "bragg", "count_time", "i0", "i1", "i2"]
df = pd.DataFrame(data, columns=columns).astype(float)  # Convert strings to float

# Drop the columns bragg, count_time, and i0
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
