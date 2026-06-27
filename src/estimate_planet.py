import lightkurve as lk
import numpy as np

# Load cleaned light curve
lc = lk.read("data/processed/toi700_clean.fits")

# Normalize
lc = lc.normalize()

# Flux values
flux = lc.flux.value

# Transit depth
transit_depth = 1 - np.min(flux)

print("=" * 40)
print("PLANET ESTIMATION")
print("=" * 40)

print(f"Transit Depth : {transit_depth:.6f}")

# Assume Sun-sized star
star_radius = 1.0  # Solar Radius

planet_radius = np.sqrt(transit_depth) * star_radius

print(f"Estimated Planet Radius : {planet_radius:.3f} Solar Radius")

earth_radius = planet_radius * 109.1

print(f"Estimated Radius : {earth_radius:.2f} Earth Radius")

print("=" * 40)

# Confidence Score
confidence = max(50, min(99, 100 - transit_depth * 1000))

print(f"Confidence : {confidence:.2f}%")

print("=" * 40)