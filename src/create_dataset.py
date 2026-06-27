import lightkurve as lk
import numpy as np
import os

# Input and output paths
input_file = "data/processed/toi700_clean.fits"
output_file = "data/processed/dataset.npz"

# Load cleaned light curve
lc = lk.read(input_file)

# Extract flux values
flux = np.array(lc.flux)

# Normalize the flux
flux = (flux - np.mean(flux)) / np.std(flux)

# Dummy label
# 1 = Planet present
label = 1

# Save dataset
np.savez(output_file, X=flux, y=label)

print("✅ Dataset created successfully!")
print("Saved to:", output_file)
print("Shape:", flux.shape)