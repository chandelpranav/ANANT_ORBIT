import lightkurve as lk
import matplotlib.pyplot as plt

# Load cleaned light curve
lc = lk.read("data/processed/toi700_clean.fits")

# Flatten removes long-term trends and noise
clean_lc = lc.flatten()

# Plot original and denoised
plt.figure(figsize=(10, 5))

plt.plot(lc.time.value, lc.flux.value, ".", markersize=1, label="Original")
plt.plot(clean_lc.time.value, clean_lc.flux.value, ".", markersize=1, label="Denoised")

plt.xlabel("Time")
plt.ylabel("Normalized Flux")
plt.legend()

plt.show()