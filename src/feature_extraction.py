import lightkurve as lk
import numpy as np
import matplotlib.pyplot as plt

# Load cleaned light curve
lc = lk.read("data/processed/toi700_clean.fits")

# Create period range (1 to 20 days)
periods = np.linspace(1, 20, 10000)

# Compute BLS periodogram
periodogram = lc.to_periodogram(
    method="bls",
    period=periods
)

# Plot
periodogram.plot()
plt.title("BLS Periodogram")
plt.show()

# Best period
print("Best period:")
print(periodogram.period_at_max_power)