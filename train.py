import torch
import torch.nn as nn
import torch.optim as optim
from configs import get_configs
from torch.utils.data import DataLoader, random_split
from torchvision import datasets, transforms

## configs
epochs = 350
milestones = [150, 250]
lr = 0.1
batch_size = 128
c_size = [(512, 4), (512, 4)]
device = 'cuda'



