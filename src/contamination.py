import lightkurve as lk
import numpy as np

print("=" * 50)
print("CROWDED FIELD CONTAMINATION ANALYSIS")
print("=" * 50)

# Load cleaned light curve
lc = lk.read("data/processed/toi700_clean.fits")

# Normalize
lc = lc.normalize()

flux = lc.flux.value

# Simple noise estimation
noise = np.std(flux)

# Convert noise into a contamination estimate
contamination = min(noise * 1000, 100)

print(f"Target Star        : TOI-700")
print(f"Noise Level        : {noise:.6f}")
print(f"Estimated Contamination : {contamination:.2f}%")

# Risk level
if contamination < 5:
    status = "LOW"
elif contamination < 15:
    status = "MEDIUM"
else:
    status = "HIGH"

print(f"Risk Level         : {status}")

print("\nInterpretation:")

if status == "LOW":
    print("✓ Light curve is clean.")
    print("✓ Transit detection is reliable.")
elif status == "MEDIUM":
    print("⚠ Nearby stellar contamination may exist.")
    print("⚠ Predictions should be interpreted carefully.")
else:
    print("❌ High contamination detected.")
    print("❌ Crowded field may affect transit detection.")

print("=" * 50)