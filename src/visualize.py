import lightkurve as lk
import matplotlib.pyplot as plt
import numpy as np

print("=" * 50)
print("VISUALIZATION MODULE")
print("=" * 50)

# Load cleaned light curve
lc = lk.read("data/processed/toi700_clean.fits")

# Denoise
clean = lc.flatten()

time = clean.time.value
flux = clean.flux.value

# Find possible transit
min_index = np.argmin(flux)
transit_time = time[min_index]
transit_flux = flux[min_index]

plt.figure(figsize=(14,6))

# Plot light curve
plt.plot(
    time,
    flux,
    ".",
    color="royalblue",
    markersize=2,
    label="Denoised Light Curve"
)

# Highlight transit
plt.scatter(
    transit_time,
    transit_flux,
    color="red",
    s=120,
    label="Possible Transit"
)

plt.axvline(
    transit_time,
    color="green",
    linestyle="--",
    linewidth=2
)

plt.title("AI Enabled Exoplanet Detection")
plt.xlabel("Time (Days)")
plt.ylabel("Normalized Flux")
plt.grid(True)
plt.legend()

# Save graph
plt.savefig(
    "data/processed/lightcurve_result.png",
    dpi=300
)

plt.show()

print("\nLight curve saved to:")
print("data/processed/lightcurve_result.png")

print("=" * 50)
print("Visualization Completed")
print("=" * 50)