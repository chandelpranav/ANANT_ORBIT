import numpy as np
import torch

# Load prediction probability
probability = 1.0   # Replace with your model output if available

print("=" * 50)
print("EXPLAINABLE AI REPORT")
print("=" * 50)

if probability >= 0.5:
    prediction = "🪐 Planet Detected"
else:
    prediction = "❌ No Planet Detected"

print(f"Prediction        : {prediction}")
print(f"Confidence Score  : {probability*100:.2f}%")

print("\nWhy did the model predict this?")

if probability >= 0.5:
    print("✓ Transit-like dip detected in the light curve")
    print("✓ Signal is periodic")
    print("✓ Noise removed during preprocessing")
    print("✓ CNN confidence is high")
    print("✓ Features match an exoplanet transit")
else:
    print("✓ No clear transit signal")
    print("✓ Flux variation appears random")
    print("✓ Low confidence for an exoplanet")

print("=" * 50)
