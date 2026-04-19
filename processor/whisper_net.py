import torch
import torch.nn as nn
class WhisperNet(nn.Module):
    def __init__(self):
        super(WhisperNet, self).__init__()
        self.feature_extractor = nn.Sequential(
            nn.Conv1d(1, 16, kernel_size=15, stride=1, padding=7),
            nn.ReLU(),
            nn.MaxPool1d(2)
        )
        self.fc = nn.Linear(16, 1)
    def forward(self, x):
        x = self.feature_extractor(x)
        return torch.sigmoid(self.fc(x.mean(dim=2)))
