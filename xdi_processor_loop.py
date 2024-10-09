import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.figure(figsize=(10, 6))

for filename in os.listdir("."):
    if filename.endswith(".xdi"):

        data = []

        with open(filename, "r", encoding="utf8") as file:
            for line in file:
                if not line.startswith("#"):
                    row = line.split()
                    if row:
                        data.append(row)

        # Create a DataFrame
        columns = ["energy", "bragg", "count_time", "i0", "i1", "i2"]
        df = pd.DataFrame(data, columns=columns).astype(float)

        # Drop unnecessary columns
        df = df.drop(columns=["bragg", "count_time", "i0"])

        # Calculate ln(i1/i2)
        df["ln_i1_i2"] = np.log(df["i1"] / df["i2"])

        # Plot
        plt.plot(df["energy"], df["ln_i1_i2"], label=filename)

# Configure plot settings
plt.xlabel("Energy (eV)")
plt.ylabel("ln(i1/i2)")
plt.legend()
plt.tight_layout()
plt.savefig("xdi_processor_loop.png")
