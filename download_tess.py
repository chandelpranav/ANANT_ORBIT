import lightkurve as lk
import os

TARGET = "TOI-700"

# Create folder if it doesn't exist
os.makedirs("data/raw", exist_ok=True)

# Search for TESS light curves
search_result = lk.search_lightcurve(
    TARGET,
    mission="TESS"
)

print(search_result)

# Download only the first light curve
lc = search_result[0].download()

# Save it as a FITS file
lc.to_fits("data/raw/toi700_sector1.fits", overwrite=True)

print("Download completed!")