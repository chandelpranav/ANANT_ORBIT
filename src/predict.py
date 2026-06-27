import numpy as np
import torch
import torch.nn as nn


class ExoplanetCNN(nn.Module):
    def __init__(self):
        super().__init__()

        self.conv1 = nn.Conv1d(1, 16, kernel_size=5, padding=2)
        self.conv2 = nn.Conv1d(16, 32, kernel_size=5, padding=2)

        self.relu = nn.ReLU()
        self.pool = nn.MaxPool1d(2)
        self.flatten = nn.Flatten()

        dummy = torch.zeros(1, 1, 18279)
        dummy = self.pool(self.relu(self.conv1(dummy)))
        dummy = self.pool(self.relu(self.conv2(dummy)))
        flattened = dummy.numel()

        self.fc1 = nn.Linear(flattened, 64)
        self.fc2 = nn.Linear(64, 1)

    def forward(self, x):
        x = self.pool(self.relu(self.conv1(x)))
        x = self.pool(self.relu(self.conv2(x)))
        x = self.flatten(x)
        x = self.relu(self.fc1(x))
        x = torch.sigmoid(self.fc2(x))
        return x


# Load model
model = ExoplanetCNN()
model.load_state_dict(torch.load("models/exoplanet_cnn.pth"))
model.eval()

# Load dataset
data = np.load("data/processed/dataset.npz")
X = data["X"]

X = torch.tensor(X, dtype=torch.float32).unsqueeze(0).unsqueeze(0)

# Predict
with torch.no_grad():
    prediction = model(X)

print("Prediction probability:", prediction.item())

if prediction.item() > 0.5:
    print("🪐 Planet Detected")
else:
    print("❌ No Planet Detected")