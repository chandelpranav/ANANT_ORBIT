import lightkurve as lk

# Read the downloaded FITS file
lc = lk.read("data/raw/toi700_sector1.fits")

# Remove missing values
lc = lc.remove_nans()

# Normalize the light curve
lc = lc.normalize()

# Save the cleaned light curve
lc.to_fits(
    "data/processed/toi700_clean.fits",
    overwrite=True
)

print("✅ Preprocessing completed successfully!")
print(lc)