import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

# ==========================
# Load Dataset
# ==========================

data = np.load("data/processed/dataset.npz")

X = data["X"]
y = float(data["y"])  # Convert scalar label to float

# Convert to tensors
X = torch.tensor(X, dtype=torch.float32).unsqueeze(0).unsqueeze(0)
y = torch.tensor([[y]], dtype=torch.float32)

print("Input shape:", X.shape)
print("Label:", y)

# ==========================
# CNN Model
# ==========================

class ExoplanetCNN(nn.Module):
    def __init__(self):
        super().__init__()

        self.conv1 = nn.Conv1d(
            in_channels=1,
            out_channels=16,
            kernel_size=5,
            padding=2
        )

        self.conv2 = nn.Conv1d(
            in_channels=16,
            out_channels=32,
            kernel_size=5,
            padding=2
        )

        self.relu = nn.ReLU()
        self.pool = nn.MaxPool1d(2)
        self.flatten = nn.Flatten()

        # Calculate flattened size automatically
        with torch.no_grad():
            dummy = torch.zeros(1, 1, X.shape[-1])
            dummy = self.pool(self.relu(self.conv1(dummy)))
            dummy = self.pool(self.relu(self.conv2(dummy)))
            flattened_size = dummy.numel()

        self.fc1 = nn.Linear(flattened_size, 64)
        self.fc2 = nn.Linear(64, 1)

    def forward(self, x):
        x = self.pool(self.relu(self.conv1(x)))
        x = self.pool(self.relu(self.conv2(x)))
        x = self.flatten(x)
        x = self.relu(self.fc1(x))
        x = torch.sigmoid(self.fc2(x))
        return x


# ==========================
# Create Model
# ==========================

model = ExoplanetCNN()

criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# ==========================
# Training Loop
# ==========================

epochs = 20

for epoch in range(epochs):

    optimizer.zero_grad()

    output = model(X)

    loss = criterion(output, y)

    loss.backward()

    optimizer.step()

    print(
        f"Epoch {epoch + 1}/{epochs} | Loss = {loss.item():.6f}"
    )

# ==========================
# Save Model
# ==========================

torch.save(model.state_dict(), "models/exoplanet_cnn.pth")

print("\n✅ Training completed successfully!")
print("✅ Model saved as: models/exoplanet_cnn.pth")