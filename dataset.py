import os, os.path

import pandas as pd
from torch.utils.data import Dataset
from PIL import Image

class myDataset(Dataset):

    def __init__(self, images_path_low, images_path_high, transform=None):
        super().__init__()
        self.images_path_high = images_path_high
        self.images_path_low = images_path_low
        self.transform = transform
        self.data_lenght = len([name for name in os.listdir(self.images_path_high)])

        
    def len(self):
        return self.data_lenght 

    def __len__(self):
        # len => Number of files inside the directory images_path_high.
        return self.data_lenght


    def __getitem__(self, id):
        path_low =  os.path.join(self.images_path_low, f"{id}.png")
        path_high =  os.path.join(self.images_path_high, f"{id}.png")

        # Fix number of files to solve this. Provisional fix
        while not os.path.isfile(path_low) and id < self.data_lenght:
            id += 1
            path_low =  os.path.join(self.images_path_low, f"{id}.png")
            path_high =  os.path.join(self.images_path_high, f"{id}.png")

        sample_low = Image.open(path_low)
        sample_high = Image.open(path_high)
        if self.transform:
            sample_low = self.transform(sample_low)
            sample_high = self.transform(sample_high)
        return sample_high, sample_low