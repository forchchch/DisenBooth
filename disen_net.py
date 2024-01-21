import torch
import torch.nn as nn

class Image_adapter(nn.Module):
    def __init__(self, hidden_size=1024):
        super().__init__()
        self.adapter = nn.Sequential(
            nn.Linear(hidden_size, hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size, hidden_size)
        )
        self.mask = nn.Parameter(torch.zeros(hidden_size))
        self.sigmoid = nn.Sigmoid()
        
    def forward(self, feature):
        out_feature = self.adapter( self.sigmoid(self.mask)*feature ) + self.sigmoid(self.mask)*feature

        return out_feature   

def cal_cos(text, img, cos):
    a = text.mean(dim=1)
    b = img.squeeze(0)
    sim = cos(a, b).mean()
    return sim